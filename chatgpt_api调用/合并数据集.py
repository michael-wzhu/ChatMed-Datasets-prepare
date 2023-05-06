import json
import os
import random

from tqdm import tqdm



if __name__ =="__main__":

    version = "v0.3"

    # 合并数据集 并 给出数据集的统计
    list_samples = []

    folder = "chatgpt_api调用/splits"
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith("jsonl"):
                print(root, file)

                samps = []
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    for line in f:
                        samps.append(json.loads(line))
                print("original", file, len(samps))
                list_samples.extend(samps)

    random.shuffle(list_samples)
    with open(f"data/ChatMed_Consult-{version}.json", "w", encoding="utf-8") as f:
        for samp in list_samples:
            f.write(
                json.dumps(samp, ensure_ascii=False) + "\n"
            )

    num_lines_per_file = 10000
    with open(f"data/ChatMed_Consult-{version}.json", "r", encoding="utf-8") as input_file:
        line_num = 1
        file_num = 1
        output_file = open(
            f"data/ChatMed_Consult-{version}-{file_num}.jsonl",
            "w",
            encoding="utf-8"
        )

        for line in tqdm(input_file):
            output_file.write(line)
            line_num += 1
            if line_num > num_lines_per_file:
                output_file.close()
                file_num += 1
                line_num = 1
                output_file = open(f"data/ChatMed_Consult-{version}-{file_num}.jsonl", 'w',
                                   encoding='utf-8')

        output_file.close()
