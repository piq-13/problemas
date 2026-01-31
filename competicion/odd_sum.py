t = int(input())

for _ in range(t):
    length = int(input())
    haseven, hasodd = False, False
    numbers = list(map(int, input().split()))
    for number in numbers:
        if number%2 == 0:
            haseven = True
        else:
            hasodd = True
        if haseven and hasodd:
            break 
    if (haseven and hasodd) or (hasodd and length%2 == 1):
        print("YES")
    else:
        print("NO")