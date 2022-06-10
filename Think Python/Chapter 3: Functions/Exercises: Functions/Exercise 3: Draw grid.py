def do_four(f):
    """Repeats rows for grid()"""
    f(); f(); f(); f()

def border():
    """Draws ASCII border"""
    print("+", end = " ")
    print("- - - -", end = " ")
    print("+", end = " ")
    print("- - - -", end = " ")
    print("+")

def row():
    """Draws ASCII row"""
    print("|", end = " ")
    print("       ", end = " ")
    print("|", end = " ")
    print("       ", end = " ")
    print("|")

def grid(f):
    border(); do_four(row); border()

grid(row)