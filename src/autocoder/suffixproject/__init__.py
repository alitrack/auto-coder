from autocoder.common import SourceCode,AutoCoderArgs
from autocoder import common as FileUtils  
from autocoder.utils.rest import HttpDoc
import os
from typing import Optional, Generator, List, Dict, Any, Callable
from git import Repo
import byzerllm
from autocoder.common.search import Search,SearchEngine

class SuffixProject():
    
    def __init__(self, args: AutoCoderArgs, llm: Optional[byzerllm.ByzerLLM] = None,file_filter=None):
        self.args = args
        self.directory = args.source_dir
        self.git_url = args.git_url        
        self.target_file = args.target_file  
        self.project_type = args.project_type
        self.suffixs = [f".{suffix}" if not suffix.startswith('.') else suffix for suffix in self.project_type.split(",") if suffix.strip() != ""]
        self.file_filter = file_filter
        self.sources = []
        self.llm = llm

    def output(self):
        return open(self.target_file, "r").read()                

    def is_suffix_file(self, file_path):
        return any([file_path.endswith(suffix) for suffix in self.suffixs])

    def read_file_content(self, file_path):
        with open(file_path, "r") as file:
            return file.read()

    def convert_to_source_code(self, file_path):                               
        module_name = file_path
        source_code = self.read_file_content(file_path)            
        return SourceCode(module_name=module_name, source_code=source_code)
    
    def get_source_codes(self) -> Generator[SourceCode, None, None]:
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                file_path = os.path.join(root, file)
                
                if self.is_suffix_file(file_path):
                
                    if self.file_filter is None or self.file_filter(file_path,self.suffixs):
                        print(f"====Filter {file_path}",flush=True)
                        source_code = self.convert_to_source_code(file_path)
                        if source_code is not None:
                            yield source_code

    def get_rest_source_codes(self) -> Generator[SourceCode, None, None]:
        if self.args.urls:
            http_doc = HttpDoc(urls=self.args.urls.split(","), llm=self.llm)
            sources = http_doc.crawl_urls()         
            return sources
        return []  

    def get_search_source_codes(self):
        if self.args.search_engine and self.args.search_engine_token:
            if self.args.search_engine == "bing":
                search_engine = SearchEngine.BING
            else:
                search_engine = SearchEngine.GOOGLE

            searcher=Search(llm=self.llm,search_engine=search_engine,subscription_key=self.args.search_engine_token)
            search_context = searcher.answer_with_the_most_related_context(self.args.query)  
            return [SourceCode(module_name="SEARCH_ENGINE", source_code=search_context)]
        return []                             

    def run(self):
        if self.git_url is not None:
            self.clone_repository()

        if self.target_file is None:     
            for code in self.get_rest_source_codes():
                self.sources.append(code)
                print(f"##File: {code.module_name}")
                print(code.source_code)

            for code in self.get_search_source_codes():
                self.sources.append(code)
                print(f"##File: {code.module_name}")
                print(code.source_code)    

            for code in self.get_source_codes():
                self.sources.append(code)
                print(f"##File: {code.module_name}")
                print(code.source_code)                
        else:            
            with open(self.target_file, "w") as file:
                for code in self.get_rest_source_codes():
                    self.sources.append(code)
                    file.write(f"##File: {code.module_name}\n")
                    file.write(f"{code.source_code}\n\n")

                for code in self.get_search_source_codes():
                    self.sources.append(code)
                    file.write(f"##File: {code.module_name}\n")
                    file.write(f"{code.source_code}\n\n")    
                    
                for code in self.get_source_codes():
                    self.sources.append(code)
                    file.write(f"##File: {code.module_name}\n")
                    file.write(f"{code.source_code}\n\n")
                    
    
    def clone_repository(self):   
        if self.git_url is None:
            raise ValueError("git_url is required to clone the repository")
             
        if os.path.exists(self.directory):
            print(f"Directory {self.directory} already exists. Skipping cloning.")
        else:
            print(f"Cloning repository {self.git_url} into {self.directory}")
            Repo.clone_from(self.git_url, self.directory)