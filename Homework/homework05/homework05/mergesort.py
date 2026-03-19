import sys
"""
merging function 
"""
def merge(list1,list2):
    """
    Merge function details
    It should take as input two sorted lists and return a single merged list that is still sorted.
    To do this, look at the first element of each list, pick the smallest, remove it from the list (or move a pointer to the next index) and store that smallest value in the new list to be returned.
    Continue to do this until one of the lists is empty (or till you’ve covered all the elements of one list).
     At that point, copy all the elements from the remaining list into the new, merged list which is then returned.
    """
    newList = []
    while len(list1) != 0 and len(list2) != 0:
        if list1[0] < list2[0]:
            newList.append(list1[0])
            list1.remove(list1[0])
        else:
            newList.append(list2[0])
            list2.remove(list2[0])
    if len(list1) != 0:
        for num in list1:
            newList.append(num)
    if len(list2) != 0:
        for num in list2:
            newList.append(num)
    return newList

def sort(lst):
    """
    Now that we can merge two sorted lists, all that we need to do is write the sorting function.
    It should take a list, and should return a sorted list. This is the function that implements the steps described in the introduction and contains the recursive calls.
    This function splits a list in half, recursively calling itself on both parts. It then calls the merge function to merge the two sorted halves.
    """
    if len(lst) <= 1:
        return lst
    else:
        halfwayPoint = len(lst)//2
        leftHalf = lst[0:halfwayPoint]
        rightHalf = lst[halfwayPoint:]
        leftHalf = sort(leftHalf)
        rightHalf = sort(rightHalf)
        return merge(leftHalf,rightHalf)
def main():
    inputFile = open(sys.argv[1], "r")
    outputFile = open(sys.argv[2], "w")
    listNums = []
    for line in inputFile:
        listNums.append(line)
    for line in listNums:
        outputFile.write(line)
if __name__ == "__main__":
    """
        read in the appropriate data and put it to a list
    """
    main()
