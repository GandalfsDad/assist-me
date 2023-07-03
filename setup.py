from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="AssistMe",
    version="0.0.2",
    author="GandalfsDad",
    description="CLI GPT helper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GandalfsDad/assist-me",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10", 
    install_requires=[
        'openai',
        'colorama',
        'click'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts':[
            'assistme=AssistMe.CLI.main:cli'
        ]
    }
)
