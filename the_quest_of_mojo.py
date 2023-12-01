import random
import time

# Imported functions
from utils import clearOutput, flush
from screens import welcomeScreen, userInput
from fights import randomEnemy, bossFight, enemyFight, playMaze

# Variables

kingdomNames = ["Nexus", "Arkdemn"]
knights = ["Ether", "Sekai"]
demons = ["Valentina", "Riyo"]
demonPrince = "Carnivale"
magicalStone = "Citrine"

# Main game
playMaze()
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
from screens import user
clearOutput(4)

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