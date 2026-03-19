from task import Task
def printOptions():
    print("What do you want to do?")
    print("1. Display all tasks")
    print("2. Add main task")
    print("3. Add subtask")
    print("4. Exit and lose all data")
def getOption():
    try:
        userNum = int(input())
        return userNum
    except ValueError:
        print("Error: Please enter in a number from 1-4")
def main():
    listMainTasks = []
    subTasks = []
    listTaskNames = []
    while True:
        printOptions()
        userInput = getOption()
        if userInput == 1:
            for task in listMainTasks:
                print(task)
        elif userInput == 2:
            mainTaskName = input("Enter the name of the new task: ")
            mainTask = Task(mainTaskName)
            listMainTasks.append(mainTask)
            listTaskNames.append(mainTask.name)
        elif userInput == 3:
            #create a subtask
            subTaskName = input("Enter the name of subtask:")
            parentTaskName = input("Enter the name of the task this is a subtask of:")
            if parentTaskName not in listTaskNames:
                print("Error: Cannot find a task name with that name. Please try again.")
                continue
            parentTask = None
            for task in listMainTasks:
                if task.name == parentTaskName:
                    parentTask = task
                    break
            if parentTask is None:
                for task in subTasks:
                    if task.name == parentTaskName:
                        parentTask = task
                        break
            subTask = Task(subTaskName)
            subTasks.append(subTask)
            listTaskNames.append(subTask.name)
            parentTask.add_subtask(subTask)

        elif userInput == 4:
            #exit and lose all the data
            break
if __name__ == "__main__":
    main()


