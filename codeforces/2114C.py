for _ in range(int(input())):
    len = int(input())
    ns = list(map(int, input().split()))
    current = ns[0]
    sol = 1
    for i in range(1, len):
        if current < ns[i] - 1:
            current = ns[i]
            sol += 1
    print(sol)
        