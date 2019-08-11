import json
from pathlib import Path

with open("第十届粤港澳安全知识竞赛题库.txt", encoding='UTF-8') as f:
    lines = f.readlines()
    question_set = []
    for i in range(1, 751):
        d = {}
        d["question"] = lines[i*6]
        d["a"] = lines[i*6+1][3:]
        d["b"] = lines[i*6+2][3:]
        d["c"] = lines[i*6+3][3:]
        d["answer"] = lines[i*6+4][-2]
        question_set.append(d)

Path("第十届粤港澳安全知识竞赛题库.json").write_text(
    json.dumps(question_set))
