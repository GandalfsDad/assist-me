import openai
from .pompts import BASE_SYSTEM_PROMPT
from ...CLI.format import format_input, format_response
from . import DEFAULT_MAX_TOKENS, DEFAULT_TEMPERATURE
import click

class Chat:

    def __init__(self, model: str, name: str, system_prompt : str = BASE_SYSTEM_PROMPT, max_tokens : int = DEFAULT_MAX_TOKENS, temperature : float = DEFAULT_TEMPERATURE):
        self.model = model
        self.name = name
        self.__max_tokens = max_tokens
        self.__temperature = temperature
        self.__history = []
        self.__system_prompt = system_prompt

        self._setup()

    def _setup(self) -> None:
        self.__history.append({"role":"system","content":self.__system_prompt})

    def generate_response(self, input : str) -> None:
        self.__history.append({"role":"user","content":input})
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.__history,
            max_tokens=self.__max_tokens,
            temperature=self.__temperature
        )

        response_text = response['choices'][0]['message']['content']

        self.__history.append({"role":"system","content":response_text})
        click.echo(format_response(self.name, response_text))
    
    def interactive(self) -> None:
        while True:
            input_text = click.prompt(format_input("You: "))
            if input_text.lower() in ["exit","q","quit","exit()","quit()","kill"]:
                break
            self.generate_response(input_text)
            