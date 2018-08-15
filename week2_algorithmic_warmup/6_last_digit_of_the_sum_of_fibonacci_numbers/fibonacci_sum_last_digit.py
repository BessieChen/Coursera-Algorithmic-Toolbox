# Uses python2
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


# the following is too slow, so I don't use
# def fib_sum_new(n):
#     sum = 0
#     for i in range(n+1):
#         sum += Huge_Fib(i)
#     return str(sum)[-1]



input = sys.stdin.read()
n = int(input)
print((Huge_Fib(n+2)-Huge_Fib(0+1))%10)



