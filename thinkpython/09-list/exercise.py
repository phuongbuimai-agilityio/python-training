# Exercise 1: Two words are anagrams if you can rearrange the letters from one to spell the other. 
# For example, tops is an anagram of stop.

# One way to check whether two words are anagrams is to sort the letters in both words. 
# If the lists of sorted letters are the same, the words are anagrams.

# Write a function called is_anagram that takes two strings and returns True if they are anagrams.

# Remove whitespace, and convert to lowercase
def remove_whitespace(word):
    word = word.replace(" ", "").lower()
    
    return word

def is_anagram(word1, word2):
    word1 = remove_whitespace(word1)
    word2 = remove_whitespace(word2)

    return sorted(word1) == sorted(word2)


print(is_anagram("tops", "stop"))
print(is_anagram("apple", "banana"))

# Exercise 2: Write a function called reverse_sentence 
# that takes as an argument a string that contains any number of words separated by spaces.

def reverse_sentence(input_string):
    sentence = ' '.join(input_string.split()[::-1]).lower()

    return sentence.capitalize()

print(reverse_sentence("Python list"))