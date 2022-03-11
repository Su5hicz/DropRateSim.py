import random

from numpy import average;


wantedItterations = None        # Will be set by user input, number of tries for frop
itemDropChance = None           # Set by user input, dropchance of desired item
currentTries = 0                # Number of tries from the last drop
minTries = None                 # Least number of tries between drop
maxTries = None                 # Most number of tries between drop
dropCount = 0                   # How many items dropped
sumBetweenDrops = 0             # Sums up all non drop tries



print("Desired number simulation itterations:")
wantedItterations = int(input())

while wantedItterations < 1:
    print("Number of desired itterations must be integer above 0!")
    print("Input desired number simulation itterations:")
    wantedItterations = int(input()) 

print("Percentage of droprate, either as integer or float number:")
itemDropChance = float(input())
while float(itemDropChance < 0):
    print("Percentage must be an integer or float number above 0!")
    print("Percentage of droprate, either as integer or float number:")
    itemDropChance = float(input()) 
    
for i in range(wantedItterations):
    dropRoll = random.uniform(0,100)
    currentTries += 1
    if(dropRoll <= itemDropChance):
        dropCount += 1
        print("Item has dropped, tries since last drop: ",currentTries)
        if minTries == None or currentTries < minTries:
            minTries = currentTries
        if maxTries == None or currentTries > maxTries:
            maxTries = currentTries
        currentTries = 0
averageTries = 0
if dropCount > 0:
    averageTries = (wantedItterations - dropCount) / dropCount
    
print("Simulation has ended")
print()
print("Drop chance: ", itemDropChance)
print("Number of tries: ", wantedItterations)
print("Item dropped: ", dropCount)
print("Smallest gap between drops: ",minTries)
print("Biggest gap between drops: ", maxTries)
print("Average tries between drops ", averageTries)

