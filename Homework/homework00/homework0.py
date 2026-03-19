import math
## CONSTANTS SHOULD GO BELOW THIS COMMENT ##
PEOPLE_PER_LARGE = 7
PEOPLE_PER_MEDIUM = 3
PEOPLE_PER_SMALL = 1
PI = 3.14159265
DIAMETER_LARGE = 20
DIAMETER_MEDIUM = 16
DIAMETER_SMALL = 12
COST_LARGE = 14.68
COST_MEDIUM = 11.48
COST_SMALL = 7.28

def main():
    ## YOUR CODE SHOULD GO IN THIS FUNCTION ##

    #get the amount of each pizza needed
    numPeople = int(input("Please enter how many guests to order for:"))
    numPeople2 = numPeople #copy of variable
    numLarge = 0
    numMedium = 0
    numSmall = 0
    numLarge = numPeople//PEOPLE_PER_LARGE
    numPeople %= PEOPLE_PER_LARGE
    numMedium = numPeople//PEOPLE_PER_MEDIUM
    numPeople %= PEOPLE_PER_MEDIUM
    numSmall = math.ceil(numPeople / PEOPLE_PER_SMALL)
    print(f"{numLarge} large pizzas, {numMedium} medium pizzas, and {numSmall} small pizzas will be needed.\n")

    #calculate total square inches of pizza needed
    if numLarge != 0:
      areaLarge = (PI * math.pow((DIAMETER_LARGE/2),2)) * numLarge
    else:
      areaLarge = 0
    if numMedium != 0:
      areaMedium = (PI * math.pow((DIAMETER_MEDIUM/2),2)) * numMedium
    else:
        areaMedium = 0
    if numSmall != 0:
      areaSmall = (PI * math.pow((DIAMETER_SMALL/2),2)) * numSmall
    else:
        areaSmall = 0
    totalArea = areaLarge + areaMedium + areaSmall
    print(f"A total of {totalArea:.2f} square inches of pizza will be ordered ({totalArea/numPeople2:.2f} per guest.)\n")

    #calculate the total cost
    tipNum = (int(input("Please enter the tip as a percentage (i.e. 10 means 10%):")))
    amountPizzas = (numLarge * COST_LARGE) + (numMedium * COST_MEDIUM) + (numSmall * COST_SMALL)
    tipCost = amountPizzas * (tipNum / 100)
    totalCost = amountPizzas + tipCost
    print(f"The total cost of the event will be: ${totalCost:.2f}")

if __name__ == "__main__":
    main()
