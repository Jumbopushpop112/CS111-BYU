def average_temperature(temps):
    """
    Given a list of temperatures, TEMPS, compute the average
    temperature and return it to the user
    >>> temp_data = [72.2, 68.7, 67.4, 77.3, 81.6, 83.7]
    >>> average_temperature(temp_data)
    75.15
    """
    ### Your code goes here
    sumTemps = 0
    for temp in temps:
        sumTemps += temp
    averageTemp = round(sumTemps/len(temps),2)
    return averageTemp


def hot_days(temps):
    """
    Given a list of temperatures, TEMPS, count the number of days
    more than five degrees above the average.  Print the number of
    days and the average and return the number of days.
    >>> temp_data = [72.2, 68.7, 67.4, 77.3, 81.6, 83.7]
    >>> hot_days(temp_data)
    There were 2 day(s) more than 5 degrees above the average of 75.2.
    2
    """
    ### Your code goes here
    averageTemp = average_temperature(temps)
    hotTemps = 0
    for temp in temps:
        if temp > averageTemp + 5:
            hotTemps +=1
    print(f"There were {hotTemps} day(s) more than 5 degrees above the average of {averageTemp:.1f}.")
    return hotTemps

def is_palindrome(word):
    """
    Given a single word, WORD, determine if it is a palindrome or not.
    Print a message that includes the word stating it is or is not a
    palindrome and return True if it is and False otherwise
    >>> is_palindrome('rotator')
    rotator is a palindrome.
    True
    >>> is_palindrome('apple')
    apple is not a palindrome.
    False
    """
    ### Your code goes here
    reversedWord = word[::-1]
    if word == reversedWord:
        print(word,"is a palindrome.")
        return True
    else:
        print(word, "is not a palindrome.")
        return False
def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    weightedList = [i*x for i,x in enumerate(s) if i % 2 == 0]
    return weightedList