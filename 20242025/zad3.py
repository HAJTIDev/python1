def table(n):
    liczby = [True] * (n+1)
    liczby[0] = liczby[1] = False
    for i in range(2, int(n**0.5) + 1):
        if liczby[i]:
            for j in range(i*i, n+1, i):
                liczby[j] = False
    return liczby

def sito_eratost(n):
    liczby = table(n)
    return [x for x in range(2, n+1) if liczby[x]]

def print(n):
    primes = sito_eratost(n)
    print(math.format(n))
    print(format(n))
    print(*primes, sep=", ")

print(100)