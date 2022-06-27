import turtle
import math

t = turtle.Turtle()

H = 300
W = H * 0.6

# utilities
def test(t, f):
    """runs function under location, size variable changes
    t: Turtle
    f: called function"""
    # original
    measure(t, W, H)
    f(t, W, H)
    # location test
    move(t, - (W * 2), H - H)
    measure(t, W, H)
    f(t, W, H)
    # size test
    move(t, - (W * 2), - (H + 10))
    measure(t, 150, 100)
    f(t, 150, 100)
    # location, size test
    move(t, W - W, - (H + 10))
    measure(t, 70, 250)
    f(t, 70, 250)

# def test_all(t, f):
#     letters = ["a"]
#     for letter in letters:

def measure(t, W, H):
    """draws proportions for letter functions
    t: Turtle
    W: WIDTH constant
    H: HEIGHT constant"""
    t.setheading(0)
    for i in range(2):
        t.fd(W)
        t.lt(90)
        t.fd(H)
        t.setheading(180)

def move(t, x, y):
    """moves without drawing to coordinate
    t: Turtle
    x: x coordinate
    y: y coordinate"""
    t.pu()
    t.goto(x, y)
    t.pd()

def restart(t, x, y):
    """moves to original position, rotation
    t: Turtle
    x: x-coordinate start of function
    y: y-coordinate start of function"""
    move(t, x, y)
    t.setheading(0)

# structures
def arc(t, r, angle, e):
    """draws arc with radius, angle:
    t: Turtle
    r: radius
    arc_l = amount of curve drawn in degrees
    angle: angle subtended by arc in degrees
    step_l = small length before turn
    step_a = small rotation before step_l
    e: extended horizontal"""
    arc_l = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_l / 4) + 3
    step_l = arc_l / n
    step_a = float(angle) / n
    t.fd(e)
    # slight turn reduces approximation error
    t.rt(step_a / 2)
    for i in range(n):
        t.fd(step_l)
        t.rt(step_a)
    t.lt(step_a / 2)
    t.fd(e)

def ellipse(t, W, H, angle, n):
    startx, starty = t.xcor(), t.ycor()
    move(t, startx + (W * math.cos(n * math.pi / 180)) + W,
         (starty + H * math.sin(n * math.pi / 180)) + H)
    for i in range(angle):
        n += 1
        t.goto((startx + W * math.cos(n * math.pi / 180)) + W,
               (starty + H * math.sin(n * math.pi / 180)) + H)

# letters
def draw_a(t, W, H):
    """draws A
    l = length of diagonal lines
    top_a = top angle of isosceles triangle
    base_a = base angles of isosceles triangle
    mp_x1, mp_y1 = start of horizontal line
    mp_x2, mp_y2 = end of horizontal line
    mp_l = length of horizontal line"""
    startx, starty = t.xcor(), t.ycor()
    l = (((W / 2) ** 2) + (H ** 2)) ** 0.5
    top_a = math.atan((W / 2) / H) * (180.0 / math.pi)
    base_a = math.asin(H / l) * (180.0 / math.pi)
    mp_x1, mp_y1 = (W / 2) / 2, H / 2
    mp_x2, mp_y2 = ((W / 2) + W) / 2, H / 2
    mp_l = (((mp_x2 - mp_x1) ** 2) + ((mp_y2 - mp_y1) ** 2)) ** 0.5
    t.setheading(base_a)
    t.fd(l)
    t.setheading(270 + top_a)
    t.fd(l)
    restart(t, startx, starty)
    t.setheading(base_a)
    t.fd(l / 2)
    t.setheading(0)
    t.fd(mp_l)
    restart(t, startx, starty)

def draw_b(t, W, H):
    """draws B
    W: WIDTH constant
    H: HEIGHT constant
    r1, r2: radii in height proportion
    e: horizontal extension length in width proportion"""
    startx, starty = t.xcor(), t.ycor()
    r1 = (H / 2) * 0.45
    r2 = (H / 2) * 0.55
    e = W - r2
    t.setheading(90)
    t.fd(H)
    for i in range(2):
        t.setheading(0)
        arc(t, r1, 180, e)
        r1 = r2
    restart(t, startx, starty)

def draw_c(t, W, H):
    """draws c
    W: WIDTH constant
    H: HEIGHT constant"""
    startx, starty = t.xcor(), t.ycor()
    adj = "find x length of pt between 0,0 and ellipse start, subtract to adj difference as product of W / 2 and " \
          "fraction of width represented "
    ellipse(t, (W / 2) * .1, H / 2, 300, 30)
    restart(t, startx, starty)

t.pensize(2)

# test(t, draw_a)
# test(t, draw_b)
test(t, draw_c)

turtle.exitonclick()