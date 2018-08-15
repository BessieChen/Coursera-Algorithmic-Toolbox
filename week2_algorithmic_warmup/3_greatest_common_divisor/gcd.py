# Uses python2
import sys

def gcd(a,b):
    larger = max(a,b)
    smaller = min(a,b)

    while True:
        mod = larger % smaller
        if mod == 0 :
            return smaller
        else:
            larger = smaller
            smaller = mod

#
# def gcd_naive(a, b):
#     current_gcd = 1
#     for d in range(2, min(a, b) + 1):
#         if a % d == 0 and b % d == 0:
#             if d > current_gcd:
#                 current_gcd = d
#
#     return current_gcd

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print gcd(a, b)
