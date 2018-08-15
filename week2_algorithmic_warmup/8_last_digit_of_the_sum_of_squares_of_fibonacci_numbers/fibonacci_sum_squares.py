# Uses python2
from sys import stdin
import sys
def Huge_Fib(n,m=10):

    if n==0:
        return 0

    # Initialize a matrix [[1,1],[1,0]]
    v1, v2, v3 = 1, 1, 0
    #print bin(n)
    # Perform fast exponentiation of the matrix (quickly raise it to the nth power)
    for rec in bin(n)[3:]: #change the n into binary value
        #print "rec",rec
        calc = (v2*v2) % m
        #print calc
        v1, v2, v3 = (v1*v1+calc) % m, ((v1+v3)*v2) % m, (calc+v3*v3) % m
        #print "v1:",v1,"v2:",v2,"v3:",v3
        if rec == '1': v1, v2, v3 = (v1+v2) % m, v1, v2
    return v2

def square_fib(n):
    if n<= 1:
        return n
    previous = 0
    n_current = 1
    for i in range(1,n+1,1): #i from 1 to n+2, so n+2 is contain in this loop
        temp = n_current
        n_current = previous + n_current
        #print "i: fib", i + 1,n_current
        previous = temp
        if i == n-1:
            m_current = n_current
            #print "m_current",m_current
    return m_current*n_current % 10

def square_fib_new(n):
    if n<= 1:
        return n
    return str(Huge_Fib(n)*Huge_Fib(n+1))[-1]


    return m_current*n_current % 10

input = sys.stdin.read()
n = int(input)
#print Huge_Fib(n)
print square_fib_new(n)


# def fibonacci_sum_squares_naive(n):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current  = 1
#     sum      = 1
#
#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current * current
#
#     return sum % 10

