# Uses python2

def last_fib(n):
    if n<= 1:
        return n
    previous = 0
    current = 1
    for i in range(1,n,1):
        previous, current = current, previous + current
    return str(current)[-1]


def Huge_Fib(n, m=10):
    # Initialize a matrix [[1,1],[1,0]]
    v1, v2, v3 = 1, 1, 0
    #print bin(n)
    # Perform fast exponentiation of the matrix (quickly raise it to the nth power)
    for rec in bin(n)[3:]:  # change the n into binary value
        #print "rec", rec
        calc = (v2 * v2) % m
        #print calc
        v1, v2, v3 = (v1 * v1 + calc) % m, ((v1 + v3) * v2) % m, (calc + v3 * v3) % m
        #print "v1:", v1, "v2:", v2, "v3:", v3
        if rec == '1': v1, v2, v3 = (v1 + v2) % m, v1, v2
    return v2


n = int(input())
print Huge_Fib(n)
# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n = int(input)
#     print last_fib(n)


