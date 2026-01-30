t = int(input())

for _ in range(t):
    for _ in range(3):
        s = input()
        if "?" in s:
            res = ({'A', 'B', 'C'} - set(s)).pop()
    print(res)
    print()