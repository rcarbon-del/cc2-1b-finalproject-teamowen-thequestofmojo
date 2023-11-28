import random
import time

# Imported functions
from utils import clearOutput, flush
from screens import welcomeScreen, deathScreen
from mazes import maze1, maze2, maze3, maze4, maze5


# Variables
user = ''
kingdomNames = ["Nexus", "Arkdemn"]
knights = ["Ether", "Sekai"]
demons = ["Valentina", "Riyo"]
demonPrince = "Carnivale"
magicalStone = "Citrine"
health = random.randint(1000, 1500)
attack = random.randint(10, 30)
defense = random.randint(1, 25)
healCounter = random.randint(5, 8)
randomEnemyCounter = 0

# Functions
#User input
def userInput():
    global user
    user = input("> ").capitalize()
    if user.isalnum() == True:
        clearOutput(1)
    else:
        print("Invalid input.")
        time.sleep(1)
        clearOutput(2)
        userInput()

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
                    if dmg >= attack+90:
                        print("Critical hit!")
                        criticalHit += 1
                    print("You dealt", dmg, "damage to the enemy!")
                    print("The enemy has", enemyHealth, "health left!")
                    print()
                    break
                else:
                    if dmg >= attack+90:
                        print("Critical hit!")
                    print("You dealt", dmg, "damage to the enemy!")
                    print("The enemy has", enemyHealth, "health left!")
                    print()
                time.sleep(0.5)

                enemydmg = random.randint(100, 175)
                if defense >= 100:
                    enemydmg -= defense-40
                else:
                    enemydmg -= defense
                health -= enemydmg
                if enemyHealth >= 0:
                    if health <= 0:
                        health = 0
                        print("The enemy dealt", enemydmg, "damage to you!")
                        if enemydmg >= 150:
                            print("The attack was super effective!")
                        print("You have", health, "health left!")
                        print()
                        break
                    else:
                        print("The enemy dealt", enemydmg, "damage to you!")
                        if enemydmg >= 150:
                            print("The attack was super effective!")
                        print("You have", health, "health left!")
                        print()
                time.sleep(0.5)
                end = input("Press enter to continue...")
                time.sleep(0.1)
                clearOutput(16)
                if dmg >= attack+90:
                    clearOutput(1)
                if enemydmg >= 150:
                    clearOutput(1)
            
            elif choice == "2":
                if healCounter > 0:
                    heal = random.randint(75, 100)
                    health += heal
                    if health >= 1500:
                        health = 1500
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
        deathScreen()
    elif enemyHealth == 0:
        print("You won!")
        additionalAttack = random.randint(1, 15)
        attack += additionalAttack
        additionalDefense = random.randint(1, 10)
        defense += additionalDefense
        if defense >= 150:
            defense = 150
            additionalDefense = 0
        additionalHealth = random.randint(50, 100)
        health += additionalHealth
        if health >= 1000:
            health = 1000
            additionalHealth = 0
        additionalHealCounter = random.randint(1, 2)
        healCounter += additionalHealCounter
        if healCounter >= 10:
            healCounter = 10
            additionalHealCounter = 0
        print()
        print(f"You have gained {additionalAttack} attack, {additionalDefense} defense, {additionalHealth} health, and {additionalHealCounter} heal(s)!")
    print()
    end = input("Press enter to exit...")

#Boss fight function
def bossFight(bossStrength: int):

    bossHealth = random.randint(bossStrength*750, bossStrength*1000)
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
                dmg = random.randint(attack+20, attack+200)
                bossHealth -= dmg
                if bossHealth <= 0:
                    bossHealth = 0
                    if dmg >= attack+150:
                        print("Critical hit!")
                        criticalHit += 1
                    print("You dealt", dmg, "damage to the boss!")
                    print("The boss has", bossHealth, "health left!")
                    print()
                    break
                else:
                    if dmg >= attack+150:
                        print("Critical hit!")
                    print("You dealt", dmg, "damage to the boss!")
                    print("The boss has", bossHealth, "health left!")
                    print()
                time.sleep(0.5)

                bossdmg = random.randint(bossStrength*75, bossStrength*110)
                if defense >= 150:
                    bossdmg -= defense-50
                else:
                    bossdmg -= defense
                health -= bossdmg
                if bossHealth >= 0:
                    if health <= 0:
                        health = 0
                        print("The boss dealt", bossdmg, "damage to you!")
                        if bossdmg >= bossStrength*80:
                            print("The attack was super effective!")
                        print("You have", health, "health left!")
                        print()
                        break
                    else:
                        print("The boss dealt", bossdmg, "damage to you!")
                        if bossdmg >= bossStrength*80:
                            print("The attack was super effective!")
                        print("You have", health, "health left!")
                        print()
                time.sleep(0.5)
                end = input("Press enter to continue...")
                time.sleep(0.1)
                clearOutput(15)
                if dmg >= attack+150:
                    clearOutput(1)
                if bossdmg >= bossStrength*80:
                    clearOutput(1)
            
            elif choice == "2":
                if healCounter > 0:
                    heal = random.randint(125, 200)
                    health += heal
                    if health >= 2000:
                        health = 2000
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
        deathScreen()
    elif bossHealth == 0:
        print("You won!")
        if bossStrength == 2:
            additionalAttack = random.randint(10, 25)
            attack += additionalAttack
            additionalDefense = random.randint(5, 15)
            defense += additionalDefense
            additionalHealth = random.randint(100, 150)
            health += additionalHealth
            additionalHealCounter = random.randint(2, 4)
            healCounter += additionalHealCounter
            if healCounter >= 10:
                healCounter = 10
                additionalHealCounter = 0
            print()
            print(f"You have gained {additionalAttack} attack, {additionalDefense} defense, {additionalHealth} health, and {additionalHealCounter} heal(s)!")
    print()
    end = input("Press enter to exit...")
    flush()
    print("The Quest of Mojo")
    print()
    
