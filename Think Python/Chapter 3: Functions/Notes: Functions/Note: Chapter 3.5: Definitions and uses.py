# Moving function call to top: NameError: undefined.
# repeat_lyrics()

def print_lyrics():
    print("First example:", "I'm a lumberjack, and I'm okay.")
    print("First example:", "I sleep all night and I work all day.")

def repeat_lyrics():
    print_lyrics(); print_lyrics()

# Causes NameError: last function undefined before call.
# def repeat_lyrics2():
    # print_lyrics2()
    # print_lyrics2()

# repeat_lyrics2()

def print_lyrics2():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")