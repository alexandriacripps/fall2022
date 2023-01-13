import random

dice = (
    ("Q", "W", "E", "R", "T"),
    ("Y", "U", "I", "O", "P"),
    ("A", "S", "D", "F", "G"),
    ("H", "I", "J", "K", "L"),
    ("Z", "X", "C", "V", "B"),
    ("N", "M", "Q", "W", "E"),
    ("R", "T", "Y", "U", "I"),
    ("O", "P", "A", "S", "D"),
    ("F", "G", "H", "J", "K"),
    ("L", "Z", "X", "C", "V"),
    ("B", "N", "M", "A", "B"),
    ("O", "P", "M", "L", "R"),
    ("F", "T", "N", "J", "Y"),
    ("G", "E", "A", "D", "W"),
    ("K", "J", "W", "U", "P"),
    ("Z", "C", "I", "P", "V")
)

def rollDice():
    roll = list(dice)
    random.shuffle(roll)
    for die in roll:
        yield random.choice(die)

board = []
roll = rollDice()
for row in range(0,4):
    newRow = []
    for col in range(0,4):
        newRow.append(next(roll))
    board.append(newRow)

print(board)