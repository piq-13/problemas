total = int(input())
res = 0
for lead in range(1,total):
    empl = total - lead
    if empl%lead == 0:
        res += 1
print(res)