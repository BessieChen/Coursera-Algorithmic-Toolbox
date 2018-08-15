# Uses python2
from __future__ import print_function
import sys

def optimal_summands_bessie(n):
    candy = 1
    candy_k = [1]
    n -= 1
    while n:
        candy += 1
        n -= candy
        # the following is the test part, to see when the remaining n subtracted by the next candy(candy+1), is this new remaining part can
        # be subtracted by the next next candy(candy+2)
        candy_next = candy+1
        n_th = min(n-candy_next,candy_next+1)
        if n_th == (candy_next+1):
            candy_k.append(candy)
        else:
            candy_k.append(candy)
            candy_k.append(n)
            n -= n
    return candy_k

def optimal_summands(n):

    summands = [1]
    n -= 1
    while n:
        last_element = summands[-1]
        # Save move: check whether the incremented last element can be used as
        # the next summand.
        if (last_element + 1) * 2 <= n:
            n -= last_element + 1
            summands.append(last_element + 1)
        else:
            if last_element >= n:
                n += summands.pop()
            summands.append(n)
            n = 0
    return summands




if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    #summands = optimal_summands(n)
    summands = optimal_summands_bessie(n)
    print(len(summands))
    for x in summands:
        print(x,end=" ")
