def all_variants(stroka):
    n = len(stroka)
    for i in range(n):
        for e in range(i+1, n+1):
            yield stroka[i:e]

a = all_variants("abc")
for i in a:
    print(i)

