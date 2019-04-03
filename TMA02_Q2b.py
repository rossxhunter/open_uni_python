#!/usr/bin/env python3

"""An implementation of the Bag ADT, using a dictionary.

For M269 18J TMA02 Question 2.

Student version 1: 7/8/18
"""

class Bag:

    def __init__(self):
        """Create a new empty bag."""
        self.bag = dict()
        

    def add(self, item):
        """Add one copy of item to the bag. Multiple copies are allowed."""
        self.bag[len(self.bag)] = item


    def count(self, item):
        """Return the number of copies of item in the bag.
        
        Return zero if the item doesn't occur in the bag.
        """

        counter = 0
        for index, current_item in self.bag.items():
            if current_item == item:
                counter += 1
        return counter
    
    def clear(self, item):
        """Remove all copies of item from the bag. 
        
        Do nothing if the item doesn't occur in the bag.
        """
        for index, current_item in self.bag.items():
            if current_item == item:
                self.bag.pop(index, None)
                
    def size(self):
        """Return the total number of copies of all items in the bag."""
        return len(self.bag)
    
    def ordered(self):
        """Return the items by decreasing number of copies.
        
        Return a list of (count, item) pairs.
        """
        result = set()
        for index, item in self.bag.items():
            result.add((self.count(item), item))
        return sorted(result, reverse=True)
