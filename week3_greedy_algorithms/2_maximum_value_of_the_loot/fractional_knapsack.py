# Uses python2
import sys
from collections import namedtuple

def get_optimal_value_oldversion(capacity, weights, values):
    value_sum = 0.
    per_value = []
    for j in range(len(weights)):
        per_value.append(values[j]/float(weights[j]))

    for i in range(len(weights)):
        index = per_value.index(max(per_value))
        a = min(capacity, weights[index])
        value_sum += a * per_value[index]
        capacity = capacity - a
        if capacity== 0:
            return value_sum
        else:per_value.remove(per_value[index])

    return value_sum



def get_optimal_value(capacity, weights, values):
    Item = namedtuple("Item", "value weight")
    value = 0
    weight_value_pairs = sorted(
        [Item(v, w) for v, w in zip(values, weights)], # then the v,w are assigned with value. zip means combine
        key=lambda i: i.value / float(i.weight), # to sort according to what, pay attention to the float, otherwise, 3/2 = 2
        reverse=True # thus Item(v,w) are sorted from the largest to the smallest.
    )

    space_left = int(capacity)
    for item in weight_value_pairs:

        # If the item fit into the knapsack, put it and recalculate space left.
        if space_left - float(item.weight) >= 0:
            value += item.value
            space_left -= float(item.weight)
        else:
            value += (item.value / float(item.weight)) * space_left
            space_left = 0
        if not space_left: # this is essenial, since it means if nothing left then break.
            break

    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2] #0:2 means 0 and 1
    values = data[2:(2 * n + 2):2] #means 2, 4, 6... 2*n, since we don't count the 2*(n+1)
    weights = data[3:(2 * n + 2):2] #means 3, 5, 7...
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
