import random
import json
from pathlib import Path

data = json.loads(Path("第十届粤港澳安全知识竞赛题库.json").read_text())


class Question:
    def __init__(self, data):
        self.user_question = ""
        self.options = []
        self.option_group = []
        self.answer = ""
        self.gather(data)
        self.generate()

    def gather(self, data):
        random_seed = random.randint(1, 750)
        self.user_question = data[random_seed]["question"]
        for i in ("a", "b", "c"):
            self.options.append(data[random_seed][i])
        self.answer = data[random_seed]["answer"]

    def generate(self):
        temp = 0
        if self.answer == 'a':
            temp = 0
        elif self.answer == 'b':
            temp = 1
        elif self.answer == 'c':
            temp = 2
        else:
            temp = 0
        for i in range(3):
            if i == temp:
                self.option_group.append((self.options[i], 1))
            else:
                self.option_group.append((self.options[i], 0))

        random.shuffle(self.option_group)


user = True
while user:
    question_post = Question(data)

    print(question_post.user_question)
    print(f"a.{question_post.option_group[0][0]}")
    print(f"b.{question_post.option_group[1][0]}")
    print(f"c.{question_post.option_group[2][0]}")

    user_answer = input("Please input your answer : ")
    user_temp = 0
    if user_answer.lower() == 'a':
        user_temp = question_post.option_group[0][1]
    elif user_answer.lower() == 'b':
        user_temp = question_post.option_group[1][1]
    elif user_answer.lower() == 'c':
        user_temp = question_post.option_group[2][1]
    else:
        print("NOOOO, that's an invalid input!!")
        break

    if user_temp == 1:
        print("You've got the right answer ♪(＾∀＾●)ﾉ")
    else:
        print("Sorry, you've got it wrong (づ╥﹏╥)づ")

    run_again = input("Do you wish to continue? 'y'for yes and 'n' for no : ")
    if run_again.lower() == "y":
        user = True
    elif run_again.lower() == "n":
        user = False
    else:
        print("NOOOO, that's an invalid input!!")
        break
