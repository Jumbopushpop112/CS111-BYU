# tree abstraction
def tree(label, branches=[]):
	return [label] + list(branches)

def label(tree):
	return tree[0]

def branches(tree):
	return tree[1:]

def is_leaf(tree):
	return len(branches(tree)) == 0

# create a simple tree
t = tree(3, [
          tree(1),
          tree(2, [
            tree(1),
            tree(1)
        ])])
# same as: 
# t = [3,
#        [1],
#        [2,
#          [1],
#          [1]
#        ]
#     ]

print(label(t))
print(is_leaf(branches(t)[0]))

# count the leaves in a tree
def count_leaves(t):
    """Returns the number of leaf nodes in t."""
    if is_leaf(t):
        return 1
    else:
        leaves_under = 0
        for b in branches(t):
            leaves_under += count_leaves(b)
        return leaves_under

print(count_leaves(t)) 

# same as above, but uses the sum function on the result of a list comprehension 
def count_leaves(t):
   """Returns the number of leaf nodes in t."""
   if is_leaf(t):
      return 1
   else:
      branch_counts = [count_leaves(b) for b in branches(t)]
      return sum(branch_counts)

print(count_leaves(t))


# print current tree
print(t) 

# double the labels in a tree
def double(t):
    """Returns a tree identical to t, but with all labels doubled."""
    if is_leaf(t):
        return tree(label(t) * 2)
    else:
        return tree(label(t) * 2,
            [double(b) for b in branches(t)])

# print tree with doubled labels    
print(double(t))

#same as above but the base case is subsumed in the recursive case    
def double(t):
    """Returns the number of leaf nodes in t."""
    return tree(label(t) * 2,
            [double(b) for b in branches(t)])

print(double(t))

# print an indented version of the labels of a tree
def print_tree(t, indent=0):
    """Prints the labels of t with a depth-based
       indent of 2 spaces.
    >>> t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
    >>> print_tree(t)
    3
      1
      2
        1
        1
    """
    print(indent * " " + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 2)

print_tree(t)


def leaves(t):
    """Return a list containing the leaf labels of t.
    >>> t = tree(20, [tree(12, [tree(9, [tree(7), tree(2)])
            ,tree(3)]), tree(8, [tree(4), tree(4)])])
    >>> leaves(t)
    [7, 2, 3, 4, 4]
    """
    if is_leaf(t):
        return [label(t)]
    else:
        leaf_labels = [leaves(b) for b in branches(t)]
        return sum(leaf_labels, [])

t = tree(20, [tree(12, [tree(9, [tree(7), tree(2)])
            ,tree(3)]), tree(8, [tree(4), tree(4)])])    

print_tree(t)
print(leaves(t))


def count_paths(t, total):
    """Return the number of paths from the root to any node in t
    for which the labels along the path sum to total.

    >>> t = tree(3, [tree(-1), tree(1, [tree(2, [tree(1)]), tree(3)]), tree(1, [tree(-1)])])
    >>> count_paths(t, 3)
    2
    >>> count_paths(t, 4)
    2
    >>> count_paths(t, 5)
    0
    >>> count_paths(t, 6)
    1
    >>> count_paths(t, 7)
    2
    """
    if label(t) == total:
        found = 1
    else:
        found = 0
    return found + sum([count_paths(b, total - label(t)) for b in branches(t)])

t = tree(3, [tree(-1), tree(1, [tree(2, [tree(1)]), tree(3)]), tree(1, [tree(-1)])])
print_tree(t)
print(count_paths(t,3))
print(count_paths(t,7))
