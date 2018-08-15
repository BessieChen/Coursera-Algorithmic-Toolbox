# Uses python3
from __future__ import print_function
import sys
import math

def binary_search(a, x):
    left, right = 0, len(a)-1
    #print(right)
    #print(a[left],a[right])

    while left<=right:
        #print("l:",left,"r",right)
        mid = left + ((right-left) // 2)
        #print("mid",mid)
        if x==a[mid]:
            return mid
        elif x>a[mid]:
            left = mid+1
        else:
            right = mid-1

    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

def binary_search_his(a, x):

    left, right = 0, len(a) - 1
    while left <= right:
        mid = left + (right - left) // 2

        a_mid = a[mid]
        if x == a_mid:
            return mid

        # left--mid--x--right
        if a_mid < x:
            left = mid + 1

        # left--x--mid--right
        elif x < a_mid:
            right = mid - 1

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    #print(n)
    m = data[n + 1]
    #print(m)
    a = data[1 : n + 1]
    #print(a)
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        #print(linear_search(a, x), end = ' ')

        #print("x:",x)
        print(binary_search(a, x), end = ' ')
