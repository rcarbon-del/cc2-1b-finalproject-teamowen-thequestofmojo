from logging import critical
import random
import time
import os
from turtle import clear

# Variables
kingdomNames = ["Nexus", "Arkdemn"]
knights = ["Ether", "Sekai"]
demons = ["Valentina", "Riyo"]
demonPrince = "Carnivale"
magicalStone = "Citrine"
health = random.randint(800, 1000)
attack = random.randint(1, 25)
defense = random.randint(1, 25)
healCounter = 10

# Functions
# Clear output function
def clearOutput(numberOfLines: int):
    cursorUpOne = '\x1b[1A'
    erase = '\x1b[2K'
    for _ in range(numberOfLines):
        print(cursorUpOne + erase, end='')

#Welcome screen function
def welcomeScreen():
    print()
    print("Welcome to the Quest of Mojo!")
    time.sleep(2)
    print()
    print(f"""The Quest of Mojo is a role-playing game (RPG) that takes place 
in a post-apocalyptic {kingdomNames[0]}, beginning in the year 1751.""")
    time.sleep(2)
    print()
    print("1. Start")
    print("2. Credits")
    print("3. Quit")
    print()
    titleChoice = input("> ")
    if titleChoice == "1":
        clearOutput(11)
    elif titleChoice == "2":
        clearOutput(11)
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
        clearOutput(12)
        welcomeScreen()

    elif titleChoice == "3":
        quit()
    else:
        print("Invalid choice.")
        time.sleep(1)
        clearOutput(11)
        welcomeScreen()

#Enemy fight function
def enemyFight():
    enemyHealth = random.randint(250, 500)
    criticalHit = 0
    global health
    global healCounter
    global attack
    global defense

    print("------------------------------------------------------------")
    print()
    while health > 0:
        if health >= 0:
            print(f"Attack: {attack} | Defense: {defense} | Health: {health} | Enemy Health: {enemyHealth}")
            print()
            print("What will you do?")
            print("1. Attack")
            print(f"2. Heal ({healCounter} left)")
            print("3. Run")
            print()
            choice = input("Enter choice: ")
            print()
            time.sleep(0.5)

            if choice == "1": 
                dmg = random.randint(attack, attack+125)
                enemyHealth -= dmg
                if enemyHealth <= 0:
                    enemyHealth = 0
                    if dmg >= 150:
                        print("Critical hit!")
                        criticalHit += 1
                    print("You dealt", dmg, "damage to the enemy!")
                    print("The enemy has", enemyHealth, "health left!")
                    print()
                    break
                else:
                    if dmg >= 150:
                        print("Critical hit!")
                    print("You dealt", dmg, "damage to the enemy!")
                    print("The enemy has", enemyHealth, "health left!")
                    print()
                time.sleep(0.5)

                enemydmg = random.randint(defense+20, 100)
                enemydmg -= defense
                health -= enemydmg
                if enemyHealth >= 0:
                    if health <= 0:
                        health = 0
                        print("The enemy dealt", enemydmg, "damage to you!")
                        if enemydmg >= 100:
                            print("The attack was super effective!")
                        print("You have", health, "health left!")
                        print()
                        break
                    else:
                        print("The enemy dealt", enemydmg, "damage to you!")
                        if enemydmg >= 100:
                            print("The attack was super effective!")
                        print("You have", health, "health left!")
                        print()
                time.sleep(0.5)
                end = input("Press enter to continue...")
                time.sleep(0.1)
                clearOutput(16)
                if dmg >= 175:
                    clearOutput(1)
                if enemydmg >= 75:
                    clearOutput(1)
            
            elif choice == "2":
                if healCounter > 0:
                    heal = random.randint(75, 125)
                    health += heal
                    if health >= 1000:
                        health = 1000
                        print("You healed", heal, "health!")
                        print("You have max left!")
                        print()
                    else:
                        print("You healed", heal, "health!")
                        print("You have", health, "health left!")
                        print()
                    healCounter -= 1
                    end = input("Press enter to continue...")     
                    time.sleep(0.1)
                    clearOutput(13)           
                else:
                    print("You have no more heals left!")
                    print()
                    end = input("Press enter to continue...")
                    time.sleep(0.1)
                    clearOutput(12)
                
            elif choice == "3":
                print("You ran away!")
                health -= 500
                attack -= 15
                defense -= 15
                break
            else:  
                clearOutput(9)

    if health == 0:
        print("You died!")
        print()
        print("Game over!")
        print()
        end = input("Press enter to exit...")
        quit()
    elif enemyHealth == 0:
        print("You won!")
    print()
    end = input("Press enter to exit...")
    clearOutput(14)
    if enemyHealth == 0:
        clearOutput(3)
        if criticalHit == 1:
            clearOutput(1)

