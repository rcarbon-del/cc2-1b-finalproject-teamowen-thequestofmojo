import os

#Clear all output function
def flush():
    os.system('cls' if os.name == 'nt' else 'clear')

# Clear output function
def clearOutput(numberOfLines: int):
    cursorUpOne = '\x1b[1A'
    erase = '\x1b[2K'
    for _ in range(numberOfLines):
        print(cursorUpOne + erase, end='')
