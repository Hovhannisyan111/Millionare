import random

def get_content(fname):
    with open(fname) as f:
        return f.readlines()

def select_questions(questions, num_questions):
    ind = random.sample(range(len(questions)), num_questions)
    quest = [questions[i].strip() for i in ind]
    return quest

def define_questions(quest):
    questions_dict = {}
    for question in quest:
        q, a = question.split("?")
        questions_dict[q] = a.split(",")
    return questions_dict

def ask_questions(questions_dict):
    count = 0
    for q, a in questions_dict.items():
        print(q + "?")
        correct = a[0]
        random.shuffle(a)
        for el in a:
            print(el)
        answer = input("Enter your answer: ")
        if correct.lower() == answer.lower():
            print("Correct")
            count += 1
        else:
            print("Wrong. The correct answer is:", correct)
    return count

def player_dict(ml):
    tmp = {}
    tmp["name"] = ml[0]
    tmp["score"] = ml[1]
    return tmp

def players_list(content):
    players = []
    for line in content:
        player = line.strip().split()
        if len(player) >= 2:
            players.append(player_dict(player))
    players.sort(key=lambda x: int(x["score"].split("/")[0]), reverse=True)
    return players

def write_into_file(fname, players):
    players.sort(key=lambda x: int(x["score"].split("/")[0]), reverse=True)
    with open(fname, "w") as fw:
        for player in players:
            data = list(player.values())
            line = " ".join([str(el) for el in data])
            fw.write(line + "\n")

def player_name():
    valid_name = False
    while not valid_name:
        name = input("Enter your name: ")
        if name.isalpha():
            valid_name = True 
        else:
            print("Enter your real name: ")
    return name

def mill(fname, num_questions=10):
    name = player_name()
    questions = get_content(fname)
    quest = select_questions(questions, num_questions)
    questions_dict = define_questions(quest)
    score = ask_questions(questions_dict)
    content = get_content("top.txt")
    p_list = players_list(content)
    p_list.append({"name": name, "score": f"{score}/{len(questions_dict)}"})
    write_into_file("top.txt", p_list)

mill("questions.txt")

