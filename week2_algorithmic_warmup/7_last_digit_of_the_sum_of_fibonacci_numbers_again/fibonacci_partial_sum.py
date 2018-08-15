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


# def fib_sum_partial_new(from_,to_):
#     sum = 0
#     for i in range(from_,to_+1):
#         sum += Huge_Fib(i)
#     return str(sum)[-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    ans = Huge_Fib(to + 2, 10) - Huge_Fib(from_ + 1, 10)  #I tired and found it is right:
    # that is: F(a)+F(a+1)+...F(b) = F(b+2) - F(a+1)
    ans += 10 if ans < 0 else 0
    print(ans)
    #print(fib_sum_partial_new(from_, to))


