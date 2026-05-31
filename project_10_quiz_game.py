print("***********************************************")
print("welcome to my quiz game")
question_bank=[{"text":"the ability of one class the acquire methods and attributes of another class______.",
                "answer":"A"},
                {"text":"which of the following is a type of inheritecne?",
                "answer":"D"},
                {"text":"what type of inheritence has multiple subclasses to a single superclass ?",
                "answer":"C"},
                {"text":"what is the depth of multilevel inheritence in python?",
                "answer":"C"},
                {"text":"what does MRO stands for?",
                "answer":"B"}
                ]
options=[["A.inheritence","B.abstraction","C.polymorphism","D.objects"],
         ["A.single","B.double","C.multiple","D.both A and C"],
         ["A.multiple inheritence","B.multilevel inheritence","C.hierarchial inheritence","D.hybrid inheritence"],
         ["A.two level","B.three level","C.any level","D.none of these"],
         ["A.method recursive object","B.method resolution order","C.main resolution object","D.main resolution order"]
         ]
score=0
def check_answer(guess,answer):
    if guess==answer:
        return True
    else:
        return False

for question_number in range(len(question_bank)):
    print("***********************************************************")
    print(question_bank[question_number]["text"])
    for i in options[question_number]:
        print(i)
    guess=input("enter your answer(A/B/C/D):").upper()  
    is_correct=check_answer(guess,question_bank[question_number]["answer"])  
    if is_correct:
        print("correct answer")
        score+=1
    else:
        print("incorrect answer")
        print(f"the current answer is {question_bank[question_number]["answer"]}") 
    print(f"your current score is {score}/{question_number+1}")       
print(f"you have given {score} correct answers")
print(f"your score is {(score)/(len(question_bank))*100}%")


                
                
                
                
                
                