# 使用说明

ChatGPT_PyBot 是一个基于 Python 开发的命令行机器人。

若要使用`ChatGPT_PyBot`，**你需要拥有一个openai账号，且在一台可以正常登录到`ChatGPT`网页版的机器上进行**。

## 安装

`ChatGPT_PyBot`已经上传至`Pypi`，你可以在终端执行如下代码进行安装

```shell
pip install ChatGPT_PyBot --upgrade
```

或者也可以通过GitHub安装

```shell
pip install git+https://github.com/liuhuanshuo/ChatGPT_PyBot
```



## 配置（非常重要）

安装完毕之后，需要配置登录文件。`ChatGPT_PyBot`提供两种方式进行登录验证。

### 使用账号密码

在当前目录下新建一个`config.json`文件，内容如下：

```json
{
    "email":"<EMAIL>",
    "password": "<PASSWORD>"
}
```

填入你的账号密码即可。

注意：如果你在`openai`所不支持的地区使用账号密码，需要配置终端走代理流量，否则会无法验证。

你可以使用如下代码检查你的终端ip地址已确保终端的ip属于可用区域

```shell
curl cip.cc
```

### 使用Cookie

如果上面的配置方案没有作用，这时可以使用第二种方式，别担心，一点也不困难。

首先需要登录ChatGPT，并按下F12或者 右键 - 检查

![](https://pic.liuzaoqi.com/picgo/202212091104801.png)

点击 `Application`

![](https://pic.liuzaoqi.com/picgo/202212091105819.png)

按照如下指示复制`Cookie Value`

![](https://pic.liuzaoqi.com/picgo/202212091107424.png)

同样的，在当前目录下新建一个`config.json`文件，内容如下：

```json
{
    "session_token":"Your Cookie Value"
}
```



## CLI使用



打开终端（命令行），确保当前的目录下有配置好的`config.json`文件，执行`chatgpt`即可进入交互式对话框

```shell
$ chatgpt
```

![](https://pic.liuzaoqi.com/picgo/202212091115468.png)

如果只需要单次的提问，可以直接在`chatgpt`后添加你的问题

```shell
$ chatgpt your question
```

![](https://pic.liuzaoqi.com/picgo/202212091119492.png)



## 致谢

本项目从[ChatGPT - 一个OpenAI 的逆向工程]( https://github.com/acheong08/ChatGPT)中得到灵感。