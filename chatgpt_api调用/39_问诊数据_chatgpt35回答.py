import argparse
import json
import random
import sys

from utils import *

import os
from settings import *

import openai

# openai.api_type = api_type
# openai.api_base = api_base
# openai.api_version = api_version
openai.api_key = api_key

decoder = Decoder()


if __name__ == "__main__":

    file_index = sys.argv[1]


    list_samples = []
    # f_out = open(f"预训练数据/chatgpt_api调用/splits/corpus_{file_index}_hpc.jsonl", "a", encoding="utf-8", buffering=1)
    f_out = open(f"chatgpt_api调用/from/corpus_{file_index}_hpc.jsonl", "a", encoding="utf-8", buffering=1)

    # with open(f"预训练数据/datasets/39_问诊数据/splits/corpus_{file_index}.jsonl", "r", encoding="utf-8") as f:
    with open(f"chatgpt_api调用/from/corpus_{file_index}.jsonl", "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            # if i > 15000:
            #     continue

            line = json.loads(line.strip())
            q = line["dialogue"][0][0]
            # print(q)

            if random.uniform(0, 1) > 0.1:
                continue

            t0 = time.time()
            try:
                print("query: ", q)
                response = decoder.decode(
                    q.strip(),  max_length=512
                )

                print("response: ", response)

            except Exception as e:
                print(e)
                response = None

            t1 = time.time()
            print("time cost: ", t1 - t0)

            if response:
                f_out.write(
                    json.dumps(
                        {
                            "query": q,
                            "response": response
                        },
                        ensure_ascii=False,
                    ) + "\n",

                )


    '''
    nohup python3 -u chatgpt_api调用/39_问诊数据_chatgpt35回答.py 91 > 91_log.log &
    nohup python3 -u chatgpt_api调用/39_问诊数据_chatgpt35回答.py 92 > 92_log.log &
    
    
    
    '''