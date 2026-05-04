for _ in range(int(input())):
    n, k = map(int, input().split())
    alist = list(map(int, input().split()))
    total = 1
    for a in alist: total *= a
    resto = total % k
    6