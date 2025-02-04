
<p align="center">
  <picture>    
    <img alt="auto-coder" src="https://github.com/allwefantasy/byzer-llm/blob/master/docs/source/assets/logos/logo.jpg" width=55%>
  </picture>
</p>

<h3 align="center">
Auto-Coder (powered by Byzer-LLM)
</h3>

<p align="center">
| <a href="./README.md"><b>English</b></a> | <a href="./README-CN.md"><b>中文</b></a> |

</p>

---

*Latest News* 🔥

- [2024/03] Release Auto-Coder 0.1.16

---



🚀 Attention developers! 🚨 The game-changing Auto-Coder has arrived, and it's about to take your AI programming to a whole new level! 🌟

Fueled by the incredible power of Byzer-LLM, this command-line tool is packed with features that will blow your mind:

📂 Say goodbye to manual context gathering! Auto-Coder intelligently generates code based on the context of your source directory. It's like having a genius assistant that knows exactly what you need!

💡 Two modes, endless possibilities! Generate perfect prompts to paste into web-based large models, or let Auto-Coder work its magic directly with private models via Byzer-LLM. The choice is yours, and the results are always spectacular!

💻 Python? TypeScript? No problem! Auto-Coder supports all the cool kids on the programming block.

🌍 Going global is a breeze! Auto-Coder automatically translates your project files, so your code can conquer the world!

🤖 Copilot mode is here, and it's your new best friend! With its built-in shell/Jupyter engine, Auto-Coder breaks down tasks, sets up environments, creates projects, and even modifies code for you. It's like having a super-smart sidekick that never sleeps!

🧑‍💻 Developers, prepare to have your minds blown! Auto-Coder integrates seamlessly with the hottest AI models like ChatGPT, turbocharging your development process to lightning speeds! 🚀

🌟 Don't wait another second! Experience the raw power of Auto-Coder today and let AI be your ultimate coding companion! https://github.com/allwefantasy/auto-coder 🔥

#AutoCoder #AIProgramming #GameChanger #ByzerLLM #DevTools

## Table of Contents

