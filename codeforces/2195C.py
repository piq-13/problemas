opuesto = [6, 5, 4, 3, 2, 1]

for _ in range(int(input())):
    n = int(input())
    caras = list(map(int, input().split()))
    c = 0
    i = 1
    while i < n:
        if caras[i] == opuesto[caras[i - 1] - 1] or caras[i] == caras[i - 1]:
            c += 1
            i += 1
        i += 1
    print(c)
