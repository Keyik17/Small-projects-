import numpy as np

def array(arr):
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            print(arr[x][y], end='')
        print()
       
size = int(input("Enter a matrix size: "))
arr = np.full((size,size),'.')

start = 0
end = size - 1

for i in range(len(arr)):
    arr[i][start] = 'U'
    arr[i][end] = 'U'

    start += 1
    end -= 1

array(arr)

