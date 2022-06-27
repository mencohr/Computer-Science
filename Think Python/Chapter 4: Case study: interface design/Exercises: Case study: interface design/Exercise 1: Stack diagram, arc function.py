# Exercise 1.1: Stack diagram of text-given code for circle(bob, radius)

# __future__ module prevents future Python incompatibilities
from __future__ import print_function, division

import math
import turtle

def polyline(t, n, length, angle):
    """Draws "n" line segments:
    t: turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments"""
    for i in range(n):
        t.fd(length); t.lt(angle)

def circle(t, r):
    """Draws circle with given radius:
    t: turtle
    r: radius"""
    arc(t, r, 360)

# Exercise 1.2: Stack diagram for arc

def arc(t, r, angle):
    """Draws arc with given radius and angle:
    t: turtle
    r: radius
    angle: angle subtended by arc in degrees"""
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # Making slight left turn before starting reduces error caused by linear approximation of arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

# Checks if running as script or imported
# If script, run test code. Don't if imported

if __name__ == '__main__':
    bob = turtle.Turtle()

    # Draws circle centered on origin
    radius = 100
    bob.pu()
    bob.fd(radius)
    bob.lt(90)
    bob.pd()
    circle(bob, radius)

    # Waits for user to close window
    turtle.mainloop()