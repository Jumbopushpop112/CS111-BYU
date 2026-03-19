### Implement your code in this file.
#NOTE TO USER: When looking at what code does, it is a good idea to write comments explaining what your code does
def retrieveGradeData(file):
    #declare appropriate lists to hold our file value
    listLabs = []
    listHomeworks = []
    listProjects = []
    listProgressChecks = []
    listMidterms = {}
    listFinals = []
    finalScore = 0
    #Loop through data and look for checks
    for line in file:
       #we do not want comments in our code, this is how we check if a line is a comment
       # this is how we ignore new line characters too!
       if "#" not in line and line != "\n":
        indexSpace = line.index(" ")
        indexComma = line.index(",")
        if "Lab" in line:
            score = line[indexSpace + 1:len(line)]
            listLabs.append(float(score))
        elif "Homework" in line:
            score = line[indexSpace + 1:len(line)]
            listHomeworks.append(float(score))
        elif "Project" in line or "FreeCoding" in line:
            score = line[indexSpace + 1:len(line)]
            listProjects.append(float(score))
        elif "ProgressCheck" in line:
            score = line[indexSpace + 1:len(line)]
            listProgressChecks.append(float(score))
        elif "Midterm" in line:
            score = line[indexSpace + 1:len(line)]
            listMidterms[line[0:indexComma]] = float(score)
        elif "Final" in line:
            finalScore = float(line[indexSpace + 1:len(line)])

    #now that we have our data processed, it is time to print the scores
    printData(listLabs,listHomeworks,listProjects, listProgressChecks, listMidterms,finalScore)

#simplify code by using this to check is a list is empty
def isEmpty(list):
    return len(list) == 0

#simplify by calculating each score via a function
def calculateScore(listScores):
    totalScore = 0
    for score in listScores:
        totalScore += score
    return totalScore

#check if the value exists
def isZero(num):
    return num == 0
