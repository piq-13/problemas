s = input()
i = 0
solution = "hello"

for c in s:
    if c == solution[i]: i += 1
    if i == 5: 
        print("YES")
        break
if i != 5: print("NO")