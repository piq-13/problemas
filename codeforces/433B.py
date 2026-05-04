import random as rd

length = int(input())
vlist = list(map(int, input().split()))
vlistsorted = sorted(vlist)

prefix = [0] * (length + 1)
prefix_sorted = [0] * (length + 1)

for i in range(length):
    prefix[i + 1] += vlist[i] + prefix[i]

for i in range(length):
    prefix_sorted[i + 1] += vlistsorted[i] + prefix_sorted[i]

for _ in range(int(input())):
    t, l, r = map(int, input().split())
    if t == 1:
        print(prefix[r] - prefix[l - 1])
    else:
        print(prefix_sorted[r] - prefix_sorted[l - 1])