#Random enemy function
def randomEnemy():
    global randomEnemyCounter
    randomEnemyCounter += random.randint(1, 15)
    if randomEnemyCounter >= 26:
        enemy = random.randint(1, 3)
        if enemy == 1:
            print("You encountered a demon!")
        elif enemy == 2:
            print("You encountered a human trafficker!")
        elif enemy == 3:
            print("You encountered a monster!")
        print()
        enemyFight()
        flush()
        randomEnemyCounter = random.randint(1, 10)
        print("The Quest of Mojo")
        print()

# Maze and character movement
def playMaze():
    WALL = '#'
    EMPTY = ' '
    START = 'S'
    EXIT = 'E'
    PLAYER = '@'
    BLOCK = chr(9608)

    def displayMaze(maze):
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if (x, y) == (playerx, playery):
                    print(PLAYER, end='')
                elif (x, y) == (exitx, exity):
                    print('X', end='')
                elif maze[(x, y)] == WALL:
                    print(BLOCK, end='')
                else:
                    print(maze[(x, y)], end='')
            print()

    mazeFile = random.choice([maze1, maze2, maze3, maze4, maze5])
    maze = {}
    lines = mazeFile
    playerx = None
    playery = None
    exitx = None
    exity = None
    y = 0
    play = True
    for line in lines:
        WIDTH = len(line.rstrip())
        for x, character in enumerate(line.rstrip()):
            assert character in (WALL, EMPTY, START, EXIT), 'Invalid character at column {}, line {}'.format(x + 1, y + 1)
            if character in (WALL, EMPTY):
                maze[(x, y)] = character
            elif character == START:
                playerx, playery = x, y
                maze[(x, y)] = EMPTY
            elif character == EXIT:
                exitx, exity = x, y
                maze[(x, y)] = EMPTY
        y += 1
    HEIGHT = y

    assert playerx != None and playery != None, 'No start in maze file.'
    assert exitx != None and exity != None, 'No exit in maze file.'

    while play == True: 
        print("The Quest of Mojo")
        print()
        displayMaze(maze)
        print()
        print("Get to the X to get to Carnivale's Throne.")
        print()
        while True:
            print('                  W')
            print('Enter direction: ASD')
            move = input('> ').upper()

            if move not in ['W', 'A', 'S', 'D']:
                print('Invalid direction. Enter one of W, A, S, or D.')
                clearOutput(4)
                continue

            if move == 'W' and maze[(playerx, playery - 1)] == EMPTY:
                break
            elif move == 'S' and maze[(playerx, playery + 1)] == EMPTY:
                break
            elif move == 'A' and maze[(playerx - 1, playery)] == EMPTY:
                break
            elif move == 'D' and maze[(playerx + 1, playery)] == EMPTY:
                break

            print('You cannot move in that direction.')
            clearOutput(4)
        if move == 'W':
            while True:
                playery -= 1
                if (playerx, playery) == (exitx, exity):
                    break
                if maze[(playerx, playery - 1)] == WALL:
                    break  
                if (maze[(playerx - 1, playery)] == EMPTY
                    or maze[(playerx + 1, playery)] == EMPTY):
                    break
            randomEnemy()  
            flush()
        elif move == 'S':
            while True:
                playery += 1
                if (playerx, playery) == (exitx, exity):
                    break
                if maze[(playerx, playery + 1)] == WALL:
                    break  
                if (maze[(playerx - 1, playery)] == EMPTY
                    or maze[(playerx + 1, playery)] == EMPTY):
                    break  
            randomEnemy()
            flush()
        elif move == 'A':
            while True:
                playerx -= 1
                if (playerx, playery) == (exitx, exity):
                    break
                if maze[(playerx - 1, playery)] == WALL:
                    break 
                if (maze[(playerx, playery - 1)] == EMPTY
                    or maze[(playerx, playery + 1)] == EMPTY):
                    break 
            randomEnemy()
            flush()
        elif move == 'D':
            while True:
                playerx += 1
                if (playerx, playery) == (exitx, exity):
                    break
                if maze[(playerx + 1, playery)] == WALL:
                    break 
                if (maze[(playerx, playery - 1)] == EMPTY
                    or maze[(playerx, playery + 1)] == EMPTY):
                    break
            randomEnemy()
            flush()

        if (playerx, playery) == (exitx, exity):
            flush()
            print("The Quest of Mojo")
            print()
            play = False

