import random

def mill(file, num_questions=10):
    name = input("Enter your name: ")

    with open('questions.txt', 'r') as f:
        questions = f.readlines()

    ind = random.sample(range(len(questions)), num_questions)
    quests = [questions[i].strip() for i in ind]

    questions_dict = {}
    for question in quests:
        q, a = question.split("?")
        questions_dict[q] = a.split(",")

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
            print("Wrong. The correct answer was:", correct)

    print("You got %d/%d" % (count, len(questions_dict)))

    with open('top.txt', 'a') as top:
        top.write(f"{name}: {count}/{len(questions_dict)}\n")

mill('questions.txt')
