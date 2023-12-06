import random
import time

from utils import clearOutput, flush
from screens import deathScreen
from mazes import maze1, maze2, maze3, maze4, maze5, mainMapLook
from characterclasses import Enemy, Player

#Variables
user = ""
health = 0
attack = 0
defense = 0
healCounter = 0
randomEnemyCounter = 0
kingdomNames = ["Nexus", "Arkdemn"]
knights = ["Ether", "Sekai"]
demons = ["Valentina", "Riyo"]
demonPrince = "Carnivale"
magicalStone = "Citrine"

# Functions
#User input
def userInput():
    global user
    global health
    global attack
    global defense
    global healCounter
    user = input("> ").capitalize()
    if user.isalnum() == True:
        player = Player(user)
        health = player.health
        attack = player.attack
        defense = player.defense
        healCounter = player.healCounter
        clearOutput(1)
        return user, health, attack, defense, healCounter
    else:
        print("Invalid input.")
        time.sleep(1)
        clearOutput(2)
        userInput()


#Enemy fight function
def enemyFight(enemyName: str):
    enemyClass = Enemy(enemyName)
    enemyHealth = enemyClass.enemyHealth
    criticalHit = 0
    global user
    global health
    global attack
    global defense
    global healCounter


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

                enemydmg = enemyClass.enemydmg+random.randint(25, 105)
                if defense >= 100:
                    enemydmg -= defense-40
                else:
                    enemydmg -= defense
                if enemydmg <= 0:
                    enemydmg = 0
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
                healCounter -= 2
                if health <= 0:
                    health = 0
                if healCounter <= 0:
                    healCounter = 0
                if attack <= 0:
                    attack = 0
                if defense <= 0:
                    defense = 0
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
        if health >= 1500:
            health = 1500
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
    global attack
    global defense
    global healCounter

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

                bossdmg = random.randint(bossStrength*90, bossStrength*120)
                if defense >= 150:
                    bossdmg -= defense-50
                else:
                    bossdmg -= defense
                if bossdmg <= 0:
                    bossdmg = 0
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
            if health >= 1500:
                health = 1500
                additionalHealth = 0
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
    randomEnemyCounter += random.randint(1, 8)
    if randomEnemyCounter >= 30:
        flush()
        print("The Quest of Mojo")
        print()
        enemy = random.randint(1, 3)
        enemyName = ""
        if enemy == 1:
            enemyclass = Enemy("demon")
            print(f"You encountered a {enemyclass.name}!")
            enemyName = enemyclass.name
        elif enemy == 2:
            enemyclass = Enemy("human trafficker")
            print(f"You encountered a {enemyclass.name}!")
            enemyName = enemyclass.name
        elif enemy == 3:
            enemyclass = Enemy("monster")
            print(f"You encountered a {enemyclass.name}!")
            enemyName = enemyclass.name
        print()
        enemyFight(enemyName)
        flush()
        randomEnemyCounter = random.randint(1, 5)
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
            randomEnemy() 
            flush()

        if (playerx, playery) == (exitx, exity):
            flush()
            print("The Quest of Mojo")
            print()
            play = False

