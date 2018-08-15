# Uses python3
import sys

def get_change(money):
    Num_of_changing_m = []
    Num_of_changing_m.append(0)
    coins = [1, 3, 4]
    for m in range(1, money+1):  # from known to un-known
        #print(m)
        comp = 1000
        for item in coins:
            if m-item >= 0:
                temp = Num_of_changing_m[m - item] + 1
                if temp < comp:
                    comp = temp
        Num_of_changing_m.append(comp)
        #print("Num_of_changing_m",Num_of_changing_m)
    return Num_of_changing_m[money]



if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
