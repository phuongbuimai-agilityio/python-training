# Write a function named has_duplicates that takes a sequence -- like a list or string -- as a parameter 
# and returns True if there is any element that appears in the sequence more than once.

def value_counts(string):
    counter = {}
    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter

def has_duplicates(t):
    """Check whether any element in a sequence appears more than once.
    
    >>> has_duplicates('banana')
    True
    >>> has_duplicates('ambidextrously')
    False
    >>> has_duplicates([1, 2, 2])
    True
    >>> has_duplicates([1, 2, 3])
    False
    """
    counter = value_counts(t)
    for item in counter:
      if counter.get(item) > 1:
        return True
    return False

print(has_duplicates([1, 2, 2]))
print(has_duplicates([1, 2, 3]))