# Main game
welcomeScreen()
print("The Quest of Mojo")
print()
time.sleep(1)

#Character creation
print("As you open your eyes, the light of day shines through your window.")
time.sleep(3)
clearOutput(1)

print("You wake up in a small room.")
time.sleep(3)
clearOutput(1)

print("Suddenly, you hear someone speaking to you.")
time.sleep(1.5)
print()
print('"Young one, what is your name?" ')
print()
userInput()

print("You reply, " + user + ".")
time.sleep(3)
clearOutput(1)

print("The voice replies,")
time.sleep(1.5)
print()
print('"Ah! ' + user + ', I see you that are awake."')
time.sleep(3)
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
print(f""""{kingdomNames[0]}: The Kingdom of Peace"
      
        The blessed kingdom brought by the gods. Even when there is  
    war, the kingdom was at peace. The gods have given the people 
    of {kingdomNames[0]} the power of magic. The people of {kingdomNames[0]} used magic to 
    help the world. The world was at peace for a thousand years. But, 
    the gods have left the world of {kingdomNames[0]}. However, the gods left a 
    gift for the people of {kingdomNames[0]}. The gift was the magical stone, 
    {magicalStone}. {magicalStone} is the most powerful and dangerous 
    object in the world. It gave the people the ability to use 
    magic without the help of gods. It can bring disaster once it is abused and explodes.""")
time.sleep(5)
print()
end = input("Press enter to flip to the next page...")
clearOutput(19)

print("You flip the page, it says,")
time.sleep(1.5)
print()
print(f""""{kingdomNames[0]} against other kingdoms"
      
        The kingdom of {kingdomNames[0]} was at peace for a thousand years. Until
    the day came when the gods left the kingdom of {kingdomNames[0]}. The people
    of other kingdoms became greedy. They wanted the to get the stone.
    Other kingdoms started to wage war with {kingdomNames[0]} for the magical 
    stone, {magicalStone}. The people of {kingdomNames[0]} started to kill each other. 
    For the past 100 years, the magical stone was able to be kept
    safe by the people of {kingdomNames[0]}. The people of {kingdomNames[0]} were the
    protectors of the magical stone.""")
time.sleep(5)
print()
end = input("Press enter to close the book...")
clearOutput(14)

print("You closed the book and put it back on the table.")
time.sleep(3)
clearOutput(1)

print("The voice says,")
time.sleep(1.5)
print()
print('"I see that you have read the book."')
time.sleep(3)
clearOutput(3)

print("You reply,")
time.sleep(1.5)
print()
print('"Yes, I have. So, what do I do now?"')
time.sleep(3)
clearOutput(3)

print("The voice replies,")
time.sleep(1.5)
print()
print(f'"You must go to the capital of {kingdomNames[0]} and defend the magical stone, {magicalStone}."')
time.sleep(3)
clearOutput(3)

print("You go outside and see a sword and a shield with a crest.")
time.sleep(2)
print()
print("You take the sword and shield.")
attack += 50
defense += 50
time.sleep(3)
clearOutput(3)
randomEnemy()
randomEnemy()

print(f"""As you wander, you find out that you were already in the capital of {kingdomNames[0]}. 
You also find out the news about {demonPrince}, the demon prince of power.""")
time.sleep(2)
print()
print(f"""      {demonPrince} is the demon prince of powers. He was extremely injured and lost 
    most of his powers during the previous fights of {kingdomNames[0]} against the demons of Arkdenm. 
    {demonPrince} believes he can save his life and bring back his powers with the help of the 
    magical stone. Out of loyalty and gratitude for keeping them when they were abandoned 
    since childhood, his two trustworthy demons, {demons[0]} and {demons[1]}, are able to risk 
    everything just to make him back again.""")
time.sleep(5)
print()
end = input("Press enter to keep walking...")
clearOutput(11)
randomEnemy()
randomEnemy()

print(f"You continue walking. You stumble upon two knights, {knights[0]} and {knights[1]}, and they seem to recognize you.")
time.sleep(2)
print()
print(f"{knights[0]} says,")
time.sleep(1.5)
print()
print(f'"Hey {user}, where are you going?"')
time.sleep(3)
clearOutput(5)

