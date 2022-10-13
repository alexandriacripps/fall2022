score=0
answer=input("what color is the sky?")
if answer=="blue":
    score=score+1
    print("Yes!")
else:
    print("I was looking for blue")
answer=input("how old is the president?")
if answer=="79":
    print("good")
    score=score+1
else:
    print('nope')
answer=input("how many great lakes are there?")
if answer=="5":
    score=score+1
    print("oh, you are smart!")
else:
    print("nice try")
print("Your score is",score)