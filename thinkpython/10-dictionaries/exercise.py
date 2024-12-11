# Exercise 1: Write a function named has_duplicates that takes a sequence -- like a list or string -- as a parameter 
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

# Exercise 2: Write function called find_repeats that takes a dictionary that maps from each key to a counter,
# like the result from value_counts. It should loop through the dictionary and return a list of keys that have counts greater than 1

def find_repeats(dict):
    """Makes a list of keys with values greater than 1.
        
        dict: dictionary that maps from keys to counts
        
        returns: list of keys
        """
    count_item = value_counts(dict)
    list_repeats = []

    for item in count_item:
        if count_item.get(item) > 1:
            list_repeats.append(item)
            
    return list_repeats

print(find_repeats('banana'))