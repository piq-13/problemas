t = int(input())
for _ in range(t):
    res = []
    l = input()
    a = input().split()
    while len(a) > 1:
        print((a.pop(0)), (a.pop()), end = " ")
    if a: print(a[0])
    else: print()