print("You reply,")
time.sleep(1.5)
print()
print('"Who are you?"')
time.sleep(3)
clearOutput(3)

print(f"{knights[1]} replies,")
time.sleep(1.5)
print()
print(f'"Ha ha ha, did you forget that we all are knights of the kingdom of {kingdomNames[0]}?"')
time.sleep(3)
clearOutput(3)

print("You reply awkwardly,")
time.sleep(1.5)
print()
print('"Oh, I forgot. Sorry about that."')
time.sleep(3)
clearOutput(3)

print(f"{knights[0]} says,")
time.sleep(1.5)
print()
print(f'"We need to go now. {demons[0]} and {demons[1]} are going to attack the capital of {kingdomNames[0]}."')
time.sleep(3)
clearOutput(3)
randomEnemy()


print("You and the two knights go to the headquaters of the Imperial Knights.")
time.sleep(2)
print()
print(f"{knights[0]} says,")
time.sleep(1.5)
print()
print(f'"We have to subdue {demons[0]} and {demons[1]}. I heard that they are on their way to the capital."')
time.sleep(3)
clearOutput(5)

print("You and the two knights go to the forest outside the capital.")
time.sleep(3)
clearOutput(1)
randomEnemy()
randomEnemy()
randomEnemy()

print(f"You and the two knights see {demons[0]} and {demons[1]}.")
time.sleep(2)
print()
print(f"{knights[0]} says,")
time.sleep(1.5)
print()
print('"ATTACK!"')
time.sleep(3)
print()
print(f"You and the two knights attack {demons[0]} first.")
print()
bossFight(2)
print(f"You and the two knights attack {demons[1]} next.")
print()
bossFight(2)
print(f"{demons[0]} and {demons[1]} retreated back to {kingdomNames[1]}.")
time.sleep(3)
clearOutput(1)

print(f"{knights[0]} says,")
time.sleep(1.5)
print()
print('"We have to go back to the capital."')
time.sleep(3)
clearOutput(3)

print("You and the two knights go back to the capital.")
time.sleep(3)
clearOutput(1)
randomEnemy()

print("You and the two knights go to the headquaters of the imperial knights.")
time.sleep(2)
print()
print(f"{knights[0]} says,")
time.sleep(1.5)
print()
print('"Their comrades have taken the magical stone."')
time.sleep(3)
clearOutput(5)

print(f"You and the two knights go to the kingdom of {kingdomNames[1]} to retrieve the stone.")
time.sleep(3)
clearOutput(1)
randomEnemy()
randomEnemy()
randomEnemy()
randomEnemy()
randomEnemy()
randomEnemy()
randomEnemy()
randomEnemy()

print("You and the two knights arrive at the 幻想の城, the Castle of Illusion.")
time.sleep(2)
print()
print(f"{knights[0]} says,")
time.sleep(1.5)
print()
print(f'''"Be careful, 幻想の城, the Castle of Illusion, is the home of the demon prince of power, {demonPrince}. It's interior has
a lot of traps and illusions. The interior of the castle changes everytime we enter it."''')
time.sleep(3)
flush()
playMaze()

print("You and the two knights arrive at the throne room.")
time.sleep(2)
clearOutput(1)

print(f"{knights[0]} says,")
time.sleep(1.5)
print()
print(f'"We have to defeat {demonPrince}."')
time.sleep(3)
clearOutput(3)

print("You and the two knights enter the throne room.")
time.sleep(2)
print()
print(f"{demonPrince} says,")
time.sleep(1.5)
print()
print(f'"I see that you have come to save the magical stone, {magicalStone}."')
time.sleep(3)
clearOutput(3)

print(f"{knights[0]} says,")
time.sleep(1.5)
print()
print(f'"We have come to defeat you {demonPrince}!"')
time.sleep(3)
clearOutput(3)

print(f"{demonPrince} says,")
time.sleep(1.5)
print()
print('"You fools, you cannot defeat me."')
time.sleep(3)
clearOutput(3)

print(f"{knights[0]} says,")
time.sleep(1.5)
print()
print(f'"We will see about that."')
time.sleep(3)
clearOutput(3)

print(f"{demonPrince} says,")
time.sleep(1.5)
print()
print('"You will regret this."')
time.sleep(3)
clearOutput(3)

print(f"{knights[0]} says,")
time.sleep(1.5)
print()
print(f'"Attack!"')
time.sleep(3)
clearOutput(3)

print(f"You and the two knights attack {demonPrince}.")
print()
bossFight(3)

print(f"{knights[0]} says,")
time.sleep(1.5)
print()
print('"We did it!"')
time.sleep(3)
clearOutput(3)

end = input("Press enter to exit the game...")
