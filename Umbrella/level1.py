import numpy as np

def array(arr):
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            print(arr[x][y], end='')
        print()
       
arr = np.full((8,5), '.')

arr[0][2] = '%'
arr[1][3] = '%'
arr[1][1] = '%'
arr[2][4] = '%'
arr[2][0] = '%'
arr[3][0] = '%'
arr[3][1] = '%'
arr[3][2] = '%'
arr[3][3] = '%'
arr[3][4] = '%'
arr[4][2] = '!'
arr[5][2] = '!'
arr[6][2] = '!'
arr[7][2] = '!'

print(arr)
array(arr)

