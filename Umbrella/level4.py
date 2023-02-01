ESC = '\x1b'
def white_color(shape):
    print('\033[35m{}\033[00m' .format(shape),end='')
def green_color(shape):
    print('\033[32m{}\033[00m' .format(shape), end='')

size = int(input("Enter a matrix size:"))

turn = 0
flag = True
for a in range(size):
    if flag == True:
        turn = 1
    else:
        turn = 0
    for b in range(size):
        if turn%2 == 0:
            white_color('#')
        else:
            green_color('#')
        turn += 1
    flag = not flag
    print()
