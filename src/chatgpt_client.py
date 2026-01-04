import time

import openai


class ChatGPTClient:
    def __init__(self):
        # https://platform.openai.com/account/api-keys
        # Replace YOUR_API_KEY with your OpenAI API key
        openai.api_key = ""

        # Set the model
        self.model_engine = "text-curie-001"
        # Set the maximum number of tokens to generate in the response
        self.max_tokens = 1024

    def get_response(self, prompt):
        # Generate a response
        t = time.time()
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=self.max_tokens,
            temperature=0.5,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        print("time taken: ", time.time() - t)

        # Print the response
        print(completion.choices[0].text)

        return completion.choices[0].text
