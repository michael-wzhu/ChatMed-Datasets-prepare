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
openai.api_key = "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"

decoder = Decoder()


if __name__ == "__main__":

    file_index = sys.argv[1]


    list_samples = []
    # f_out = open(f"预训练数据/chatgpt_api调用/splits/corpus_{file_index}_hpc.jsonl", "a", encoding="utf-8", buffering=1)
    f_out = open(f"self_instruct/tcm_answers_{file_index}.json", "a", encoding="utf-8", buffering=1)

    # with open(f"预训练数据/datasets/39_问诊数据/splits/corpus_{file_index}.jsonl", "r", encoding="utf-8") as f:
    with open(f"self_instruct/tcm_queries_{file_index}.json", "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            # if i > 15000:
            #     continue

            line = json.loads(line.strip())
            q = line["query"]

            t0 = time.time()
            try:
                print("query: ", q)
                response = decoder.decode(
                    q.strip(),  max_length=1024
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
    nohup python3 -u chatgpt_api调用/tcm_chatgpt35_answers.py 1 > tcm_1_log.log &
    
    
    
    '''
