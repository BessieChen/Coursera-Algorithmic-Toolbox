# Uses python2
import sys

# def lcm_naive(a, b):
#     for l in range(1, a*b + 1):
#         if l % a == 0 and l % b == 0:
#             return l
#
#     return a*b

def lcm(a,b):
    larger = max(a,b)
    smaller = min(a,b)

    while True:
        mod = larger % smaller
        if mod == 0 :
            return (a*b)/smaller
        else:
            larger = smaller
            smaller = mod


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

