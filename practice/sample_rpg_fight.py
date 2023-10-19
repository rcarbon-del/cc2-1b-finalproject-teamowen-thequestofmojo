import random

bossHealth = random.randint(1500, 2000)
health = random.randint(500, 1000)

while bossHealth or health == True:
    if health <= 0:
        dmg = random.randint(10, 200)
        bossHealth -= dmg
        if health <= 0:
            health = 0
            break
        print("You dealt", dmg, "damage to the boss!")
        print("The boss has", bossHealth, "health left!")

    if bossHealth <= 0:
        bossdmg = random.randint(10, 50)
        health -= bossdmg
        if bossHealth <= 0:
            bossHealth = 0
            break
        print("The boss dealt", bossdmg, "damage to you!")
        print("You have", health, "health left!")

if health == 0:
        print("You died!")
if bossHealth == 0:
        print("You won!")
        