"""
Name: FLASK Tutorial
Version 1.0
Dependencies:
Author: Samuel Steiner
Description: A basic math program tht gets te sin of a float passed as an argument
"""
import sys
import math

r = float(sys.argv[1])

s = math.sin(r)
print('Hello, World! sin(%g)=%g' % (r, s))