import os
import shutil
import time

from datasets import load_dataset

import sys
sys.path.append("./")

count = 0
while True:

    try:
        cache_dir = "预训练数据/chatgpt_api调用/cache"
        os.makedirs(cache_dir, exist_ok=True)

        dataset = load_dataset("michaelwzhu/ChatMed-Datasets", cache_dir=cache_dir + f"/cache_{count}/")
        # shutil.rmtree(cache_dir)
    except Exception as e:
        print(e)

    count += 1

    if count > 1000:
        break

    time.sleep(2.0)

    # nohup python 预训练数据/chatgpt_api调用/download_dataset.py > data_download_1.log &
