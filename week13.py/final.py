quiz = [
    {
        "question": "What is Python?",
        "choices": [
            "a programming language",
            "a computer",
            "a website",
        ],
        "answer": "a programming language"
    },
    {
        "question": "What is the name of the version control system we use?",
        "choices": [
            "VS Code",
            "Python",
            "Git"
        ],
        "answer": "Git"
    },
    {
        "question": "What is a repository?",
        "choices": [
            "a file in Python",
            "place where files are stored",
            "a folder"
        ],
        "answer": "place where files are stored"
    },
    {
        "question": "What does Python use to group lines?",
        "choices": [
            "indentations",
            "outputs",
            "if statements"
        ],
        "answer": "indentations"
    },
    {
        "question": "What is a module?",
        "choices": [
            "a group of files",
            "random outputs",
            "a bundle of functions"
        ],
        "answer": "a bundle of functions"
    },
    {
        "question": "Which statement is true?",
        "choices": [
            "lists have multiple items, a tuple does not",
            "tuples can not be unpacked into other other variables",
            "ists can be changed after it's created"
        ],
        "answer": "lists can be changed after it's created"
    },
    {
        "question": "What is the symbol for iterate in Python",
        "choices": [
            "i",
            "t1",
            "#"
        ],
        "answer": "i"
    },
    {
        "question": "What does I/O stand for?",
        "choices": [
            "inside/outside",
            "input/output",
            "in/out"
        ],
        "answer": "input/output"
    },
    {
        "question": "What do curly brackets indicate?",
        "choices": [
            "a set",
            "a tuple",
            "a list"
        ],
        "answer": "a set"
    },
    {
        "question": "True or False: Sets have no order",
        "choices": [
            "True",
            "False"
        ],
        "answer": "True"
    },
    {
        "question": "What is a table of key and value pairs?",
        "choices": [
            "sorting",
            "a loop",
            "a dictionary"
        ],
        "answer": "a dictionary"
    },
    {
        "question": "What does 'del' do in Python?",
        "choices": [
            "deletes a key/pair",
            "deletes a file",
            "delays a loop"
        ],
        "answer": "deletes a key/pair"
    }
]

problemNumber = 0
correct = 0
for problem in quiz:
    problemNumber+= 1
    print(f"Question {problemNumber}: {problem['question']}")

    for choice in problem['choices']:
        print(f" {choice}")

    guess = input("Your guess: ")
    if guess == problem['answer']:
        correct += 1
        print(f"You are correct!")
    else: 
        print(f"Incorrect.")

    print()
    
print(f"Correct: {correct} of {problemNumber} ({correct * 100 / problemNumber}%)")