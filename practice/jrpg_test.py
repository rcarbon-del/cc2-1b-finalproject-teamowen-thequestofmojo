import random
import time

# Clear output
def clearOutput(num_lines: int):
    cursorUpOne = '\x1b[1A'
    erase = '\x1b[2K'
    for _ in range(num_lines):
        print(cursorUpOne + erase, end='')

#Welcome screen
print()
print()
print("Welcome to the Quest of Mojo!")
print()
print()
time.sleep(3)
clearOutput(3)

print("You are a young adventurer who lives alone.")
time.sleep(5)
clearOutput(1)
print("As you open your eyes, the light of day shines through your window.")
time.sleep(5)
clearOutput(1)
print("You suddenly hear someone speaking to you.")
print()
time.sleep(1.5)
user = input('"Young one, what is your name?" ')