def mainMap():
    WALL = '#'
    EMPTY = ' '
    START = 'S'
    EXIT = 'E'
    CHECKPOINT1 = '1'
    CHECKPOINT2 = '2'
    CHECKPOINT3 = '3'
    CHECKPOINT4 = '4'
    CHECKPOINT5 = '5'
    CHECKPOINT6 = '6'
    PLAYER = '@'
    BLOCK = chr(9608)
    ENCOUNTER = '!'

    def displayMaze(maze):
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if (x, y) == (playerx, playery):
                    print(PLAYER, end='')
                elif (x, y) == (exitx, exity):
                    print('X', end='')
                elif (x, y) == (check1x, check1y):
                    print(ENCOUNTER, end='')
                elif (x, y) == (check2x, check2y):
                    print(ENCOUNTER, end='')
                elif (x, y) == (check3x, check3y):
                    print(ENCOUNTER, end='')
                elif (x, y) == (check4x, check4y):
                    print(ENCOUNTER, end='')
                elif (x, y) == (check5x, check5y):
                    print(ENCOUNTER, end='')
                elif (x, y) == (check6x, check6y):
                    print(ENCOUNTER, end='')
                elif maze[(x, y)] == WALL:
                    print(BLOCK, end='')
                else:
                    print(maze[(x, y)], end='')
            print()

    mazeFile = mainMapLook
    maze = {}
    lines = mazeFile
    playerx = None
    playery = None
    exitx = None
    exity = None
    check1x = None
    check1y = None
    check2x = None
    check2y = None
    check3x = None
    check3y = None
    check4x = None
    check4y = None
    check5x = None
    check5y = None
    check6x = None
    check6y = None
    y = 0
    play = True
    for line in lines:
        WIDTH = len(line.rstrip())
        for x, character in enumerate(line.rstrip()):
            assert character in (WALL, EMPTY, START, EXIT, CHECKPOINT1, CHECKPOINT2, CHECKPOINT3, CHECKPOINT4, CHECKPOINT5, CHECKPOINT6), 'Invalid character at column {}, line {}'.format(x + 1, y + 1)
            if character in (WALL, EMPTY):
                maze[(x, y)] = character
            elif character == START:
                playerx, playery = x, y
                maze[(x, y)] = EMPTY
            elif character == EXIT:
                exitx, exity = x, y
                maze[(x, y)] = EMPTY
            elif character == CHECKPOINT1:
                check1x, check1y = x, y
                maze[(x, y)] = EMPTY
            elif character == CHECKPOINT2:
                check2x, check2y = x, y
                maze[(x, y)] = EMPTY
            elif character == CHECKPOINT3:
                check3x, check3y = x, y
                maze[(x, y)] = EMPTY
            elif character == CHECKPOINT4:
                check4x, check4y = x, y
                maze[(x, y)] = EMPTY
            elif character == CHECKPOINT5:
                check5x, check5y = x, y
                maze[(x, y)] = EMPTY
            elif character == CHECKPOINT6:
                check6x, check6y = x, y
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
        print("You are outside. you may encounter enemies while roaming.")
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
            playery -= 1
            randomEnemy()  
            flush()
        elif move == 'S':
            playery += 1
            randomEnemy()
            flush()
        elif move == 'A':
            playerx -= 1
            randomEnemy()
            flush()
        elif move == 'D':
            playerx += 1
            randomEnemy()
            flush()

        if (playerx, playery) == (check1x, check1y):
            flush()
            print("The Quest of Mojo")
            print()
            print(f"""As you wander, you find out that you were already in the capital of {kingdomNames[0]}. 
You also find out the news about {demonPrince}, the demon prince of power.""")
            time.sleep(2)
            print()
            print(f"""          {demonPrince} is the demon prince of powers. He was extremely injured and lost 
    most of his powers during the previous fights of {kingdomNames[0]} against the demons of Arkdenm. 
    {demonPrince} believes he can save his life and bring back his powers with the help of the 
    magical stone. Out of loyalty and gratitude for keeping them when they were abandoned 
    since childhood, his two trustworthy demons, {demons[0]} and {demons[1]}, are able to risk 
    everything just to make him back again.""")
            time.sleep(5)
            print()
            end = input("Press enter to keep walking...")
            CHECKPOINT1 = ' '
            check1x = None
            check1y = None
            flush()
        if (playerx, playery) == (check2x, check2y):
            flush()
            print("The Quest of Mojo")
            print()
            print(f"You stumble upon two knights, {knights[0]} and {knights[1]}, and they seem to recognize you.")
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
            CHECKPOINT2 = ' '
            check2x = None
            check2y = None
            flush()
        if (playerx, playery) == (check3x, check3y):
            flush()
            print("The Quest of Mojo")
            print()
            print(f"You are now in the capital of {kingdomNames[0]}.")
            time.sleep(2)
            print()
            print(f"{knights[0]} says,")
            time.sleep(1.5)
            print()
            print(f'"We need to go to the imperial knights headquaters."')
            time.sleep(3)
            clearOutput(3)
            CHECKPOINT3 = ' '
            check3x = None
            check3y = None
            flush()
        if (playerx, playery) == (check4x, check4y):
            flush()
            print("The Quest of Mojo")
            print()
            print("You and the two knights get to the headquaters of the Imperial Knights.")
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
            CHECKPOINT4 = ' '
            check4x = None
            check4y = None
            flush()
        if (playerx, playery) == (check5x, check5y):
            flush()
            print("The Quest of Mojo")
            print()
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
            CHECKPOINT5 = ' '
            check5x = None
            check5y = None
            flush()
        if (playerx, playery) == (check6x, check6y):
            flush()
            print("The Quest of Mojo")
            print()
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
            CHECKPOINT6 = ' '
            check6x = None
            check6y = None
            flush()
        if (playerx, playery) == (exitx, exity):
            flush()
            print("The Quest of Mojo")
            print()
            play = False