- [Installation](#installation)
- [Brand new Installation](#raw-meta-matchine-installation)
- [Usage](#usage)
  - [Basic](#basic)
  - [Advanced](#advanced)
  - [Python Project Only Features](#python-project-only-features)
  - [TypeScript Project](#typescript-project)
  - [Real-Auto](#real-auto)
    - [Real-Auto with Search Engine](#real-auto-with-search-engine)



## Installation

```shell
conda create --name autocoder python=3.10.11
conda activate autocoder
pip install -U auto-coder
## if you want to use private/open-source models, uncomment this line.
# pip install -U vllm
ray start --head
```

## Raw Meta Matchine Installation

You can use the script provided by Byzer-LLM to setup the nvidia-driver/cuda environment:

1. [CentOS 8 / Ubuntu 20.04 / Ubuntu 22.04](https://docs.byzer.org/#/byzer-lang/zh-cn/byzer-llm/deploy)

After the nvidia-driver/cuda environment is set up, you can install auto_coder like this:

```shell
pip install -U auto-coder
```


## Usage 

### LLM Model

> Recommend to use 千义通问Max/Qwen-Max SaaS model
> Make sure your model has at least 8k context.

Try to use the following command to deploy Qwen-Max:

```shell
byzerllm deploy  --pretrained_model_type saas/qianwen \
--infer_params saas.api_key=xxxxxxx saas.model=qwen-max \
--model qianwen_chat 
```

Then you can use the following command to test the model:

```shell
byzerllm query --model qianwen_chat --query "你好"
```

If you want to undeploy the model:

```shell
byzerllm undeploy --model qianwen_chat
```

If you want to deploy you private/open source model, please try to this [link](https://github.com/allwefantasy/byzer-llm)

### Basic 


The auto-coder provide two ways:

1. Generate context for the query and you can copy&&Paste to Web UI of ChatGPT/Claud3/Kimi.
2. Use the model from Byzer-LLM to generate the result directly.

>> Note: You should make sure the model has a long context length support, e.g. >32k. 

The auto-coder will collect the source code from the source directory, and then generate context into the target file based on the query.

Then you can copy the content of `output.txt` and paste it to Web UI of ChatGPT/Claud3/Kimi:

For example:

```shell
auto-coder --source_dir /home/winubuntu/projects/ByzerRawCopilot --target_file /home/winubuntu/projects/ByzerRawCopilot/output.txt --query "如何让这个系统可以通过 auto-coder 命令执行？" 
```

You can also put all arguments into a yaml file:


```yaml
# /home/winubuntu/projects/ByzerRawCopilot/auto-coder.yaml
source_dir: /home/winubuntu/projects/ByzerRawCopilot
target_file: /home/winubuntu/projects/ByzerRawCopilot/output.txt
query: |
  如何让这个系统可以通过 auto-coder 命令执行？
```
  
Then use the following command:

```shell
auto-coder --file /home/winubuntu/projects/ByzerRawCopilot/auto-coder.yaml
``` 

If you want to use the model from Byzer-LLM, you can use the following command:

```shell
auto-coder --source_dir /home/winubuntu/projects/ByzerRawCopilot --target_file /home/winubuntu/projects/ByzerRawCopilot/output.txt --model qianwen_chat --execute --query "重新生成一个 is_likely_useful_file 方法，满足reactjs+typescript 组合的项目。" 
```

In the above command, we provide a model and enable the execute mode, the auto-coder will collect the source code from the source directory, and then generate context for the query, and then use the model to generate the result, then put the result into the target file.

### How to reduce the context length?

As you may know, auto-coder will collect the source code from the source directory, and then generate context for the query, if the source directory is too large, the context will be too long, and the model may not be able to handle it.

There are two ways to reduce the context length:

1. Change the source_dir to sub directory of project.
2. Enable aut-coder's index feature.

In order to use the index feature, you should configure some extra parameters:

1. skip_build_index: false
2. model

For example:

```yaml
source_dir: /home/winubuntu/projects/ByzerRawCopilot 
target_file: /home/winubuntu/projects/ByzerRawCopilot/output.txt 

model: qianwen_chat
model_max_length: 2000
model_max_input_length: 6000
anti_quota_limit: 13

skip_build_index: false

project_type: "copilot/.py"
query: |
  优化 copilot 里的 get_suffix_from_project_type 函数并更新原文件
```

Here we add a new parameter `skip_build_index`, by default, this value is true. 
If you set it to false and a model provide at the same time, then the auto-coder will generate index for the source code using the model(This may cost a lot of tokens), and the index file will be stored in a directory called `.auto-coder` in source directory. 

Once the index is created, the auto-coder will use the index to filter files and reduce the context length. notice that the filter action also use model, and it may cost tokens, so you should use it carefully.


### Advanced

> This feature only works with the model from Byzer-LLM.

Translate the markdown file in the project:

```shell

auto-coder --source_dir /home/winubuntu/projects/ByzerRawCopilot --target_file /home/winubuntu/projects/ByzerRawCopilot/output.txt --project_type "translate/中文/.md/cn" --model_max_length 2000 --model qianwen_chat 
```
When you want to translate some files, you must specify the model parameter. And the project_type is a litle bit complex, it's a combination of the following parameters:

- translate: the project type
- 中文: the target language you want to translate to
- .md: the file extension you want to translate
- cn: the new file suffix created with the translated content. for example, if the original file is README.md, the new file will be README-cn.md

So the final project_type is "translate/中文/.md/cn"

If your model is powerful enough, you can use the following command to do the same task:

```shell
auto-coder --source_dir /home/winubuntu/projects/ByzerRawCopilot --target_file /home/winubuntu/projects/ByzerRawCopilot/output.txt --model qianwen_chat --project_type translate --model_max_length 2000 --query "把项目中的markdown文档翻译成中文"
```

The model will extract "translate/中文/.md/cn" from the query and then do the same thing as the previous command.

Note: The model_max_length is used to control the model's generation length, if the model_max_length is not set, the default value is 1024.
You should change the value based on your esitmating on the length of the translation.


### Python Project Only Features

In order to reduce the context length collected by the auto-coder, if you are dealing with a python project, you can use the following command:


```shell
auto-coder --target_file /home/winubuntu/projects/ByzerRawCopilot/output.txt --script_path /home/winubuntu/projects/ByzerRawCopilot/xxx --package_name byzer_copilot --project_type py-script --query "帮我实现script模块中还没有实现方法"

```

In the above command, we provide a script path and a package name, the script_path is the python file you are working on now, and the package_name 
is you cares about, then the auto-coder only collect the context from the package_name and imported by the script_path file, this will significantly reduce the context length.

When you refer `script module` in `--query`, you means you are talking about script_path file.

After the job is done, you can copy the prompt from the output.txt and paste it to Web of ChatGPT or other AI models.

If you specify the model, the auto-coder will use the model to generate the result, then put the result into the target file.

```shell
auto-coder --target_file /home/winubuntu/projects/ByzerRawCopilot/output.txt --script_path /home/winubuntu/projects/YOUR_PROJECT/xxx.py --package_name xxxx --project_type py-script --model qianwen_chat --execute --query "帮我实现script模块中还没有实现方法" 
```

## TypeScript Project

Just try to set the project_type to ts-script.

## Real-Auto


Here is a example:

```shell
auto-coder --source_dir /home/winubuntu/projects/ByzerRawCopilot --target_file /home/winubuntu/projects/ByzerRawCopilot/output.txt --project_type copilot --model_max_length 2000 --model qianwen_chat  --query "帮我创建一个名字叫t-copilot 的python项目，生成的目录需要符合包装的python项目结构"

```

This project type will automatically create a python project based on the query, and then generate the result based on the query. 

You can check all log in the `output.txt` file.

auto-coder also support python code interpreter,try this:
  
```shell 
auto-coder --source_dir /home/winubuntu/projects/ByzerRawCopilot --target_file /home/winubuntu/projects/ByzerRawCopilot/output.txt --project_type copilot --model_max_length 2000 --model qianwen_chat  --query "用python打印你好，中国" 
```

The content of the output.txt will be:

```text
=================CONVERSATION==================

user: 
根据用户的问题，对问题进行拆解，然后生成执行步骤。

环境信息如下:
操作系统: linux 5.15.0-48-generic  
Python版本: 3.10.11
Conda环境: byzerllm-dev 
支持Bash

用户的问题是：用python打印你好，中国

每次生成一个执行步骤，然后询问我是否继续，当我回复继续，继续生成下一个执行步骤。

assistant: 
{
  "code": "print('你好，中国')",
  "lang": "python",
  "total_steps": 1,
  "cwd": "",
  "env": {},
  "timeout": -1,
  "ignore_error": false
}

是否继续？
user: 继续
=================RESULT==================

Python Code:
print('你好，中国')
Output:
你好，中国
--------------------
```

### Real-Auto with Search Engine

If you want to get a more stable result, you should introduce search engine:

```yaml
source_dir: /home/winubuntu/projects/ByzerRawCopilot 
target_file: /home/winubuntu/projects/ByzerRawCopilot/output.txt 

model: qianwen_short_chat
model_max_length: 2000
anti_quota_limit: 5

search_engine: bing
search_engine_token: xxxxxx

project_type: "copilot"
query: |
  帮我在/tmp/目录下创建一个 typescript + reactjs 组成的项目，项目名字叫 t-project
```

Here we add  new parameters  `search_engine` and `search_engine_token`, the search engine will provide more context for the model, and the model will use the context to generate the result.

For now, we support bing/google.  If you use bing, try to get the token from [here](https://www.microsoft.com/en-us/bing/apis/bing-web-search-api).

The basic workflow is:

1. search the query 
2. reranking the search result by snippets
3. fetch the first search result and answer the question based on the full content.
4. generate the result based on the query and the full content.
5. get execute steps based on the result.
5. execute the steps by ShellClient/PythonClient in auto-coder.

Here is the output:

```text
用户尝试: UserIntent.CREATE_NEW_PROJECT
search SearchEngine.BING for 帮我在/tmp/目录下创建一个 typescript + reactjs 组成的项目，项目名字叫 t-project...
reraking the search result by snippets...
fetch https://blog.csdn.net/weixin_42429718/article/details/117402097 and answer the quesion (帮我在/tmp/目录下创建一个 typescript + reactjs 组成的项目，项目名字叫 t-project) based on the full content...
user: 
你熟悉各种编程语言以及相关框架对应的项目结构。现在，你需要
根据用户的问题，根据提供的信息，对问题进行拆解，然后生成执行步骤，当执行完所有步骤，最终帮生成一个符合对应编程语言规范以及相关框架的项目结构。
整个过程只能使用 python/shell。

环境信息如下:
操作系统: linux 5.15.0-48-generic  
Python版本: 3.10.11
Conda环境: byzerllm-dev 
支持Bash

现在请参考下面内容：

由于提供的上下文信息与在Linux环境下使用命令行创建一个TypeScript和ReactJS项目无关，我将基于一般操作步骤给出解答。

要在Linux系统的 `/tmp/` 目录下创建一个由TypeScript和ReactJS组成的项目，并命名为`t-project`，请按照以下步骤操作：

1. 首先，请确保您已全局安装了Node.js包管理器（npm）以及创建React应用的脚手架工具 `create-react-app`。如果尚未安装，可以通过以下命令安装：
   ```
   npm install -g create-react-app
   ```

2. 然后，由于`create-react-app`默认不支持 TypeScript，需要安装 `create-react-app` 的 TypeScript 版本，即 `react-scripts-ts`，但请注意，`react-scripts-ts` 已不再维护，最新推荐做法是直接使用 `create-react-app` 并通过 `--template typescript` 参数指定 TypeScript 模板：

   ```sh
   npx create-react-app t-project --template typescript
   ```

   这条命令会在 `/tmp/` 目录下创建名为 `t-project` 的新React项目，并配置为使用TypeScript。

3. 创建完成后，进入项目目录并启动开发服务器：

   ```sh
   cd /tmp/t-project
   npm start
   ```

这样就成功在 `/tmp/` 目录下创建了一个基于TypeScript和ReactJS的项目。[information is missing on]如何具体使用命令行在Linux系统中创建项目，因为上下文没有提供相关指导。

用户的问题是：帮我在/tmp/目录下创建一个 typescript + reactjs 组成的项目，项目名字叫 t-project

每次生成一个执行步骤，然后询问我是否继续，当我回复继续，继续生成下一个执行步骤。        

assistant: ```json
{
  "code": "npm install -g create-react-app",
  "lang": "shell",
  "total_steps": 3,
  "current_step": 1,
  "cwd": "/tmp",
  "env": {},
  "timeout": null,
  "ignore_error": false
}
```
请确认是否已安装全局的 `create-react-app` 工具。如果确认或执行完成，请回复“继续”。

user: 继续

assistant: ```json
{
  "code": "npx create-react-app t-project --template typescript",
  "lang": "shell",
  "total_steps": 3,
  "current_step": 2,
  "cwd": "/tmp",
  "env": {},
  "timeout": null,
  "ignore_error": false
}
```
请在 `/tmp` 目录下执行此命令以创建基于 TypeScript 的 ReactJS 项目。如果项目创建完成，请回复“继续”。

user: 继续

assistant: ```json
{
  "code": "cd t-project",
  "lang": "shell",
  "total_steps": 3,
  "current_step": 3,
  "cwd": "/tmp",
  "env": {},
  "timeout": null,
  "ignore_error": false
}
```
请在终端中切换到刚创建的 `t-project` 目录。若切换成功，请回复“继续”以进行下一步操作，即启动项目开发服务器。

user: 继续
```

There are three steps to create the new project, and the ShellClient in auto-coder will finally execute the three steps.
