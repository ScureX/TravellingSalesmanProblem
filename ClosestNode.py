from math import sqrt
from tkinter import *
from datetime import datetime
from time import sleep
from math import factorial
import random

class City:
    #x, y, name = None, None, None

    def __init__(self, size):
        self.x = random.randint(0, size)
        self.y = random.randint(0, size)
        self.connections = 0
        self.name = self.generateName()

    def generateName(self):
        vowels = ['a','e','i','o','u']
        consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'y', 'z']

        name = ""
        prob = 0
        i = 0
        while(True):
            if(i > 2):
                prob += 10 # increase probability to end name generation
            
            if(i % 2 == 0):  # if even number
                name += random.choice(vowels)
            else:            # if odd number
                name += random.choice(consonants)
            
            if(random.randint(0, 100) < prob):
                return name
            i += 1

    def getName(self):
        return self.name

    def getCoords(self):
        return [self.x, self.y]

    # def get closest city?

def display(canvas, top):
    # pack canvas before loop
    canvas.pack()
    # window loop
    top.mainloop()

# window
top = Tk()
size = 1000
scale = 1.01
dotsize = 5
nodeAmount = 10
possibilities = factorial(nodeAmount - 1)/2
# make window
top.geometry("{}x{}".format(int(size*scale), int(size*scale)))

# make canvas
canvas = Canvas(top, bg="white", height=str(size), width=str(size))

# get seed 
seed = input("seed? ")
if(seed == ""):
    random.seed(datetime.now())
else:
    random.seed(seed)

# make list of cities / generate them
cities = [City(size) for count in range(nodeAmount)]

# display cities as dots, bigger than coordinates
i = 1
for city in cities:
    print(str(city.getName()) + ": " + str(city.getCoords()))
    canvas.create_oval([c - dotsize for c in city.getCoords()], [c + dotsize for c in city.getCoords()], fill='red')
    canvas.create_text([c - 10 for c in city.getCoords()], fill='blue', text=str(i))
    i += 1

fullDistance = 0
currCityIndex = 0
for i in range(0, len(cities)):
    cities[currCityIndex].connections += 1
    # current city has the closest coords
    closestDistance = size*2 # size that is too big anyway
    closestCity = cities[currCityIndex]

    for newCity in cities:
        distance = sqrt(pow(newCity.x - cities[currCityIndex].x, 2) + pow(newCity.y - cities[currCityIndex].y, 2))
        if(cities[currCityIndex] is not newCity and newCity.connections < 1 and distance < closestDistance):
            closestDistance = distance
            closestCity = newCity
    
    
    canvas.create_line(cities[currCityIndex].getCoords(), closestCity.getCoords(), fill='black', width=2, arrow='last')
    currCityIndex = cities.index(closestCity)
    fullDistance += distance

    canvas.pack()
    top.update()
    x = input("")

print("pathlength: " + str(fullDistance))
display(canvas, top)