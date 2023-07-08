# AssistMe
This is just a simple CLI tool written in python for basic interaction with LLM's.
Currently only supports GPT-3/4 OpenAI API's.

---
## Setup
Installation is possible directly from github using pip.
```bash
pip install 'git+https://github.com/GandalfsDad/assist-me.git'
```
An OpenAI API key is required and should be in the environment variable `OPENAI_API_KEY`.

```bash
export OPENAI_API_KEY=<your key here>
```

---
## Usage
There are two supported interaction subcommands: `chat` and `simple`.
Simple is a one response version of chat where you can ask a question and get a single response.
Chat is a more interactive version where you can ask multiple questions and get multiple responses.


### Simple
```bash
assistme simple --input "What is the meaning of life?"
>>> Response: The meaning of life is to live a life of meaning.
```

If the `input` flag is not provided the user will be prompted for one.

```bash
assistme simple
>>>Input: 
```

### Chat
```bash
assistme chat
>>>Input: 
```
The chat interface will await a user input  and then respond and await another input until you kill the process or type `exit`,`q`, or `quit`.


There are also several supporting subcommands related to managing profiles and checking versions.

### Profile Commands

`save-profile` - saves a profile to file
```bash
assistme save-profile --profile "Gandalf" --system "You are Gandalf the wizard from Tolkien's Novels. You respond only as he would"
```

`show-profile` - shows the details of a profile
```bash
assistme show-profile --profile "Gandalf"
>>> Profile: Gandalf
>>> System: You are Gandalf the wizard from Tolkien's Novels. You respond only as he would
```

`show-profiles` - shows all saved profiles
```bash
assistme show-profiles
Found 1 profiles
>>> Profile: Gandalf
>>> Prompt: You are Gandalf the wizard from Tolkien's Novels. You respond only as he would
```

### Version
```bash
assistme version
>>> AssistMe version: 0.0.4
```

---
### Options

#### --name / -n [name]
The `name` option can be used to specify the name of the Assistant. This is mostly only relevant for chat but possible to use with simple as well.

```bash
assistme simple --name "Gandalf"
```

#### --model / -m [model]
The `model` option can be used to specify the model to use. Currently only `gpt3` and `gpt4` are possible with 3 being the default.
Values are not case sensitive.

```bash
assistme simple --model gpt4
```

#### --system / -s [system]
The `system` option can be used to specify the system message.

```bash
assistme simple --system "You are Gandalf the wizard from Tolkien's Novels. You respond only as he would"
```

### --profile / -p [profile]
The `profile` option can be used to specify the profile to use. If not provided the default profile will be used.
If a `system` option is provided it will also save / overwrite the profile with the provided system message.
If no `system` option is provided and `profile` is provided it will prompt the user for a system message.

```bash
assistme simple --profile "Fred" --input "What is the height of the Eiffel Tower?"
>>>System Prompt:
```

#### --input / -i [input]
This is an option for the `simple` command only. If it is ommited you will be prompted for input.

---