import os
import sys
import time

from utils import clearOutput, flush

#Welcome screen function
def welcomeScreen():
    flush()
    print()
    print("Welcome to the Quest of Mojo!")
    time.sleep(1)
    print()
    print("1. Start")
    print("2. Credits")
    print("3. Quit")
    print()
    titleChoice = input("> ")
    if titleChoice == "1":
        flush()
    elif titleChoice == "2":
        flush()
        print("""The Quest of Mojo was created by:
        
    Bulatao, Chris Owyn
    Carbonel, Radge Daryll
    Carbonell, Jennylyn
    Cero, Wyatt
              
For completion of the requirements for the course,
Introduction to Computer Programming | CITCS 1B,
taught by Sir Jerry Junior Pacalso.""")
        print()
        end = input("Press enter to return...")
        welcomeScreen()

    elif titleChoice == "3":
        quit()
    else:
        print("Invalid choice.")
        time.sleep(1)
        welcomeScreen()

#Death screen function
def deathScreen():
    print("You died!")
    print()
    print("Game over!")
    print()
    print("1. Restart")
    print("2. Quit")
    print()
    deathChoice = input("> ")
    if deathChoice == "1":
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    elif deathChoice == "2":
        quit()
    else:
        clearOutput(8)
        deathScreen()
