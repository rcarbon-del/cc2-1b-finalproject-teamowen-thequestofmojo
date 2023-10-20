import random

bossHealth = random.randint(1500, 2000)
health = random.randint(1000, 1500)
initialWeaponDamage = 50
healCounter = 3

while bossHealth or health == True:
    if health >= 0:
        print("What will you do?")
        print("1. Attack")
        print(f"2. Heal ({healCounter} left)")
        print("3. Run")
        print()
        choice = input("Enter choice: ")
        print()
        if choice == "1": 
            dmg = random.randint(initialWeaponDamage, initialWeaponDamage+200)
            bossHealth -= dmg
            if bossHealth <= 0:
                bossHealth = 0
                print("You dealt", dmg, "damage to the boss!")
                print("The boss has", bossHealth, "health left!")
                print()
                break
            else:
                if dmg >= 150:
                    print("Critical hit!")
                print("You dealt", dmg, "damage to the boss!")
                print("The boss has", bossHealth, "health left!")
                print()
            
            if bossHealth >= 0:
                bossdmg = random.randint(10, 100)
                health -= bossdmg
                if health <= 0:
                    health = 0
                    print("The boss dealt", bossdmg, "damage to you!")
                    print("You have", health, "health left!")
                    print()
                    break
                else:
                    print("The boss dealt", bossdmg, "damage to you!")
                    if bossdmg >= 75:
                        print("The attack was super effective!")
                    print("You have", health, "health left!")
                    print()

        elif choice == "2":
            if healCounter > 0:
                heal = random.randint(100, 200)
                health += heal
                if health >= 1500:
                    health = 1500
                    print("You healed", heal, "health!")
                    print("You have", health, "health left!")
                    print()
                else:
                    print("You healed", heal, "health!")
                    print("You have", health, "health left!")
                    print()
                healCounter -= 1                
            else:
                print("You have no more heals left!")
                print()
            
        elif choice == "3":
            print("You ran away!")
            break
        else:  
            print("Invalid input!")
            print()
        

print("Game over!")
if health == 0:
        print("You died!")
elif bossHealth == 0:
        print("You won!")
print()
end = input("Press enter to exit...")

        