# To-Do List

## Overview

You are going to create a simple to-do list application that allows users to
create tasks and subtasks. You will implement this using a `Task` class and a
simple user interface (UI) to interact with the `Task` class.

## Sample Execution

```
What do you want to do?
1. Display all tasks
2. Add main task
3. Add subtask
4. Exit (and lose all data)
2
Enter the name of the new task: cleaning

What do you want to do?
1. Display all tasks
2. Add main task
3. Add subtask
4. Exit (and lose all data)
2
Enter the name of the new task: homework

What do you want to do?
1. Display all tasks
2. Add main task
3. Add subtask
4. Exit (and lose all data)
3
Enter the name of the subtask: cs 111
Enter the name of the task this is a subtask of: homework

What do you want to do?
1. Display all tasks
2. Add main task
3. Add subtask
4. Exit (and lose all data)
3
Enter the name of the subtask: math 213
Enter the name of the task this is a subtask of: homework

What do you want to do?
1. Display all tasks
2. Add main task
3. Add subtask
4. Exit (and lose all data)
3
Enter the name of the subtask: project 4
Enter the name of the task this is a subtask of: cs 111

What do you want to do?
1. Display all tasks
2. Add main task
3. Add subtask
4. Exit (and lose all data)
3
Enter the name of the subtask: dishes
Enter the name of the task this is a subtask of: cleaning

What do you want to do?
1. Display all tasks
2. Add main task
3. Add subtask
4. Exit (and lose all data)
1
cleaning
    dishes

homework
    cs 111
        project 4
    math 213

What do you want to do?
1. Display all tasks
2. Add main task
3. Add subtask
4. Exit (and lose all data)
3
Enter the name of the subtask: talk to friend
Enter the name of the task this is a subtask of: volunteer work
Error: There is no task with that name. Please try again

What do you want to do?
1. Display all tasks
2. Add main task
3. Add subtask
4. Exit (and lose all data)
Display
Error: Please enter a number 1-4

What do you want to do?
1. Display all tasks
2. Add main task
3. Add subtask
4. Exit (and lose all data)
4
```

## Program Specification

### The `Task` Class

The program should use a `Task` class to represent each task and subtask. You
will create this class in `task.py`. You can think of a `Task` similar to a node
in a tree structure, where each task can have multiple subtasks, each subtask
can also have its own subtasks, and so on. All task names and subtask names will
be unique.

Your `Task` class should have 2 attributes:

1. `name`: a string representing the name of the task. This should be entered by
    the user when creating a new task.
2. `subtasks`: a list of `Task` objects representing subtasks. This should
    always be an empty list when a task is created.

Your class should have a method `add_subtask` that takes a `Task` object as an
argument and adds it to the end of the `subtasks` list.

You should also have a recursive `__str__` method that returns a string
representation of the task in the following format:

```text
shopping
    apples
        5
    oranges
        7
        check ripeness
```

In this example, `shopping` is the main task, and it has two subtasks: `apples`
and `oranges`. The `apples` subtask has a subtask of `5`, and the `oranges`
subtask has two subtasks: `7` and `check ripeness`.

Each subtask should be indented by four spaces relative to its parent task. In
the example above, `apples` is indented by 4 spaces as a subtask of `shopping`,
and `5` is indented by 8 spaces as a subtask of `apples`.

Each line should end with a newline character (`\n`).

**HINT**: You probably need a recursive helper method to handle all of the
subtasks.

You may add any other functions into your class as needed.

### The UI

The user interface in `todo_list.py` is what allows users to interact with the
`Task` class. You will create a simple text-based menu that allows users to
perform the following actions:

1. Display all tasks: This should call print on each main task. A blank line
    should be printed separating each main task.
2. Add main task: This should prompt the user to enter the name of a new main
    task and then create a new `Task` object with that name, saving it to the
    data structure you created to store tasks.
3. Add subtask: This should prompt the user to enter the name of a new subtask
    and then the name of the task it is a subtask of. If the task exists, it
    should create a new `Task` object for the subtask and add it to the
    appropriate `Task`'s `subtasks` list. Keep in mind that both main tasks and
    subtasks can have subtasks added to them.
4. Exit the program: This ends the interaction with the user. To simplify the
    program, you do not need to save the tasks to a file or database, so all
    data will be lost when the program exits. While letting the program
    complete do not use `exit()` or `quit()` as that would break the unit
    tests.

The user should first be prompted with a main menu that allows them to select
what they want to do from the above list. The user should select an option by
entering *only* the number corresponding to what they want to do. This main menu
should reappear after each action is completed.

**IMPORTANT**: Make sure that your menu numbers match the order above (so that 1
displays the list, 2 adds a main task, 3 adds a subtask, and 4 stops the program
from running)

You should also handle 2 possible cases of user error:

1. If the user enters an invalid option on the main menu (not 1, 2, 3, or 4)
2. If the user tries to add a subtask to a task that does not exist

In both these cases, you should print `Error:` followed by a helpful error
message and return to the main menu without crashing the program.

You should create some sort of data structure or structures to store the main
tasks and subtasks in.

Refer to the sample execution above for an example of how the program should
work and be formatted.

### Provided Documentation

Use `input()` to read input from the user.

## Rubric

| Grade Level   | Required standards                                                                                                                                                                                                                                                                                                                                         |
| :------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Core**      | - `__init__` and `add_subtask` from the `Task` class are written correctly according to the specification<br/>- The UI includes correct functionality for displaying the tasks, adding main tasks, and exiting the program                                                                                                                                 |
| **Advanced**  | - `__str__` from the `Task` class is written correctly according to the specification<br/>- The UI includes correct functionality for adding and displaying subtasks<br/>- Variable names are clear and informative and match Python's naming conventions<br/>- There is no unused code<br/>- The UI prints appropriate and helpful prompts for each input |
| **Excellent** | - Code correctly handles the two cases of user error, including printing helpful error messages<br/>- Code is broken down into functions that follow the Single Responsibility Principle, with no large sections of duplicate code<br/>- Code is easy to read                                                                                              |
