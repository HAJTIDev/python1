from json import load

correct_answers=0
with open("quizjson.json",encoding="UTF-8") as question_file:
    questions=load(question_file)
    #print(questions)

    for question in questions:
        print(question['question'])
        for index,answer in enumerate (question['answers']):
            print(index,answer['text'])
        user_answer=int(input("podaj odpowiedź: "))
        try:
            is_correct_answer=question['answers'][user_answer]['correct']
            if is_correct_answer:
                correct_answers+=1
        except IndexError:
            print('-'*20)
        print('\n')
    print("poprawnych odpowiedzi: ",correct_answers)