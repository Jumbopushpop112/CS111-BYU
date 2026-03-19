class Link:

    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(
            rest, Link), "Link does not follow proper structure"
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
    
def count_targets(link, targets):
    return count_targets_iterative(link, targets)
    # return count_targets_recursive(link, targets)
    ...
def count_targets_iterative(link, targets):
    dicTargets = {x:0 for x in targets}
    #traverse through each part of the linked list
    #if the current value is already a key, increase its value by 1
    #to keep the loop going, set the link equal to the rest of itself
    while link is not Link.empty:
        if link.first in dicTargets:
            dicTargets[link.first] +=1
        link = link.rest
    return dicTargets
def count_targets_recursive(link, targets):
    #base case - return a blank dictionary
    if link is Link.empty:
        return {x:0 for x in targets}
    #create a dictionary with the targets as values
    targetCount = count_targets_recursive(link.rest, targets)
    #loop through each value, if it is found, increase it's value by 1
    if link.first in targetCount:
            targetCount[link.first] += 1
    return targetCount
def remove_targets(link, targets):
    #if our link is empty, return a blank tuple
    if link is Link.empty:
        return Link.empty
    #oops! we want to remove it
    elif link.first in targets:
        return remove_targets(link.rest, targets)
    #keep it, it's a good boy
    else:
        return Link(link.first, remove_targets(link.rest, targets))


