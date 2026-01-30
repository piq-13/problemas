t = int(input())

for _ in range(t):
    n_gifts = int(input())
    moves = 0
    a = [int(c) for c in input().split()]
    b = [int(c) for c in input().split()]
    amin = min(a)
    bmin = min(b)
    if amin > bmin: amin, bmin, a, b = bmin, amin, b, a # amin < bmin
    for i in range(n_gifts):
        move = b[i] - bmin
        a[i] = a[i] - move
        if a[i] > amin:
            move += a[i] - amin
        moves += move
    print(moves)