import random
random_number = random.randint(1, 100)
guess = int(input("Input: "))

while guess != random_number:
    if guess > random_number:
        print("Too high!")
        guess = int(input("Enter a number again: "))
    elif guess < random_number:
        print("Too low!")
        guess = int(input("Enter a number again: "))
    else:
        break
print("Correct!")