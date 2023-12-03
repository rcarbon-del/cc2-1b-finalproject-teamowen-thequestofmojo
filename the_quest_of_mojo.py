import random
import time

# Imported functions
from utils import clearOutput, flush
from screens import welcomeScreen
from fights import bossFight, playMaze, mainMap, userInput, kingdomNames, knights, demonPrince, magicalStone

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
from fights import user
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
flush()

mainMap()

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

print("You and the knights return to the capital of " + kingdomNames[0] + ".")
time.sleep(3)
clearOutput(1)

print("You and the knights enter the castle.")
time.sleep(3)
clearOutput(1)

print("You and the knights enter the throne room.")
time.sleep(3)
clearOutput(1)

print("You and the knights see the king.")
time.sleep(3)
clearOutput(1)

print("The king says,")
time.sleep(1.5)
print()
print(f'"{user}, WAKE UP! YOU ARE GOING TO BE LATE FOR SCHOOL!"')
time.sleep(3)
clearOutput(3)

print("You wake up and see your mom yelling at you. You also find out that everything that happened was a just a dream.")
time.sleep(3)
print()

end = input("Press enter to exit the game...")