#Uses python3

import sys

# the following code doesn't give the right answer for 89999>89
# def which_is_greater(aa,bb):
#     min_length = min(len(str(aa)),len(str(bb)))
#     n_th = 0
#     while n_th < min_length:
#         if str(aa)[n_th] == str(bb)[n_th]:
#             n_th += 1
#         else:
#             if str(aa)[n_th] > str(bb)[n_th]:
#                 return aa
#             if str(aa)[n_th] < str(bb)[n_th]:
#                 return bb
#     return aa
#
# def largest_number(Digit):
#     #write your code here
#     answer = []
#     while Digit:
#         MaxDigit = -100
#         for item in Digit:
#             MaxDigit = which_is_greater(item,MaxDigit)
#         Digit.pop(Digit.index(MaxDigit))
#         answer.append(MaxDigit)
#     res = ""
#     for x in answer:
#         res += x
#     return res

# here is the new one:
# the procedure of this function is that:
# I compare the first one and the second one, and then decide which one is larger
# to compare, I create a cycle for it, which the len(first * len(second)) = len(len(first *second)
# if the first one is larger, then append it to my answer and than

def largest_number(a):
    # write your code here
    res = ""
    while len(a):
        first = a[0]
        for second in a[1:]:
            # print("second",second)
            # print(len(second))
            # print("first",first)
            # print(first * len(second))
            # print(second * len(first))
            # here is the thing: if first > second, then skip the following if and then res+=first and remove it
            # if first < second, then let second replace the first, and res+=first and then remove
            # notice that even when first = second, doesn't mean that we don't have the former first anymore
            # the former first is still exist in a[0], for the next while loop, the a[0] still compare with the next a[1]
            if first * len(second) < second * len(first):
                first = second
        res += first
        a.remove(first)
        #print("res",res)
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))



