'''99 bottles of beer on the wall, 99 bottles of beer.
Take one down, pass it around, 98 bottles of beer on the wall.'''

def bottle_verse(num):
    while num >= 1:
        print(str(num) +' bottles of beer on the wall,')
        print(str(num) +' bottles of beer.')
        print('Take one down, pass it around,')
        print(str(num - 1) + ' bottles of beer on the wall.')
        print('\n')
        num -= 1

bottle_verse(99)