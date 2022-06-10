# Development plan: Process for writing programs
# Chapter 4 uses encapsulation, generalization:

import turtle
turtle.Turtle()

def square1(t):             # Functions are encapsulation.
    for i in range(4):
        t.fd(100); t.lt(90)

square1(bob)

def square2(t, length):         # Added parameter is generalization
    for i in range(4):
        t.fd(length); t.lt(90)

square2(bob, 100)

# 1. Write program with no functions
# 2. Encapsulate coherent sections in functions
# 3. Generalize with parameters
# 4. Repeat 1-3 until set of working functions
# 5. Refactor: Group similar code into general function

# Some drawbacks at later stages but good for now