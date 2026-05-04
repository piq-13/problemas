primos = {2, 3}
primo_max = 3

def primo_mas_cercano(n): #n impar
    es_primo = False
    while not es_primo:
        es_primo = True
        for primo in primos:
            if n%primo == 0: es_primo = False
        n += 2
    return n - 2

def añadir_primos(end, start=3): #DEVUELVE PRIMO MAX
    max = 2
    for i in range(start,end,2):
        es_primo = True
        for primo in primos:
            if i%primo == 0:
                es_primo = False
                break
        if es_primo:
            primos.add(i)
            max = i
    return max

for _ in range(int(input())):
    d = int(input())
    if d == 1:
        print(6)
        continue
    if d == 2:
        print(15)
        continue
    a = 1 + d
    if a%2 == 0: a += 1
    #calculo de primos hasa a
    primo_max = añadir_primos(a, start=primo_max)
    a = primo_mas_cercano(a)
    b = a + d
    if b%2 == 0: b += 1
    primo_max = añadir_primos(end=b, start=primo_max)
    b = primo_mas_cercano(b)
    print(a*b)