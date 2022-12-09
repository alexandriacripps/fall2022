quiz=[
    {
        "question": "What day is Christmas on?",
        "choices": [ 
            "February 3rd",
            "December 25th",
            "October 16th",
            "April 22nd"
        ],
        "answer": "December 25th"
    },
    {
        "question": "What is the capital of Spain?",
        "choices": [
            "Barcelona",
            "Granada",
            "Ibiza",
            "Madrid"
        ],
        "answer": "Madrid"
    },
    {
        "question": "What is the world's largest ocean?",
        "choices": [
            "Pacific",
            "Atlantic",
            "Indian",
            "Arctic"
        ],
        "answer": "Pacific"
    },
    {
        "question": "What planet is closest to the sun?",
        "choices": [
            "Mars",
            "Saturn",
            "Jupiter",
            "Mercury"
        ],
        "answer": "Mercury"
    },
    {
    "question": "How many weeks are in a year?",
    "choices": [
        "109",
        "45",
        "52",
        "87"
    ],
    "answer": "52"
    }
]

import random
random.shuffle(quiz)

problemNumber=0
correct=0
for problem in quiz:
    problemNumber += 1
    print(f"Question {problemNumber}: {problem['question']}")

    for choices in problem['choices']:
        print(f" {choices}")

    guess=input("Your guess: ")
    if guess==problem['answer']:
        correct +=1
        print(f"You are correct!")
    else:
        print(f"Incorrect.")

    print( ) 

print(f"Correct: {correct} of {problemNumber} ({correct * 100 / problemNumber}%)")