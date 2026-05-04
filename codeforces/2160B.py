for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == 1 and b == 2 or a == 2 and b == 1: 
        print("YES")
        continue
    x = (2*b - a) / 3
    y = (2*a - b) / 3
    if type(x) == int or type(y == int): print("YES")
    else: print("NO")