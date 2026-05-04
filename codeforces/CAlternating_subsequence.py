for _ in range(int(input())):
    length = int(input())
    l = list(map(int, input().split()))
    sign = l[0] > 0
    final = list()
    sub = list()
    for i in l:
        if (i > 0) != sign:
            final.append(max(sub))
            sub = list()
        sub.append(i)
        sign = i > 0
    final.append(max(sub))
    print(sum(final))
