# Exercise 1: Write a line of code that appends the value 6 to the end of the second list in t. 
# If you display t, the result should be ([1, 2, 3], [4, 5, 6]).
list0 = [1, 2, 3]
list1 = [4, 5]

t = (list0, list1)

convert_list = list(t)
convert_list[1].append(6)
convert_tuple = tuple(convert_list)

print(convert_tuple)

# Exercise 2: Try to create a dictionary that maps from t to a string, and confirm that you get a TypeError.
dict = {
    (list0, list1): "dictionary"
}

print(dict)

# Exercise 3: Write a function called most_frequent_letters that takes a string and prints the letters in decreasing order of frequency.
def most_frequent_letters(string):
    
    # lower all letters, check alpha
    lower_letter = string.lower()
    char = []
    for letter in lower_letter:
        if letter.isalpha():
            char.append(letter)

    # count the number of each letter
    counter = {}
    for item in char:
        if item not in counter:
            counter[item] = 1
        else:
            counter[item] += 1
    print(counter)

    # sort by frequency
    sorted_letters = sorted(counter.items(), reverse=True)

    for ch, count in sorted_letters:
        print(f"{ch}: {count}")