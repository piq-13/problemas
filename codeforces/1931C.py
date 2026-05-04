for _ in range(int(input())):
    length = int(input())
    alist = list(map(int, input().split()))
    first = alist[0]
    last = alist[length - 1]
    i = 0
    j = -1
    while i < length and alist[i] == first: i += 1
    while j > - (length + 1) and alist[j] == last: j -= 1
    j = length + j + 1
    if first == last:
        if j < 1: print(0)
        else: print(j - i)
    else:
        i, j = max(i, length - j), length
        print(j - i)