def printData(listLabs, listHomeworks, listProjects, listProgressChecks, listMidterms, finalScore):
    # ok sweet, now we need to drop the two lowest lab scores and drop the lowest homeworkGrade
    minHomework = min(listHomeworks)
    listHomeworks.remove(minHomework)
    minValue = min(listLabs)
    listLabs.remove(minValue)
    minValue2 = min(listLabs)
    listLabs.remove(minValue2)
    #declare total possible score values for each assignment
    totalPossibleLabScore = 20 * len(listLabs)
    totalPossibleHomeworkScore = 50 * len(listHomeworks)
    totalPossibleProjectScore =  100 * len(listProjects)
    totalPossibleProgressCheckScore = 100 * len(listProgressChecks)
    #calculate the achieved score
    #for the midterms and final, we can just access the index of which the score is at and display it by a hard coded number because we know that value before hand
    labScore = 0
    homeworkScore = 0
    projectScore = 0
    progressCheckScore = 0
    finalScore = float(finalScore)
    #get the total scores for each assignment in the category
    if not isEmpty(listLabs):
        labScore = calculateScore(listLabs)
    if not isEmpty(listHomeworks):
        homeworkScore = calculateScore(listHomeworks)
    if not isEmpty(listProjects):
        projectScore = calculateScore(listProjects)
    if not isEmpty(listProgressChecks):
        progressCheckScore = calculateScore(listProgressChecks)
    #print the data
    print(projectScore)
    print("Here are the students grades:")
    print("Category              Points         Percentage")
    print(f"Labs:                 {labScore:.1f}/{totalPossibleLabScore}      {(labScore/totalPossibleLabScore)*100:.1f}%")
    print(f"Homeworks:            {homeworkScore:.1f}/{totalPossibleHomeworkScore}      {(homeworkScore/totalPossibleHomeworkScore)*100:.1f}%")
    print(f"Projects:             {projectScore:.1f}/{totalPossibleProjectScore}      {((projectScore/totalPossibleProjectScore)*100):.1f}%")
    print(f"Progress Checks:      {progressCheckScore}/{totalPossibleProgressCheckScore}      {(progressCheckScore/totalPossibleProgressCheckScore)*100:.1f}%")
    print(f"Midterm 1:            {listMidterms["Midterm1"]:.1f}/20        {(listMidterms["Midterm1"]/20)*100:.1f}%")
    print(f"Midterm 2:            {listMidterms["Midterm2"]:.1f}/20        {(listMidterms["Midterm2"]/20)*100:.1f}%")
    if "Midterm3" in listMidterms:
        print(f"Midterm 3:            {listMidterms["Midterm3"]:.1f}/20        {(listMidterms["Midterm3"]/20)*100:.1f}%")
    if finalScore != 0:
        print(f"Final:                {finalScore:.1f}/70        {(finalScore/70)*100:.1f}%")
    #now it is time to compute the final grade
    weightedPercentTotal = 0
    percentTotalGrade = 0
    percentageLabScore = ((labScore/totalPossibleLabScore)*100)/10
    weightedPercentTotal += percentageLabScore
    percentTotalGrade += 0.1
    percentageHomeworkScore = ((homeworkScore/totalPossibleHomeworkScore)*100)/10
    weightedPercentTotal += percentageHomeworkScore
    percentTotalGrade += 0.1
    percentageProjectScore =  (((projectScore/totalPossibleProjectScore)*100)/10)*2
    weightedPercentTotal += percentageProjectScore
    percentTotalGrade += 0.2
    percentageProgressChecksScore = ((progressCheckScore/totalPossibleProgressCheckScore)*100)/10
    weightedPercentTotal += percentageProgressChecksScore
    percentTotalGrade += 0.1
    #get the scores if they exist!
    if "Midterm1" in listMidterms:
     percentMidterm1Score = ((listMidterms["Midterm1"]/20) * 100)/10
     if percentMidterm1Score != 0:
        weightedPercentTotal += percentMidterm1Score
        percentTotalGrade += 0.1
    if "Midterm2" in listMidterms:
      percentMidterm2Score = ((listMidterms["Midterm2"]/20) * 100)/10
      if percentMidterm2Score != 0:
        weightedPercentTotal += percentMidterm2Score
        percentTotalGrade += 0.1
    if "Midterm3" in listMidterms:
      percentMidterm3Score = ((listMidterms["Midterm3"]/20) * 100)/10
      if percentMidterm3Score != 0:
        weightedPercentTotal += percentMidterm3Score
        percentTotalGrade += 0.1
    percentFinalScore = (((finalScore/70)*100)/10)*2
    if percentFinalScore != 0:
        percentTotalGrade += 0.2
        weightedPercentTotal += percentFinalScore
    #now let's compute our weighted percentage total
    finalGrade = weightedPercentTotal/percentTotalGrade
    #now we have the final grade, let's score it as a letter!
    grade = ""
    if finalGrade > 93:
        grade = "A"
    elif finalGrade < 93 and finalGrade >= 90:
        grade = "A-"
    elif finalGrade < 90 and finalGrade >= 87:
        grade = "B+"
    elif finalGrade < 87 and finalGrade >= 83:
        grade = "B"
    elif finalGrade < 83 and finalGrade >= 80:
        grade = "B-"
    elif finalGrade < 80 and finalGrade >= 77:
        grade = "C+"
    elif finalGrade < 77 and finalGrade >= 73:
        grade = "C"
    elif finalGrade < 73 and finalGrade >= 70:
        grade = "C-"
    elif finalGrade < 70 and finalGrade >= 67:
        grade = "D+"
    elif finalGrade < 67 and finalGrade >= 63:
        grade = "D"
    elif finalGrade < 63 and finalGrade >=60:
        grade = "D-"
    else:
        grade = "E"
    print()
    print(f"The overall grade in the class is: {grade} ({finalGrade:.2f}%)")
def main():
    fileName = input("Enter the grade data file's name:")
    file = open(fileName,'r')
    retrieveGradeData(file)
main()
