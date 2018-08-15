# Uses python3
from __future__ import print_function
import sys

def optimal_sequence_old(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def optimal_sequence_bessie(n):
    Op_sequence = [0]
    Op_sequence.append(1)
    for i in range(2,n+1):
        temp = 100000
        #print(i)

        if Op_sequence[i-1] < temp:
            temp = Op_sequence[i-1]
        if  i%3 == 0:
            #print(i/3)
            if Op_sequence[i/3] < temp:
                temp = Op_sequence[i/3]
        if  i%2 == 0:
            #print(i / 2)
            if Op_sequence[i/2] < temp:
                temp = Op_sequence[i/2]
        Op_sequence.append(temp+1)
    # this code from other is also very efficient:  min_hops = min([hop_count[x] for x in indices])
    #then is to trace back to the coming result:
    #for each value, the possible value it comes from, eg. 12 can come from 11, 6, 4
    index = n
    result = []
    result.append(n)
    while index != 1:
        possible_origin = []
        possible_origin.append(index-1)
        if index % 2 == 0:
            possible_origin.append(index/2)
        if index % 3 == 0:
            possible_origin.append(index/3)
        index = min([(i,Op_sequence[i]) for i in possible_origin], key = lambda x: x[1])[0]
        #print(index)
        result.append(index)
    return reversed(result)

def optimal_sequence(n):
    # Create a list which stores the hop count from an element to 1.
    hop_count = [0] * (n + 1)
    # Path from 1 to 1 is 1.
    hop_count[1] = 1
    for i in range(2, n + 1):
        indices = [i - 1]
        if i % 2 == 0:
            indices.append(i // 2)
        if i % 3 == 0:
            indices.append(i // 3)

        # Get the index with the least hop count to 1.
        min_hops = min([hop_count[x] for x in indices])

        # Write hop count from current index to 1. Hop count incremented by 1.
        hop_count[i] = min_hops + 1

    # ptr points to current position of hop_count.
    ptr = n
    optimal_seq = [ptr]
    while ptr != 1:

        # The list contains next hop candidates.
        candidates = [ptr - 1]
        if ptr % 2 == 0:
            candidates.append(ptr // 2)
        if ptr % 3 == 0:
            candidates.append(ptr // 3)

        # Choose from the candidates whose hop count is the least.
        ptr = min(
            [(c, hop_count[c]) for c in candidates],
            key=lambda x: x[1]
        )[0]
        optimal_seq.append(ptr)

    return reversed(optimal_seq)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence_bessie(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
