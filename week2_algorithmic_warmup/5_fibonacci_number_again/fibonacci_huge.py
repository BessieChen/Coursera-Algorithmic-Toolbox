# Uses python2
import sys
def Huge_Fib(n,m):

    # Initialize a matrix [[1,1],[1,0]]
    v1, v2, v3 = 1, 1, 0
    print bin(n)
    # Perform fast exponentiation of the matrix (quickly raise it to the nth power)
    for rec in bin(n)[3:]: #change the n into binary value
        print "rec",rec
        calc = (v2*v2) % m
        print calc
        v1, v2, v3 = (v1*v1+calc) % m, ((v1+v3)*v2) % m, (calc+v3*v3) % m
        print "v1:",v1,"v2:",v2,"v3:",v3
        if rec == '1': v1, v2, v3 = (v1+v2) % m, v1, v2
    return v2


input = sys.stdin.read()
n, m = map(int, input.split())
print Huge_Fib(n,m)


# def get_fibonacci_huge_naive(n, m):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current  = 1
#
#     for _ in range(n - 1):
#         previous, current = current, previous + current
#
#     return current % m
#
# if __name__ == '__main__':
#     input = sys.stdin.read();
#     n, m = map(int, input.split())
#     print(get_fibonacci_huge_naive(n, m))

