#Uses python2

import sys
from collections import namedtuple

def max_dot_product(aa, bb):
    sort_a = sorted(aa, key=lambda x: x, reverse=True)
    sort_b = sorted(bb, key=lambda x: x, reverse=True)

    Sorted = namedtuple("Sorted","a b")
    iter = [Sorted(a,b) for a,b in zip(sort_a,sort_b)]
    res = 0
    for item in iter:
        res += item.a*item.b
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
