# https://www.hackerrank.com/challenges/python-tuples/problem

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))

# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem?h_r=next-challenge&h_v=zen

import numpy

n = tuple(map(int, input().split()))
print(numpy.zeros(n, dtype=numpy.int))
print(numpy.ones(n, dtype=numpy.int))

# https://www.hackerrank.com/challenges/np-eye-and-identity/problem?h_r=next-challenge&h_v=zen

import numpy

print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))

