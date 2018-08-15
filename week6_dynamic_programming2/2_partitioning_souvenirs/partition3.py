# Uses python3
import sys
import itertools

def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0

def optimal_weight_bessie_update(W,w):
    items = [0] + w #so that we can construct [0 ,w1, w2, w3...]
    Weight_matrix = [ [0]*(W+1) for _ in range(len(items)) ] #thus the matrix has (1+wn) rows, and W+1 column
    #print(Weight_matrix)
    #Thus the i_th row means the i_th item, and the j_th column means the j weight.
    #We need to fill the matrix row by row, not column by column

    for i in range(1,len(items)): #since the first row has already been filled up, we now need to fill up the second row.
        for j in range(1,(W+1)):
            if j - items[i] < 0:
                Weight_matrix[i][j] = Weight_matrix[i-1][j]
            else:
                Weight_matrix[i][j] = max(Weight_matrix[i-1][j], (Weight_matrix[i-1][j-items[i]]+items[i]))

    # We also need to find out which items we indeed choose to use:
    item_choosen = []
    i = len(items)-1
    j = W

    while i!=0 and j!=0:
        #print("item = ", i)
        if_not_add = Weight_matrix[i-1][j]
        #print("if_not_add",if_not_add)
        if Weight_matrix[i][j] != if_not_add:
            #print("Weight",Weight_matrix[i][j])
            item_choosen.append(i)
            j -= items[i]
            i -= 1
        else:
             i -= 1

    if item_choosen:
        #print("yes!!!!")
        for item in item_choosen:
            items.pop(item)
    items.pop(0)

    return Weight_matrix[-1][-1],item_choosen,items


def partition3_bessie(A):
    total_value = sum(A)
    if total_value % 3 != 0:
        return 0
    one_third_value = total_value // 3
    #W1 = optimal_weight_bessie_update(one_third_value,A)
    W1 = optimal_weight_bessie_update(one_third_value, A)[0]
    A = optimal_weight_bessie_update(one_third_value, A)[2]

    #print(A)
    W2 = optimal_weight_bessie_update(one_third_value, A)[0]
    A = optimal_weight_bessie_update(one_third_value, A)[2]

    #print(A)
    W3 = sum(A)

    if one_third_value == W1 and one_third_value == W2 and one_third_value == W3:
        return 1
    else:
        return 0






if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    A = data[1:]
    print(partition3_bessie(A))