#Boss fight function
def bossFight():

    bossHealth = random.randint(1500, 2000)
    criticalHit = 0
    global health
    global healCounter
    global attack
    global defense

    print("------------------------------------------------------------")
    print()
    while health > 0:
        if health >= 0:
            print(f"Attack: {attack} | Defense: {defense} | Health: {health} | Boss Health: {bossHealth}")
            print()
            print("What will you do?")
            print("1. Attack")
            print(f"2. Heal ({healCounter} left)")
            print()
            choice = input("Enter choice: ")
            print()
            time.sleep(0.5)

            if choice == "1": 
                dmg = random.randint(attack, attack+200)
                bossHealth -= dmg
                if bossHealth <= 0:
                    bossHealth = 0
                    if dmg >= 175:
                        print("Critical hit!")
                        criticalHit += 1
                    print("You dealt", dmg, "damage to the boss!")
                    print("The boss has", bossHealth, "health left!")
                    print()
                    break
                else:
                    if dmg >= 175:
                        print("Critical hit!")
                    print("You dealt", dmg, "damage to the boss!")
                    print("The boss has", bossHealth, "health left!")
                    print()
                time.sleep(0.5)

                bossdmg = random.randint(defense+20, 150)
                bossdmg -= defense
                health -= bossdmg
                if bossHealth >= 0:
                    if health <= 0:
                        health = 0
                        print("The boss dealt", bossdmg, "damage to you!")
                        if bossdmg >= 75:
                            print("The attack was super effective!")
                        print("You have", health, "health left!")
                        print()
                        break
                    else:
                        print("The boss dealt", bossdmg, "damage to you!")
                        if bossdmg >= 75:
                            print("The attack was super effective!")
                        print("You have", health, "health left!")
                        print()
                time.sleep(0.5)
                end = input("Press enter to continue...")
                time.sleep(0.1)
                clearOutput(15)
                if dmg >= 175:
                    clearOutput(1)
                if bossdmg >= 75:
                    clearOutput(1)
            
            elif choice == "2":
                if healCounter > 0:
                    heal = random.randint(75, 125)
                    health += heal
                    if health >= 1000:
                        health = 1000
                        print("You healed", heal, "health!")
                        print("You have max left!")
                        print()
                    else:
                        print("You healed", heal, "health!")
                        print("You have", health, "health left!")
                        print()
                    healCounter -= 1
                    end = input("Press enter to continue...")     
                    time.sleep(0.1)
                    clearOutput(12)           
                else:
                    print("You have no more heals left!")
                    print()
                    end = input("Press enter to continue...")
                    time.sleep(0.1)
                    clearOutput(11)
            else:  
                clearOutput(8)

    if health == 0:
        print("You died!")
        print()
        print("Game over!")
        print()
        end = input("Press enter to exit...")
        quit()
    elif bossHealth == 0:
        print("You won!")
    print()
    end = input("Press enter to exit...")
    clearOutput(16)
    if criticalHit == 1:
        clearOutput(1)

# Main game
welcomeScreen()
print("The Quest of Mojo")
print()
time.sleep(1)

