from Question import Question
question_prompts = [
    "What is encapsulation in object-oriented programming?\n(a) Bundling data and methods into a single unit\n(b) Creating instances of classes\n(c) Defining class inheritance\n\n",
    "What is inheritance in OOP?\n(a) Adding new features to an existing class\n(b) Organizing code into functions\n(c) Creating objects from classes\n\n",
    "How does polymorphism manifest in object-oriented programming?\n(a) Using descriptive variable names\n(b) Writing modular code\n(c) Allowing objects of different types to be treated as objects of a common type\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got "+ str(score)+ "/"+ str(len(questions))+ " correct")

run_test(questions)
