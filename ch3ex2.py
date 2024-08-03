def triangle(sym, height):
    for s in range(height + 1):
        print(sym * s, end="\n")

triangle('L', 5)