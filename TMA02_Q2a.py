#!/usr/bin/env python3

"""An implementation of the Bag ADT, using unsorted lists.

For M269 18J TMA02 Question 2.

Student version 1: 6/8/18
"""

class Bag:

    def __init__(self):
        """Create a new empty bag."""
        self.items = []

    def add(self, item):
        """Add one copy of item to the bag. Multiple copies are allowed."""
        self.items.append(item)

    def count(self, item):
        """Return the number of copies of item in the bag.
        
        Return zero if the item doesn't occur in the bag.
        """
        counter = 0
        for an_item in self.items:
            if an_item == item:
                counter += 1
        return counter

    #def clear(self, item):
    #    """Remove all copies of item from the bag. 
    #    
    #    Do nothing if the item doesn't occur in the bag.
    #    """
    #    index = 0
    #    while index < len(self.items):
    #        if self.items[index] == item:
    #            self.items.pop(index)
    #        else:
    #            index += 1
    
                
    def clear(self, item):
        delete = 0
        for _ in self.items:
            if _ == item:
                self.items.pop(delete)
            else:
                delete += 1
                
     
    def size(self):
        """Return the total number of copies of all items in the bag."""
        return len(self.items)
            
    def ordered(self):
        """Return the items by decreasing number of copies.
        
        Return a list of (count, item) pairs.
        """
        result = set()
        for item in self.items:
            result.add((self.count(item), item))
        return sorted(result, reverse=True)