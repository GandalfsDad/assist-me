import google.generativeai as palm
from .defaults import DEFAULT_CONTEXT, DEFAULT_TEMPERATURE
from ...CLI.format import format_input, format_response
import click

class Chat:
    def __init__(self, model: str, name: str, context: str = DEFAULT_CONTEXT, temperature : float = DEFAULT_TEMPERATURE):
        self.model = model
        self.name = name
        self.__context = context
        self.__temperature = temperature

        self.__last_response = None
    
    def generate_response(self, input : str) -> None:
        if self.__last_response is None:
            self.__last_response = palm.chat(model=self.model, context =self.__context, temperature=self.__temperature, messages = input) 
        else:
            self.__last_response = self.__last_response.reply(input)
        
        click.echo(format_response(self.name, self.__last_response.last))
    
    def interactive(self) -> None:
        while True:
            input_text = click.prompt(format_input("You: "))
            if input_text.lower() in ["exit","q","quit","exit()","quit()","kill"]:
                break
            self.generate_response(input_text)
