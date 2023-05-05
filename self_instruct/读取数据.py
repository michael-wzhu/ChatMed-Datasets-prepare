import json
import re

if __name__ == "__main__":

    list_samples = []
    list_samples_1 = []
    set_queries = set()

    for i in range(1, 8):
        with open(f"self_instruct/file_{i}.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            # print(type(lines))
            lines = " ".join([w.strip() for w in lines])
            # print(type(lines))

            lines = lines.strip().replace("\n", "", 100000).replace("```", "", 100000)
            # print(lines[: 1000])

            while True:
                res = re.search(r"\{.*?\}", lines)

                if not res:
                    break

                span = res.span()
                samp = lines[span[0]: span[1]]
                if "代码" in samp or "函数" in samp or "程序" in samp:
                    lines = lines[: span[0]] + " " + lines[span[1]:]
                else:
                    # samp = "\'" + samp + "\'"
                    # print(samp)
                    samp = eval(samp)
                    # print(type(samp))

                    if len(samp) != 2:
                        # print(samp.keys())

                        if len(samp) == 3:
                            if "instruction" in samp and "input" not in samp:
                                instruction = samp["instruction"]
                                query = instruction
                                list_samples.append({
                                    "input": query
                                })
                        else:
                            list_samples_1.append(samp)
                    elif "input" not in samp or "output" not in samp:
                        list_samples_1.append(samp)

                    else:
                        list_samples.append(samp)

                    lines = lines[: span[0]] + " " +  lines[span[1]: ]

    # f_out = open("self_instruct/ChatMed-TCM-v0.1.json", "w", encoding="utf-8")
    f_out = open("self_instruct/tcm_queries_1.json", "w", encoding="utf-8")
    for samp in list_samples:
        if "output" not in samp:
            print(samp)

        f_out.write(
            json.dumps(
                {
                    "query": samp["input"],
                    # "response": samp["output"]
                },
                ensure_ascii=False,
            ) + "\n",

        )

    f_out = open("self_instruct/list_samples_1.json", "w", encoding="utf-8")
    for samp in list_samples_1:
        f_out.write(
            json.dumps(
                samp,
                ensure_ascii=False,
            ) + "\n",

        )


        #     for line in f:
        #         # print(line)
        #
        #         if line.startswith("query: ") or "Invalid response object from API" in line:
        #             if len(line_tmp) > 0:
        #                 truncs.append(line_tmp)
        #                 line_tmp = ""
        #                 line_tmp += line
        #                 # .replace("query:  ", "").replace("response:  ", "").replace("time cost:  ", "")
        #
        #             else:
        #                 line_tmp = ""
        #                 line_tmp += line
        #
        #
        #         else:
        #             line_tmp += line
        #
        #     if len(line_tmp) > 0:
        #         truncs.append(line_tmp)
        #
        # # assert len(truncs) % 3 == 0
        # # print(len(truncs) % 3)
        # # for k in range(12):
        # #     print(f"{k}-" * 50)
        # #     print(truncs[k])
        # #     print(f"{k}-" * 50)
        #
        # # print(truncs[-3])
        # # print(truncs[-2])
        # # print(truncs[-1])
        #
        # f_out = open(f"预训练数据/chatgpt_api调用/cache/corpus_{i}_hpc.jsonl", "w", encoding="utf-8", buffering=1)
        # for j in range(len(truncs)):
        #     # print(j)
        #
        #     # print(query)
        #
        #     text_ = truncs[j]
        #     if "Invalid response object from API" in text_:
        #         continue
        #
        #     assert "time cost:" in text_
        #
        #     text_ = text_.split("time cost:")[0].strip()
        #     if not "query: " in text_:
        #         print("jnjnvojvn", text_)
        #     if "Invalid response " in text_:
        #         text_ = text_.split("Invalid response ")[0].strip()
        #
        #     if not "query: " in text_:
        #         print("jnjnvojvn", text_)
        #     assert "query: " in text_
        #
        #     if not "response: " in text_:
        #         print("ojvnjdfnvogb", text_)
        #     assert "response:" in text_
        #
        #     query = text_.split("response:")[0].replace("query:", "").strip()
        #     response = text_.split("response:")[1].strip()
        #     assert "query: " not in query
        #     assert "response: " not in response
        #
        #     # print(query)
        #     # print(response)
        #
        #     if len(response) == 0:
        #         continue
        #
        #
        #     # if time not in
        #
        #     f_out.write(
        #         json.dumps(
        #             {
        #                 "query": query,
        #                 "response": response
        #             },
        #             ensure_ascii=False,
        #         ) + "\n",
        #
        #     )
