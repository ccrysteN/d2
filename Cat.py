import random

class Animal:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.health = 50
        self.alive = True
    def to_hunt(self):
        print("Time to hunt")
        self.gladness += 5
        self.health -= 4
    def to_sleep(self):
        print("I will sleep")
        self.gladness += 2
        self.health += 4
    def to_walk(self):
        print("Time for a walk")
        self.gladness -= 6
        self.health += 1
    def is_alive(self):
        if self.health <= 0:
            print("Health is over...")
            self.alive = False
        elif self.gladness < 0:
            print("Too boring...")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Health = {self.health}")
    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life "
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_walk()
            self.end_of_day()
            self.is_alive()
        elif live_cube == 2:
            self.to_sleep()
            self.end_of_day()
            self.is_alive()
        elif live_cube == 3:
            self.to_hunt()
            self.end_of_day()
            self.is_alive()

Cat = Animal(name="Incomprehensibility")

for day in range(365):
    if Cat.alive == False:
        break
    Cat.live(day)