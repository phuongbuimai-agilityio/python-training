# Exercise: Write a function that counts the number of times each trigram (sequence of three words) appears
from collections import Counter

def count_trigrams(text):
    # Split the text into words
    words = text.split()
    
    # Generate trigrams (sequences of three consecutive words)
    trigrams = [' '.join(words[i:i+3]) for i in range(len(words) - 2)]
    
    # Count the frequency of each trigram
    trigram_counts = Counter(trigrams)
    
    # Print each trigram and its count
    for trigram, count in trigram_counts.items():
        print(f"{trigram}: {count}")
    
    return trigram_counts

text = "the quick brown fox jumps over the lazy dog the quick brown fox"
count_trigrams(text)