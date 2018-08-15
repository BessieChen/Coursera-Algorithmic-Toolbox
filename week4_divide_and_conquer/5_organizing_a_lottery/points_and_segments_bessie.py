# Uses python3
from __future__ import print_function
from itertools import chain
import sys

def advanced_count_segment(left_end, right_end, point):
    '''first I need to add a mark that the left_end is "left" and right_end is "right", so create a tuple:'''
    left_tuple = zip(left_end,"l"*len(left_end))
    right_tuple = zip(right_end,"r"*len(right_end))
    point_tuple = zip(point, "p"*len(point))
    #also need to create an empty list to later store the result of each point
    result = [0]*len(point) # caution! you cannot write this as list(0*len(point)), since warning will be:'int' object is not iterable

    combine = sorted(chain(left_tuple,right_tuple,point_tuple), key = lambda x: (x[0],x[1]))
    #that is to say we first sort the left_tuple from small to large, if the left_tuple are the same, then we sort the right_tuple
    count = 0
    for numerical_value, which_end in combine:
        if which_end == "l": count += 1
        elif which_end == "r": count -= 1
        else: result[point.index(numerical_value)] = count

    return result

def precise_advanced_count_segment(left_end, right_end, point):# but still slow!

    left_tuple = zip(left_end,"l"*len(left_end))
    right_tuple = zip(right_end,"r"*len(right_end))
    point_tuple = zip(point, "p"*len(point))

    result = [0]*len(point)
    combine = sorted(chain(left_tuple,right_tuple,point_tuple), key = lambda x: (x[0],x[1]))

    count = 0
    for numerical_value, which_end in combine:
        if which_end == "l": count += 1
        elif which_end == "r": count -= 1
        else: result[point.index(numerical_value)] = count

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * (n + 1) - 1:2]
    ends = data[3:2 * (n + 1):2]
    points = data[2 * n + 2:]
    cnt = precise_advanced_count_segment(starts, ends, points)
    for x in cnt:
        print(x, end=' ')