#Character creation
print("As you open your eyes, the light of day shines through your window.")
time.sleep(5)
clearOutput(1)
time.sleep(3)

print("You wake up in a small room.")
time.sleep(5)
clearOutput(1)

print("Suddenly, you hear someone speaking to you.")
time.sleep(1.5)
print()
print('"Young one, what is your name?" ')
print()
user = input("> ")
clearOutput(5)

print("You reply, " + user + ".")
time.sleep(5)
clearOutput(1)

print("The voice replies,")
time.sleep(1.5)
print()
print('"Ah, ' + user + ', I see you that are awake."')
time.sleep(5)
clearOutput(3)

print("You look around the room and see a book.")
time.sleep(2)
print()
print("The book was written in Japanese. However, you are able to read it.")
time.sleep(2)
print()
print("The book says,")
time.sleep(1.5)
print()
print(f"""" {kingdomNames[0]}: The Kingdom of Peace"
        The blessed kingdom brought by the gods. Even when there is  
    war, the kingdom was at peace. The gods have given the people 
    of {kingdomNames[0]} the power of magic. The people of {kingdomNames[0]} used magic to 
    help the world. The world was at peace for a thousand years. But, 
    the gods have left the world of {kingdomNames[0]}. However, the gods left a 
    gift for the people of {kingdomNames[0]}. The gift was the magical stone, 
    {magicalStone}. {magicalStone} is the most powerful and dangerous 
    object in the world. It gave the people the ability to use 
    magic without the help of gods.""")
time.sleep(10)
print()
end = input("Press enter to flip to the next page...")
clearOutput(18)

print("You flip the page, it says,")
time.sleep(1.5)
print()
print(f"""" {kingdomNames[0]} against other kingdoms"
        The world of {kingdomNames[0]} was at peace for a thousand years. Until
    the day came when the gods left the kingdom of {kingdomNames[0]}. The people
    of other kingdoms became greedy. They wanted the to get the stone.
    Other kingdoms started to wage war with {kingdomNames[0]} for the magical 
    stone, {magicalStone}. The people of {kingdomNames[0]} started to kill each other. 
    For the past 100 years, the magical stone was able to be kept
    safe by the people of {kingdomNames[0]}. The people of {kingdomNames[0]} were the
    protectors of the magical stone.""")
time.sleep(10)
print()
end = input("Press enter to close the book...")
clearOutput(13)

print("You closed the book and put it back on the table.")
time.sleep(5)
clearOutput(1)

print("The voice says,")
time.sleep(1.5)
print()
print('"I see that you have read the book."')
time.sleep(5)
clearOutput(3)

print("You reply,")
time.sleep(1.5)
print()
print('"Yes, I have. So, what do I do now?"')
time.sleep(5)
clearOutput(3)

print("The voice replies,")
time.sleep(1.5)
print()
print(f'"You must go to the capital of {kingdomNames[0]} and defend the magical stone, {magicalStone}."')
time.sleep(5)
clearOutput(3)

print("You go outside and see a sword and a shield with a crest.")
time.sleep(2)
print()
print("You take the sword and shield.")
attack += 50
defense += 50
time.sleep(5)
clearOutput(3)

print(f"""  As you wander, you find out that you were already in the capital of {kingdomNames[0]}.
You also find out the news about Carnivale, the demon prince of power.""")
time.sleep(2)
print(f"""'Carnivale is the demon prince of powers. He was extremely injured and lost most of his 
powers during the previous fights of Nexus against the demons of Arkdenm. Carnivale believes he can 
save his life and bring back his powers with the help of the magical stone. Out of loyalty and 
gratitude for keeping them when they were abandoned since childhood, his two trustworthy demons, 
Valentina and Riyo, are able to risk everything just to make him back again.'""")
time.sleep(10)
print()
end = input("Press enter to keep walking...")
clearOutput(14)

print("You continue walking. You stumble upon two knights, Ether and Sekai, and they seem to recognize you.")
