#!/usr/bin/env python3

"""Tests for the Bag ADT

For M269 18J TMA02 Question 2.

Student version 1: 30/8/18
"""

# change Q2a to Q2b in the next line to test your dictionary implementation
from TMA02_Q2b import Bag

failed = 0
ran = 0

def test(name, actual, expected):
    """Report if test passed or failed."""
    global ran, failed
    if actual == expected:
        print(name, 'OK')
    else:
        print(name, 'FAILED: got', actual, 'instead of', expected)
        failed += 1
    ran += 1

words = Bag()
words.add('once')
words.add('twice')
words.add('twice')

test('size', words.size(), 3)
test('non-existing item', words.count('none'), 0)
test('multiple copies', words.count('twice'), 2)
test('ordered', words.ordered(), [(2, 'twice'), (1, 'once')])

words.clear('what?')
test('clear non-existing', words.size(), 3)
words.clear('once')
test('clear item', words.size(), 2)
test('once gone', words.count('once'), 0)
test('twice remains', words.count('twice'), 2)
test('ordered after clearing', words.ordered(), [(2, 'twice')])

print()
print('Ran', ran, 'tests:', ran - failed, 'OK,', failed, 'FAILED')

if failed == 0:
    print('You passed all our tests. Well done!')
    print('Now add YOUR tests. Think of boundary values.')