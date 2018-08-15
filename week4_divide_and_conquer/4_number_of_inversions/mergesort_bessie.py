# Uses python3
import sys

def merge(smaller, larger):
    smaller_element = []
    while smaller and larger: #if one of the two original lists is empty, then we stop #mark!
        if smaller[0] < larger[0]:
            smaller_element.append(smaller[0])
            del(smaller[0])

        else:
            smaller_element.append(larger[0])
            del(larger[0])



    smaller_element += smaller if smaller else larger  #remind me of:ans += 10 if ans < 0 else 0
    return smaller_element


def merge_sort(a):
    if len(a) == 1:
        return a
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
    print(merge_sort(a))