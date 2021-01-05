#Problem link
'''''''''https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays'''''''''
#Solution
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum_list = []
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            sum_list.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+
            arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
    return max(sum_list)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
