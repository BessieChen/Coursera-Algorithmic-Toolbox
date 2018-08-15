# Uses python3
import sys

def merge(smaller, larger): #doesn't have loop, is just a part of the merge_sort()
    smaller_element = []
    inversion_number = smaller[1]
    left_part = smaller[0]
    right_part = larger[0]
    while left_part and right_part: #if one of the two original lists is empty, then we stop #mark!
        if left_part[0] > right_part[0]: #if the right_part is smaller, which violate our rule, then we should add how much the length is the left part.
            smaller_element.append(left_part[0])
            inversion_number += len(left_part)
            del(left_part[0])

        else:
            smaller_element.append(right_part[0])
            del(right_part[0])
    smaller_element += left_part if left_part else right_part  #remind me of:ans += 10 if ans < 0 else 0
    return [smaller_element,inversion_number]


def merge_sort(a): #contains a loop
    if len(a) == 1:
        return [a,0] #which the first one is the real number, the second part of this list is our result.
    mid = len(a)//2
    smaller = merge_sort(a[0:mid])#this is stuck me a while
    larger = merge_sort(a[mid:])
    return merge(smaller,larger)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:]
    b = n * [0]
    print(merge_sort(a)[1])