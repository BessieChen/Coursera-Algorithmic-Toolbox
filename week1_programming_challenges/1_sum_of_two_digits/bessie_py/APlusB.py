# Uses python2
# There are two ways of running this program:
# 1. Run
#     python3 APlusB.py
# then enter two numbers and press ctrl-d/ctrl-z
# 2. Save two numbers to a file -- say, dataset.txt.
# Then run
#     python3 APlusB.py < dataset.txt

import sys
input = sys.stdin.read()
tokens = input.split()
print tokens
a = int(tokens[0])
b = int(tokens[1])
print a+b

my_list=[a,b]
print my_list
with open ('dataset.txt','w') as f:
 for i in range(len(my_list)):
     print i
     f.write(str(my_list[i-1])+'\n')
