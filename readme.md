# ChatGPT-PyBot

<p align="center"><a href="https://github.com/liuhuanshuo/ChatGPT_PyBot">En</a>|<a href="https://github.com/liuhuanshuo/ChatGPT_PyBot/blob/main/Docs/cn_doc.md">Cn</a></p>

![](https://pic.liuzaoqi.com/picgo/202212091444750.png)

## Usage

ChatGPT_PyBot is a command-line robot developed in Python.

To use ChatGPT_PyBot, you need to have an openai account and use it on a machine that can log into the ChatGPT web version.

## Install

`ChatGPT_PyBot` has been uploaded to `Pypi`, you can execute the following code in the terminal to install

```shell
pip install ChatGPT_PyBot --upgrade
```

Or you can install it via GitHub

```shell
pip install git+https://github.com/liuhuanshuo/ChatGPT_PyBot
```

## Configuration (very important❗️)

After the installation is complete, you need to configure the login file. ChatGPT_PyBot provides two ways to verify login.

### Use account password

Create a `config.json` file in the current directory with the following contents:

```json
{
    "email":"<EMAIL>",
    "password": "<PASSWORD>"
}
```

Just fill in your account password.

**Note:** If you use an account password in an area not supported by `openai`, you need to configure the terminal to go through proxy traffic, otherwise it will not be verified.

You can use the following code to check your terminal ip address to ensure that the terminal ip address belongs to the available region

```shell
curl cip.cc
```

### Use Cookie

If the above configuration scheme does not work, then you can use the second method, don't worry, it is not difficult at all.

First you need to log in to ChatGPT and press F12 or right-click - Check

![](https://pic.liuzaoqi.com/picgo/202212091104801.png)

click `Application`

![](https://pic.liuzaoqi.com/picgo/202212091105819.png)

Copy the `Cookie Value` as instructed below

![](https://pic.liuzaoqi.com/picgo/202212091107424.png)

Similarly, create a `config.json` file in the current directory with the following contents:

```json
{
    "session_token":"Your Cookie Value"
}
```

## CLI Usage

Open the terminal (command line), ensure that the current directory has the configured `config.json` file, execute `chatgpt` to enter the interactive dialog box

```shell
$ chatgpt
```

![](https://pic.liuzaoqi.com/picgo/202212091115468.png)

If you only need a single question, you can add your question directly after chatgpt

```shell
$ chatgpt your question
```

![](https://pic.liuzaoqi.com/picgo/202212091119492.png)

## Python Usage

If you need to call ChatGPT in Python, you can do something like this

```python
>>> from ChatGPT_PyBot import ChatBot
>>> config = {
    "session_token":"Your token"
    				or
    "email": "<YOUR_EMAIL>",
    "password": "<YOUR_PASSWORD>"
}
>>> chatbot = ChatBot(config, conversation_id=None)
>>> chatbot.get_chat_response('hello world')["message"]


'''
"Hello there! It's nice to meet you. Is there anything I can help you with today? I'm here to answer any questions you might have."
'''
```



## TO DO

- [ ] Better way to log in (Now this is a little cumbersome, but it's a little difficult to implement a new approach)
- [ ] Refresh the session and reset the session



## Acknowledgments

This project is inspired by [ChatGPT - A reverse engineering of OpenAI]( https://github.com/acheong08/ChatGPT)

