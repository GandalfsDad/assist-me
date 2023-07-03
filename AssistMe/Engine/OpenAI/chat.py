import openai
from .pompts import BASE_SYSTEM_PROMPT

class Chat:

    def __init__(self, model: str, system_prompt : str = BASE_SYSTEM_PROMPT):
        self.model = model
        self.__history = []
        self.__system_prompt = system_prompt

        self._setup()

    def _setup(self) -> None:
        self.__history.append({"role":"system","content":self.__system_prompt})

    def genResponse(self, input : str) -> str:
        self.__history.append({"role":"user","content":input})
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.__history,
        )

        response_text = response['choices'][0]['message']['content']

        self.__history.append({"role":"system","content":response_text})
        return response_text
    
    def interactive(self) -> None:
        while True:
            input_text = input("Input: ")
            if input_text.lower() in ["exit","q","quit","exit()","quit()","kill"]:
                break
            response = self.genResponse(input_text)
            print(f"Response: {response}")