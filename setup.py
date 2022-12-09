from setuptools import setup, find_packages

# with open("readme.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

setup(
    name="ChatGPT_PyBot",
    version="0.4",
    license="GNU General Public License v2.0",
    author="Liuhuanshuo",
    author_email="huanshuo080l@gmail.com",
    description="A Python based ChatGPT robot",
    long_description=open("readme.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/liuhuanshuo/ChatGPT_PyBot",
    packages=find_packages(),
    install_requires=[
        "rich",
        "requests",
        "OpenAIAuth"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "chatgpt = ChatGPT_PyBot.chatgpt:main"
        ]
    },
)
