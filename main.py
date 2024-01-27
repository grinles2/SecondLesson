import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.15
        self.gladness -= 3

    def to_sleep(self):
        print("GO FALL ASLEEP")
        self.gladness += 3

    def to_chill(self):
        print("Time to chill")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Get out from here!")
            self.alive = False
        elif self.gladness <= 0:
            print("Тебе к психиологу бро")
            self.alive = False
        elif self.progress > 5:
            print("Passed Externally")
            self.alive = False
            self.gladness += 50

    def end_of_the_day(self):
        print(f"Gladness =", {self.gladness})
        print(f"Progress = {round(self.progress), 2}")

    def live(self, day):
        d = f"Day{day} of {self.name} life"
        # d = "Day 1 of Oleg Life
        print(f"{d:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_the_day()
        self.is_alive()


nick = Student("Nick")
for day in range(1, 366):
    if nick.alive == False:
        break
    nick.live(day)
