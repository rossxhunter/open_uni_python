#!/usr/bin/env python3

"""Finding common English words.

For M269 18J TMA02 Question 2.

Student version 1: 30/8/18
"""

# If you have done Question 2b, you may replace 2a by 2b
# to test your dictionary implementation returns the same most frequent words
from TMA02_Q2a import Bag


def valid(word):
    """Return True if word should be added to the bag, otherwise False.
    
    word is a string
    """
    return word != ''


def bag_of_words(filename):
    """Return the words occurring in filename as a bag-of-words.
    
    filename is a string with the name of a text file
    """
    words = Bag()
    # open the file in read-only mode
    with open(filename, 'r') as file:
        # go through the file line by line
        for line in file:
            # transform punctuation into space
            line = line.replace('(', ' ')
            line = line.replace('[', ' ')
            line = line.replace('{', ' ')
            line = line.replace(')', ' ')
            line = line.replace(']', ' ')
            line = line.replace('}', ' ')
            line = line.replace('.', ' ')
            line = line.replace(',', ' ')
            line = line.replace(';', ' ')
            line = line.replace(':', ' ')
            line = line.replace('_', ' ')
            # use space to separate the words in a line
            for word in line.split():
                # remove quote marks and other characters
                word = word.strip("'\"!?+-*/#")
                # put in lowercase
                word = word.lower()
                if valid(word):
                    words.add(word)
    return words

print("Collecting words in Shakespeare's Hamlet...")
all_words = bag_of_words('hamlet.txt')
print("Done")

print('Sorting the words by decreasing frequency...')
frequency = all_words.ordered()
print("Done")

top = 50
print("The", top, "most frequent words are:")
for (count, word) in frequency[:top]:
    print(count, word)