#Problem link
'''''''''https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays'''''''''
#Solution
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

#Problem Statement
"""""""""https://www.hackerrank.com/challenges/time-conversion/problem"""""""""
#Solution
import os
import sys
# Complete the timeConversion function below.
def timeConversion(s):
    time = s.strip()
    h, m, s = map(int, time[:-2].split(':'))
    p = time[-2:]
    h = h % 12 + (p.upper() == 'PM') * 12
    return(('%02d:%02d:%02d') % (h, m, s))

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    f.write(result + '\n')
    f.close()
    
#Problem Statement
""""""""""https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup"""""""""
#Solution
import math
import os
import random
import re
import sys
# Complete the 'countingValleys' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
def countingValleys(steps, path):
    # Write your code here
    valleyCount = seaLevel =  0
    for step in path:
        if step == 'U':
            seaLevel += 1
        else:
            seaLevel -= 1
        if step == 'U' and seaLevel == 0:
            valleyCount += 1
    return valleyCount
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)
    fptr.write(str(result) + '\n')
    fptr.close()
