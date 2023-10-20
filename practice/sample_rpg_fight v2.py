import random

bossHealth = random.randint(1500, 2000)
health = 700
initialWeaponDamage = 50
healCounter = 3

def clearOutput(num_lines: int):
    cursorUpOne = '\x1b[1A'
    erase = '\x1b[2K'
    for _ in range(num_lines):
        print(cursorUpOne + erase, end='')

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
                if dmg >= 175:
                    print("Critical hit!")
                print("You dealt", dmg, "damage to the boss!")
                print("The boss has", bossHealth, "health left!")
                print()
            
            bossdmg = random.randint(10, 100)
            health -= bossdmg
            if bossHealth >= 0:
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
            end = input("Press enter to continue...")
            clearOutput(14)
            if dmg >= 175:
                clearOutput(1)
            if bossdmg >= 75:
                clearOutput(1)

        elif choice == "2":
            if healCounter > 0:
                heal = random.randint(75, 125)
                health += heal
                if health >= 700:
                    health = 700
                    print("You healed", heal, "health!")
                    print("You have max left!")
                    print()
                else:
                    print("You healed", heal, "health!")
                    print("You have", health, "health left!")
                    print()
                healCounter -= 1
                end = input("Press enter to continue...")     
                clearOutput(11)           
            else:
                print("You have no more heals left!")
                print()
                end = input("Press enter to continue...")
                clearOutput(10)

        elif choice == "3":
            print("You ran away!")
            break
        else:  
            clearOutput(7)

if health == 0:
        print("Game over!")
        print()
        print("You died!")
elif bossHealth == 0:
        print("You won!")
print()
end = input("Press enter to exit...")

        