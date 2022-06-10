def do_twice(f):
    """Text-given function to repeat function call twice using parameter"""
    f(); f()

def print_spam():
    """Text-given function to print string"""
    print("Textbook example:", 'spam')

do_twice(print_spam)            # Testing text-given functions

def print_twice(arg):
    """Text-given function testing do_twice_mod()"""
    print("Modified example at first iteration:", arg); print("Modified example at second iteration:", arg)

def do_twice_mod(f, v):
    """Calls function twice, passing value as argument"""
    f(v); f(v)

do_twice_mod(print_twice, "spam two")

def do_four(f, v):
    """Calls print_twice() four times using two statements"""
    do_twice_mod(f, v); do_twice_mod(f, v)

do_four(print_twice, "spam three")