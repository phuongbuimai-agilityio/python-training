# Write a function named uses_none that takes a word and a string of forbidden letters,
# and returns True if the word does not use any of the forbidden letters.
def uses_none(word, forbidden):
    for letter in word.lower():
        if letter in forbidden.lower():
            return False
    return True
print(uses_none('banana', 'xyz'))
print(uses_none('apple', 'abc'))

# Write a function called uses_all that takes a word and a string of letters,
# and that returns True if the word contains all of the letters in the string at least once.

def uses_all(word, required):
    for letter in word.lower():
        if letter not in required.lower():
            return False
    return True

print(uses_all('banana', 'ban'))
print(uses_all('apple', 'api'))
