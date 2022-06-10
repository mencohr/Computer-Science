# Exercise 1: Initial function, call with passed argument
import turtle
bob = turtle.Turtle()

def square(t):
    """Draws square iteratively, returns to origin"""
    for i in range(4):
        t.fd(200); t.lt(90)

square(bob)
turtle.resetscreen()

# Exercise 2: Length added as parameter to square()
def square2(t, l):
    """Draws square iteratively with length parameter, returns to origin"""
    for i in range(4):
        t.fd(l); t.lt(90)

square2(bob,250)
turtle.resetscreen()

# Exercises 3-5 are examples of refactoring code

# Exercise 3: Polygon
def polyline(t, n, l, ang):
    """Text-given function to draw polygon shapes"""
    for i in range(n):
        t.fd(l); t.lt(ang)

def polygon(t,l,n):
    """Draws n-sided polygon"""
    ang = 360.0 / n               # "360.0" sets as float, avoids error codes
    polyline(t, n, l, ang)

polygon(bob,l=200, n=3)
turtle.resetscreen()

# Exercise 4: Circle as polygon
import math

def circle(t, r):
    """Draws circle by calling polygon()"""
    c = 2 * r * math.pi
    n = int(c / 3) + 3          # Instead of constant, define number of sides by circumference where +3 ensures n >= 3
    l = c / n
    polygon(t, l, n)

def circle2(t, r):
    """Text-given alternate with refactoring"""
    arc(t, r, 360)

circle(bob, 50)
turtle.resetscreen()
circle(bob, 100)
turtle.resetscreen()

# Exercise 5: Circle arc
def arc(t, r, ang):
    """Draws complete circle if 360 degrees, partial otherwise"""
    arc_c = 2 * math.pi * r * ang / 360
    n = int(arc_c / 3) + 1
    a_l = arc_c / n
    a_ang = ang / n
    polyline(t, n, a_l, a_ang)              # Rewritten with text-provided polyline.

arc(bob, 50, 180)
turtle.mainloop()