#Uses python2

def fib(n):
    if n<=1:
        return n
    previous = 0
    current = 1
    for i in range(1,n,1):  # i from 1 to n+2, so n+2 is contain in this loop
        previous, current = current, previous + current
    return current


n = int(input())
print fib(n)

# def calc_fib(n):
#     if (n <= 1):
#         return n
#
#     return calc_fib(n - 1) + calc_fib(n - 2)
#
# n = int(input())
# print(calc_fib(n))


