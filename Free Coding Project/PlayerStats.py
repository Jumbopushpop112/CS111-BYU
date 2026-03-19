"""
Read in the file data and print the names to a file
Function took approximately 30 minutes to write
"""
import math
import random


def readFileData():
    listBatterNames = []
    listAtBats = []
    listHits = []
    listAverages = []
    listRBIs = []
    listTeamNames = []
    playerData = open("Players.txt","r")
    for line in playerData.readlines():
        if not "#" in line:
            line = line.strip("\n")
            line = line.split(",")
            listBatterNames.append(line[0])
            listAtBats.append(line[1])
            listHits.append(line[2])
            listAverages.append(line[3])
            listRBIs.append(line[4])
            listTeamNames.append(line[5])
    writeANames(listBatterNames)
    writeAllStars(listAtBats,listRBIs,listAverages,listBatterNames)
    designateAssignment(listRBIs,listAverages,listBatterNames)
    writeWorldSeries(listBatterNames,listTeamNames)
    removeOutliers(listBatterNames,listAverages,listRBIs,listTeamNames)

"""
Write the names of the players to a file if they have more than 2 letter a's in their name
approximately 30 minutes
"""
def writeANames(listNames):
    outputFile = open("APlayers.txt","w")
    for name in listNames:
        numAs = name.count("A".lower())
        if numAs >= 2:
            outputFile.write( "Batter: " + name)
            outputFile.write("\n")
    outputFile.close()

"""
This function will check to see if a player is considered an all star. To be an all star the following things must be true 
    .They must have batted over .280
    .They must have had at least 65 RBIs
    .They must have had at least 500 at Bats
    approximately 30 minutes to write
    .However, the allstar roster can only have 9 players in it. We'll have to kick those who are not there!
"""
def writeAllStars(bats,rbis,averages,names):
    outputFile = open("AllStars.txt","w")
    outputFile.write("Your 2025 MLB All Star Team!")
    outputFile.write("\n")
    listAllStars = []
    for i in range(len(bats)):
        averages[i] = averages[i].strip(".")
        if int(averages[i]) > 280 and int(rbis[i]) >= 65 and int(bats[i]) > 500:
            listAllStars.append(names[i])
            outputFile.write(names[i])
            outputFile.write("\n")
    print("All Star List:")
    numPlayers = 1
    listPlayers = []
    listPositions = ["RF","CF","LF","SS","2B","3B","1B","C","DH"]
    for batter in listAllStars:
        choicePosition = random.choice(listPositions)
        playerString = f"Player {numPlayers}: {batter} - {choicePosition}"
        print(playerString)
        listPlayers.append(playerString)
        listPositions.remove(choicePosition)
        if numPlayers >= 9:
            print("Oops! Only 9 ALl-Star players can be on a roster.")
            break
        numPlayers += 1
    print("Thought it would be over? Why don't we switch up things and shuffle the roster?")
    listPlayers = shuffle(listPlayers)
    for player in listPlayers:
        print(player)
"""
This function will sadly designate the batters for assignment (removed from the 40 man roster) To be designed for assignment
    .The player had 65 or less RBIs
    .The player's average was below .260
    approximately 30 minutes
"""
def designateAssignment(rbis,averages,names):
    outputFile = open("DesignatedAssignment.txt","w")
    outputFile.write("Those dedicated for assignment after the 2025 MLB Season")
    outputFile.write("\n")
    for i in range(len(rbis)):
        averages[i] = averages[i].strip(".")
        if int(averages[i]) < 260 and int(rbis[i]) <= 65:
            outputFile.write(names[i])
            outputFile.write("\n")
def writeWorldSeries(names,teams):
    outputFile = open("WorldSeriesRings.txt", "w")
    outputFile.write("Here are the top 100 players who got a world series ring!")
    outputFile.write("\n")
    for i in range(len(names)):
        if teams[i] == "Los Angeles Dodgers":
            outputFile.write(names[i])
            outputFile.write("\n")
def shuffle(lst):
   """
   Write Time 15 Minutes
   Fisher-Yates Algorithm Implemented (Translated from JavaScript to Python
   This algorithm works as follows:
   1. Generate a random number in the list
   2. Get the current value
   3. Set the value at the current element to be equal to the random value in the list.
   4. Set the value at the random current element in the list equal to the value in the list you are currently at.
   5. Boom! You have a nice algorithm to sort a  list.
   """
   for i in range(len(lst)-1,0,-1):
       j = math.floor(random.random() * (i+1))
       k = lst[i]
       lst[i] = lst[j]
       lst[j] = k
   return lst
"""
Outliers are batters who had an average over .250 but less than 60 RBIs
Function took approximately 30 minutes to write 
"""
def removeOutliers(listBatters, listAverages, listRBIs, listTeams):
    outputFile = open("Outliers.txt","w")
    outputFile.write("Here are the outliers! They had an average over .250 but less than 60 RBIs\n")
    for i in range(len(listBatters)):
        if int(listAverages[i]) > 250 and int(listRBIs[i]) < 60:
            outputFile.write(f"{listBatters[i]}, {listTeams[i]}\n")
    pass
def main():
    readFileData()
main()
"""
Work Log
Time Spent so Far
4 Hours 30 Minutes- 11-6-2025
"""