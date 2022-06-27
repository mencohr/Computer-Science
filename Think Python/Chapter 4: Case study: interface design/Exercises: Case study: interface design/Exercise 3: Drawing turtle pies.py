import turtle
import math

t = turtle.Turtle()
t.speed(10)

def t_pies(t, tris):
    angle = 360 / tris
    length = 50

    outline(t, tris, angle, length)
    finish(t, tris, angle, length)

def finish(t, tris, angle, length):
    base_angle = 90 - (angle / 2)
    outer_length = math.sin(math.radians(angle / 2)) * length * 2

    t.lt(angle)
    t.fd(length)
    t.rt(180 - base_angle)
    for i in range(tris):
        t.fd(outer_length)
        t.rt(angle)

def outline(t, tris, angle, length):
    origin = t.pos()
    for i in range(tris):
        t.lt(angle)
        t.fd(length)
        t.goto(origin)

def move(t, x, tris):
    t.penup()
    t.goto(x, 200)
    t.pendown()
    t_pies(t, tris)

move(t, 0, 5)
move(t, 150, 6)
move(t, 300, 7)

# Text-provided solution in blue after reorienting Turtle:
t.pu()
t.goto(0,0)
t.setheading(0)
t.color("blue")
t.pd()

def draw_pie(t, n, l):
    """Draws pie, moves position to right
    t: Turtle
    n: number of segments
    l: length of radial spokes"""
    polypie(t, n, l)
    t.pu()
    t.fd((l * 2) + 10)
    t.pd()

def polypie(t, n, l):
    """Draws pie in radial segments:
    t: Turtle
    n: number of segments
    l: length of radial spokes"""
    angle = 360.0 / n
    for i in range(n):
        tri(t, l, angle / 2)
        t.lt(angle)

def tri(t, l, angle):
    """Draws icosceles triangle: Turtle starts, ends at peak facing middle of base
    t: Turtle
    l: length of equal legs
    angle: half-peak angle in degrees"""
    base_l = l * math.sin(angle * math.pi / 180)

    t.rt(angle)
    t.fd(l)
    t.lt(90 + angle)
    t.fd(2 * base_l)
    t.lt(90 + angle)
    t.fd(l)
    t.lt(180 - angle)

t.pu()
t.bk(130)
t.pd()

# Draw polypies with various numbers of sides
size = 50
draw_pie(t, 5, size)
draw_pie(t, 6, size)
draw_pie(t, 7, size)
draw_pie(t, 8, size)

t.hideturtle()
turtle.mainloop()