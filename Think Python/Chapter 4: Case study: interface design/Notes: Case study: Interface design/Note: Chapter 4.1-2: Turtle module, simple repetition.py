import turtle
t = turtle.Turtle()

def draw_square(t):
    """Draws square from starting place, returns to origin"""
    for i in range(4):          # Draw iteratively, avoiding redundant commands
        t.fd(200); t.lt(90)

draw_square(t)
turtle.mainloop()