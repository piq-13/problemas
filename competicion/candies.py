t = int(input())
m, b = 0, 0

for _ in range(t):
    length = int(input())
    candies = list(map(int, input().split()))
    m = sum(c for c in candies if c%2 == 0)
    b = sum(c for c in candies if c%2 == 1)
    if m>b:
        print("YES")
    else:
        print("NO")