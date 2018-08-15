# Uses python3
def edit_distance_old(s, t):
    #write your code here
    return 0


def edit_distance(s, t):
    len_s = len(s) + 1
    len_t = len(t) + 1

    # Create a distance matrix and write in initial values.
    d = [[x] + [0] * (len_t - 1) for x in range(len_s)]
    d[0] = [x for x in range(len_t)]

    for i in range(1, len_s): #for each row
        for j in range(1, len_t): # then for each column

            # Levenshtein distance calculation.
            if s[i - 1] == t[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = min(d[i][j - 1], d[i - 1][j], d[i - 1][j - 1]) + 1

    # The last element of the matrix is edit distance metric.
    return d[-1][-1]


# Uses python3
def edit_distance_maxers(a, b):
    list_a, list_b = [0]+ [x for x in a], [0]+ [y for y in b]
    n, m = len(list_a), len(list_b)
    d = [[0 for x in range(m)] for y in range(n)]
    for i in range(n): d[i][0] = i
    for j in range(m): d[0][j] = j
    for j in range(1, m):
        for i in range(1, n):
            insertion = d[i][j - 1] + 1
            deletion = d[i - 1][j] + 1
            match = d[i - 1][j - 1]
            mismatch = d[i - 1][j - 1] + 1
            if list_a[i] == list_b[j]:
                d[i][j] = min(insertion, deletion, match)
            else:
                d[i][j] = min(insertion, deletion, mismatch)
    return d[n - 1][m - 1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
