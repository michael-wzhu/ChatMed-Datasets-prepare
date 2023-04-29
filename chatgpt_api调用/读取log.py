import json

if __name__ == "__main__":

    list_samples = []
    list_queries = []

    for i in range(31, 46):
        truncs = []
        line_tmp = ""
        with open(f"预训练数据/chatgpt_api调用/cache/{i}_log.log", "r", encoding="utf-8") as f:
            for line in f:
                # print(line)

                if line.startswith("query: ") or "Invalid response object from API" in line:
                    if len(line_tmp) > 0:
                        truncs.append(line_tmp)
                        line_tmp = ""
                        line_tmp += line
                        # .replace("query:  ", "").replace("response:  ", "").replace("time cost:  ", "")

                    else:
                        line_tmp = ""
                        line_tmp += line


                else:
                    line_tmp += line

            if len(line_tmp) > 0:
                truncs.append(line_tmp)

        # assert len(truncs) % 3 == 0
        # print(len(truncs) % 3)
        # for k in range(12):
        #     print(f"{k}-" * 50)
        #     print(truncs[k])
        #     print(f"{k}-" * 50)

        # print(truncs[-3])
        # print(truncs[-2])
        # print(truncs[-1])

        f_out = open(f"预训练数据/chatgpt_api调用/cache/corpus_{i}_hpc.jsonl", "w", encoding="utf-8", buffering=1)
        for j in range(len(truncs)):
            # print(j)

            # print(query)

            text_ = truncs[j]
            if "Invalid response object from API" in text_:
                continue

            assert "time cost:" in text_

            text_ = text_.split("time cost:")[0].strip()
            if not "query: " in text_:
                print("jnjnvojvn", text_)
            if "Invalid response " in text_:
                text_ = text_.split("Invalid response ")[0].strip()

            if not "query: " in text_:
                print("jnjnvojvn", text_)
            assert "query: " in text_

            if not "response: " in text_:
                print("ojvnjdfnvogb", text_)
            assert "response:" in text_

            query = text_.split("response:")[0].replace("query:", "").strip()
            response = text_.split("response:")[1].strip()
            assert "query: " not in query
            assert "response: " not in response

            # print(query)
            # print(response)

            if len(response) == 0:
                continue


            # if time not in

            f_out.write(
                json.dumps(
                    {
                        "query": query,
                        "response": response
                    },
                    ensure_ascii=False,
                ) + "\n",

            )
