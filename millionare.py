"""
This file is for millionare game
Creted by: Arman Hovhannisyan
Date: 29 May
"""
import random

def get_content(fname):
    """
    Function: get_content
    Brief: The function returns the whole content of the file
    Params: fname: The name of input file
    Return: returns the content of the file as a list
    """
    try:
        with open(fname) as f:
            return f.readlines()
    except FileNotFoundError:
        print("No such file. Please provide an existing one")
    return []

def select_questions(questions, num_questions):
    """
    Function: select_questions
    Brief: selects random questions from a list of questions
    Params: questions: A list containing the questions 
            num_questions: The number of questions
    Return: A list of selected questions
    """
    ind = random.sample(range(len(questions)), num_questions)
    quest = [questions[i].strip() for i in ind]
    return quest

def define_questions(quest):
    """
    Function: define_questions
    Brief: Parses questions and answers from a list of questions
    Params: quest: A list of questions
    Return: A dictionary where keys are questions and values are answers
    """
    questions_dict = {}
    for question in quest:
        q, a = question.split("?")
        questions_dict[q] = a.split(",")
    return questions_dict

def ask_questions(questions_dict):
    """
    Function: ask_questions
    Brief: Asks questions and checks the answers
    Params: questions_dict: A dictionary of question and answers
    Return: The count of correct answers
    """
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

def player_dict(p_dict):
    """
    Function: player_dict
    Brief: Creates a dictionary of player name and score
    Params: p_dict: A list containing player's name and score
    Return: A dictionary with name and score
    """
    tmp = {}
    tmp["name"] = p_dict[0]
    tmp["score"] = p_dict[1]
    return tmp

def players_list(content):
    """
    Function: players_list
    Brief: Creates a list of dictionaries
    Params: content: A list containing lines from a file
    Return: A list of player dictionaries sorted by score
    """
    players = []
    for line in content:
        player = line.strip().split()
        if len(player) >= 2:
            players.append(player_dict(player))
    players.sort(key=lambda x: int(x["score"].split("/")[0]), reverse=True)
    return players

def write_into_file(fname, players):
    """
    Function: write_into_file
    Brief: Writes player data into a file
    Params: fname: The name of the output file
            players: A list of player dictionaries.
    """
    players.sort(key=lambda x: int(x["score"].split("/")[0]), reverse=True)
    with open(fname, "w") as fw:
        for player in players:
            data = list(player.values())
            line = " ".join([str(el) for el in data])
            fw.write(line + "\n")

def player_name():
    """
    Function: player_name
    Brief: Asks the player for their name
    Return: Returns player name.
    """
    valid_name = False
    while not valid_name:
        name = input("Enter your name: ")
        if name.isalpha():
            valid_name = True 
        else:
            print("Enter your real name: ")
    return name

def main():
    """
    Function: main
    Brief: Entery point
    """
    fname = "questions.txt"
    num_questions = 10
    name = player_name()
    questions = get_content(fname)
    quest = select_questions(questions, num_questions)
    questions_dict = define_questions(quest)
    score = ask_questions(questions_dict)
    content = get_content("top.txt")
    p_list = players_list(content)
    p_list.append({"name": name, "score": f"{score}/{len(questions_dict)}"})
    write_into_file("top.txt", p_list)

if __name__ == "__main__":
    main()

