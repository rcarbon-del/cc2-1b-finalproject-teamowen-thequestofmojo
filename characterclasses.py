import random

class Enemy:
    def __init__(self, name):
        self.name = name
        if self.name == "demon":
            self.enemyHealth = random.randint(350, 700)
            self.enemydmg = random.randint(120, 175)
        elif self.name == "human trafficker":
            self.enemyHealth = random.randint(250, 500)
            self.enemydmg = random.randint(90, 140)
        elif self.name == "monster":
            self.enemyHealth = random.randint(300, 600)
            self.enemydmg = random.randint(105, 160)

class Player:
    def __init__(self, name):
        self.name = name
        if self.name == "Radge":
            self.health = 9999
            self.attack = 9999
            self.defense = 9999
            self.healCounter = 9999
        else:
            self.health = random.randint(1000, 1500)
            self.attack = 50+random.randint(10, 30)
            self.defense = 50+random.randint(1, 25)
            self.healCounter = random.randint(5, 8)