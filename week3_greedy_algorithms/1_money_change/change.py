# Uses python2
import sys

"""Changing money optimally.
The goal in this problem is to find the minimum number of coins needed to
change the given amount of money using coins with denominations
1, 5, and 10.
Samples:
>>> get_change(2)
2 # Explanation: 2 = 1 + 1.
>>> get_change(28)
6 # Explanation: 28 = 10 + 10 + 5 + 1 + 1 + 1.
"""

def get_change(money):
    coins_available = [10, 5, 1]  # must be sorted
    count = 0
    for coin in coins_available:

        count += money // coin  #count = count + (amount // coin) ,"//"means the integer value after divided by coin.
        money %= coin # amount = amount % coin, this is the remainer.
    return count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print get_change(m)


"""
what I learn from this is that when you need to do the work that are alike, eg. money%10, money%5, you can put the value 10,5
into a list, and then use the for loop to process the money variable
"""
