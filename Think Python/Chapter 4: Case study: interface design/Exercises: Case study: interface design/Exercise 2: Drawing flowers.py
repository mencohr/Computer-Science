import turtle
import math

t = turtle.Turtle()
t.speed(10)

def polyline(t, n, length, angle):
    """Draws n-line segments:
    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments"""
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    """Draws arc with given radius, angle:
    t: Turtle
    r: radius
    angle: angle subtended by arc in degrees"""
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # Slight left turn before starting reduces error caused by arc's linear approximation
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def petal(t, r, angle):
    """Draws petal using two arcs:
    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends arcs"""
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

def flower(t, n, r, angle):
    """Draws flower with n petals:
    t: Turtle
    n: number of petals
    r: radius of arcs
    angle: angle (degrees) that subtends arcs"""
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)

def move(t, length):
    """Moves Turtle forward (length) units without leaving trail, leaves pen down"""
    t.pu()
    t.fd(length)
    t.pd()

# Draws three flowers from book
move(t, -100)
flower(t, 7, 60.0, 60.0)

move(t, 100)
flower(t, 10, 40.0, 80.0)

move(t, 100)
flower(t, 20, 140.0, 20.0)

t.hideturtle()
turtle.mainloop()