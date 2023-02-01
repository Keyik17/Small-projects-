import numpy as np 
size = int(input("Enter a matrix size: "))

for a in range(size):
    for b in range(size):
        if a <= 1 or a >= size -2 or b <= 1 or  b >= size -2:
            print('#', end ='')
        else:
            print('~', end='')
    print()
