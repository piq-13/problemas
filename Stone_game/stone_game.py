t = int(input())
for _ in range(t):
    n = int(input())
    stones = list(map(int, input().split()))
    x = stones.index(min(stones))
    y = stones.index(max(stones))
    if x > y: x, y = y, x
    ans = min(y+1, n-x, (x+1) + (n-y))
    print(ans)
