'''
Adapted from https://github.com/kojima-takeshi188/zero_shot_cot
'''

import time

import openai


# # defining a function to create the prompt from the system message and the messages
# def create_prompt(system_message, messages):
#     prompt = system_message
#     message_template = "\n<|im_start|>{}\n{}\n<|im_end|>"
#     for message in messages:
#         prompt += message_template.format(message['sender'], message['text'])
#     prompt += "\n<|im_start|>assistant\n"
#
#     # print(prompt)
#     return prompt


# Sentence Generator (Decoder) for GPT-3 ...
def decoder_for_gpt35(input, max_length):
    time.sleep(1)

    # defining the system message
    system_message_template = "<|im_start|>system\n{}\n<|im_end|>"
    system_message = system_message_template.format("你现在是我的智能助手")

    # creating a list of messages to track the conversation
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": input},
            # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            # {"role": "user", "content": "Where was it played?"}
        ],
        temperature=0.7,
        max_tokens=max_length,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
    )

    # response = openai.Completion.create(
    #     engine=settings.api_engine,
    #     prompt=create_prompt(system_message, messages),
    #     temperature=0.7,
    #     max_tokens=max_length,
    #     top_p=0.95,
    #     frequency_penalty=0,
    #     presence_penalty=0,
    #     stop=["<|im_end|>"]
    # )

    # return response['choices'][0]['text']
    return response['choices'][0]['message']["content"]


class Decoder():
    def __init__(self):
        # print_now()
        pass
 
    def decode(self, input, max_length):
        # response = decoder_for_gpt3(args, input, max_length)
        response = decoder_for_gpt35(input, max_length)
        return response


