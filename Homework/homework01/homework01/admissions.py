# Provided code
# This function checks to ensure that a list is of length
# 8 and that each element is type float
# Parameters:
# row - a list to check
# Returns True if the length of row is 8 and all elements are floats
def check_row_types(row):
    if len(row) != 8:
        print("Length incorrect! (should be 8): " + str(row))
        return False
    ind = 0
    while ind < len(row):
        if type(row[ind]) != float:
            print("Type of element incorrect: " + str(row[ind]) + " which is " + str(type(row[ind])))
            return False
        ind += 1
    return True
# define your functions here
def convert_row_type(studentScores):
    listFloatScores = [float(score) for score in studentScores]
    return listFloatScores

def calculate_score(scoreSet):
    return round(((int(scoreSet[0]) / 160) * 0.3) + ((scoreSet[1] * 2) * 0.4) + (int(scoreSet[2]) * 0.1) + (scoreSet[3] * 0.2),2)

def is_outlier(SATscore, GPA, StudentInterest):
    normalizedGPA = GPA * 2
    normalizedSAT = SATscore/160
    return StudentInterest == 0 or normalizedGPA > normalizedSAT + 2

def calculate_score_improved(scoreSet, SATscore, GPA, StudentInterest):
    score = calculate_score(scoreSet)
    isOutlier = is_outlier(SATscore, GPA, StudentInterest)
    return score > 6 or isOutlier

def grade_outlier(listGrades):
    sortedListGrades = sorted(listGrades)
    if sortedListGrades[1] - sortedListGrades[0] > 20:
        return True
    else:
        return False

def grade_improvement(listGrades):
    sortedListGrades = sorted(listGrades)
    return listGrades == sortedListGrades

def main():
    filename = "admission_algorithms_dataset.csv"
    input_file = open(filename, "r")    
    output_file = open("student_scores.csv","w")
    file_6score = open("chosen_students.csv","w")
    outliers_file = open("outliers.csv", "w")
    chosenImproved_file = open("chosen_improved.csv","w")
    betterImproved_file = open("better_improved.csv","w")
    compositeChosen_file = open("composite_chosen.csv", "w")
    print("Processing " + filename + "...")
    # grab the line with the headers
    headers = input_file.readline()
    # TODO: loop through the rest of the file
    listStudents = []
    for line in input_file:
        listStudents.append(line.split(","))

    #get each students name, put it into a list
    studentNames = [student[0] for student in listStudents]

    #remove student names from list
    listStudents = [student[1:] for student in listStudents]

    #convert each row
    nameIndex=0
    for scoresStudent in listStudents:
        scoresStudent = convert_row_type(scoresStudent)
        if check_row_types(scoresStudent) == False:
            print("Error!")
        #make the lists
        firstFourNums = scoresStudent[0:4]
        lastFourNums = scoresStudent[4:len(listStudents) + 1]
        score = calculate_score(firstFourNums)
        #write data to file
        output_file.write((str(studentNames[nameIndex])+"," + str(f"{score:.2f}") + "\n"))
        if score >= 6:
            file_6score.write(str(studentNames[nameIndex])+"\n")
        if is_outlier(firstFourNums[0], firstFourNums[1], firstFourNums[2]):
            outliers_file.write(str(studentNames[nameIndex])+"\n")
        if score >= 6 or (is_outlier(firstFourNums[0], firstFourNums[1], firstFourNums[2]) and score >= 5):
            chosenImproved_file.write(str(studentNames[nameIndex])+"\n")
        if calculate_score_improved(firstFourNums,firstFourNums[0], firstFourNums[1], firstFourNums[2]):
            betterImproved_file.write( (studentNames[nameIndex] + "," + str(firstFourNums[0]) + "," + str(firstFourNums[1]) + "," + str(firstFourNums[2]) + "," + str(firstFourNums[3])) )
            betterImproved_file.write("\n")
        if score >= 6 or ((score >= 5) and ((is_outlier(firstFourNums[0], firstFourNums[1], firstFourNums[2])) or (grade_outlier(lastFourNums)) or (grade_improvement(lastFourNums)))):
            compositeChosen_file.write(str(studentNames[nameIndex]))
            compositeChosen_file.write("\n")
        nameIndex += 1
    #VERY IMPORTANT! Files must be closed after writing!
    input_file.close()
    output_file.close()
    file_6score.close()
    outliers_file.close()
    chosenImproved_file.close()
    betterImproved_file.close()
    compositeChosen_file.close()













# this bit allows us to both run the file as a program or load it as a
# module to just access the functions
if __name__ == "__main__":
    main()
