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
    f_out = open(f"corpus_{file_index}_hpc.jsonl", "a", encoding="utf-8", buffering=1)

    # with open(f"预训练数据/datasets/39_问诊数据/splits/corpus_{file_index}.jsonl", "r", encoding="utf-8") as f:
    with open(f"corpus_{file_index}.jsonl", "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            # if i > 15000:
            #     continue

            line = json.loads(line.strip())
            q = line["dialogue"][0][0]
            # print(q)

            if random.uniform(0, 1) > 0.2:
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
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py > 1_log.log &
    
    
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py > 3_log.log &
    
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py > 4_log.log &
    
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py > 5_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py > 6_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py > 7_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py > 8_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py > 9_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py > 10_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py > 11_log.log &
    
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 12 > 12_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 13 > 13_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 14 > 14_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 15 > 15_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 16 > 16_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 17 > 17_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 18 > 18_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 19 > 19_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 20 > 20_log.log &
    
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 51 > 51_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 52 > 52_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 53 > 53_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 54 > 54_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 55 > 55_log.log &
    
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 56 > 56_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 57 > 57_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 58 > 58_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 59 > 59_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 60 > 60_log.log &
    
    
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 61 > 61_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 62 > 62_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 63 > 63_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 64 > 64_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 65 > 65_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 66 > 66_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 67 > 67_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 68 > 68_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 69 > 69_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 70 > 70_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 71 > 71_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 72 > 72_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 73 > 73_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 74 > 74_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 75 > 75_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 76 > 76_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 77 > 77_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 78 > 78_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 79 > 79_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 80 > 80_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 81 > 81_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 82 > 82_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 83 > 83_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 84 > 84_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 85 > 85_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 86 > 86_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 87 > 87_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 88 > 88_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 89 > 89_log.log &
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 90 > 90_log.log &
    
    nohup python -u 预训练数据/chatgpt_api调用/39_问诊数据_chatgpt35回答.py 91 > 91_log.log &
    
    
    '''