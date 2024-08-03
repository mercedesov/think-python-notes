def print_right(text):
    if len(text) > 40 and len(text) < 0:
        print('Insert a text with len from 1 to 40 letters in it')
    elif len(text) == 40:
        print(text)
    else:
        print((40 - len(text)) * ' ' + text)

print_right("Monty")
print_right("Python's")
print_right("Flying Circus")