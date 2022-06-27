def ellipse(t, a, b, angle, n, adj):
    for i in range(angle):
        t.goto(a * math.cos(n * math.pi / 180) + WIDTH / 2 + adj, b * math.sin(n * math.pi / 180) + HEIGHT / 2)
        n += 1

def draw_c(t, adjx, adjy):
    startx = adjx * math.cos(30 * math.pi / 180) + adjx
    center_adj = (WIDTH - startx) / 2
    startx += center_adj
    starty = adjy * math.sin(30 * math.pi / 180) + adjy
    teleport(t, startx, starty)
    ellipse(t, WIDTH / 2, HEIGHT / 2, 300, 30, center_adj)


def draw_d(t):
    r = HEIGHT / 2
    e = WIDTH - r
    teleport(t, WIDTH - WIDTH, HEIGHT - HEIGHT)
    t.lt(90)
    t.fd(HEIGHT)
    t.rt(90)
    oblong(t, r, 180, e)
    teleport(t, WIDTH - WIDTH, HEIGHT - HEIGHT)


def draw_e(t):
    d = 0.5
    teleport(t, WIDTH - WIDTH, HEIGHT - HEIGHT)
    t.lt(90)
    t.fd(HEIGHT)
    t.rt(90)
    for i in range(3):
        t.fd(WIDTH)
        teleport(t, WIDTH - WIDTH, HEIGHT * d)
        d = 0


def draw_f(t):
    d = 0.5
    teleport(t, WIDTH - WIDTH, HEIGHT - HEIGHT)
    t.lt(90)
    t.fd(HEIGHT)
    t.rt(90)
    for i in range(2):
        t.fd(WIDTH)
        teleport(t, WIDTH - WIDTH, HEIGHT * d)
        d = 0


def draw_g(t, adjx, adjy):
    draw_c(t, adjx, adjy)
    t.lt(90)
    t.fd(45)
    t.lt(90)
    t.fd(WIDTH / 4)


def draw_h(t):
    teleport(t, WIDTH - WIDTH, HEIGHT)
    t.rt(90)
    t.fd(HEIGHT)
    teleport(t, WIDTH, HEIGHT)
    t.fd(HEIGHT)
    teleport(t, WIDTH - WIDTH, HEIGHT / 2)
    t.setheading(0)
    t.fd(WIDTH)


def draw_i(t):
    d = HEIGHT
    teleport(t, WIDTH / 2, HEIGHT)
    t.setheading(270)
    t.fd(HEIGHT)
    for i in range(2):
        teleport(t, WIDTH - WIDTH, d)
        t.setheading(0)
        t.fd(WIDTH)
        d -= HEIGHT


def draw_j(t):
    r = WIDTH / 2
    teleport(t, WIDTH, HEIGHT)
    t.setheading(270)
    t.fd(HEIGHT - r)
    oblong(t, r, 180, 0)


def draw_k(t):
    mpx = (WIDTH / 2) / 2
    mpy = (((HEIGHT + (HEIGHT * 0.4)) / 2) + (HEIGHT * 0.4)) / 2
    teleport(t, WIDTH - WIDTH, HEIGHT)
    t.setheading(270)
    t.fd(HEIGHT)
    teleport(t, WIDTH - WIDTH, HEIGHT * 0.4)
    t.goto(WIDTH, HEIGHT)
    teleport(t, mpx, mpy)
    t.goto(WIDTH, HEIGHT - HEIGHT)


def draw_l(t):
    teleport(t, WIDTH - WIDTH, HEIGHT)
    t.setheading(270)
    t.fd(HEIGHT)
    t.setheading(0)
    t.fd(WIDTH)


def draw_m(t):
    teleport(t, WIDTH - WIDTH, HEIGHT - HEIGHT)
    t.setheading(90)
    t.fd(HEIGHT)
    draw_v(t)
    t.setheading(270)
    t.fd(HEIGHT)
    teleport(t, WIDTH - WIDTH, HEIGHT - HEIGHT)


def draw_n(t):
    t.setheading(90)
    t.fd(HEIGHT)
    t.goto(WIDTH, HEIGHT - HEIGHT)
    t.goto(WIDTH, HEIGHT)


def draw_s(t):
    teleport(t, WIDTH, HEIGHT * 0.75)
    ellipse(t, WIDTH / 2, HEIGHT / 4, 270, 0, 0)


def draw_v(t):
    teleport(t, WIDTH - WIDTH, HEIGHT)
    t.goto(WIDTH / 2, HEIGHT - HEIGHT)
    t.goto(WIDTH, HEIGHT)


# measure(t)
# t.pensize(5)

# draw_a(t)
# draw_b(t)
# draw_c(t, WIDTH / 2, HEIGHT / 2)
# draw_d(t)
# draw_e(t)
# draw_f(t)
# draw_g(t, WIDTH / 2, HEIGHT / 2)
# draw_h(t)
# draw_i(t)
# draw_j(t)
# draw_k(t)
# draw_l(t)
# draw_m(t)
# draw_n(t)
# draw_s(t)
# draw_v(t)

turtle.mainloop()