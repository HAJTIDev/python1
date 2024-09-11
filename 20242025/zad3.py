def wypelnij_sito(n):
    liczby = [True] * (n+1)
    liczby[0] = liczby[1] = False
    for i in range(2, int(n**0.5) + 1):
        if liczby[i]:
            for j in range(i*i, n+1, i):
                liczby[j] = False
    return liczby

def sito_eratosa(n):
    liczby = wypelnij_sito(n)
    return [x for x in range(2, n+1) if liczby[x]]

def printed(n):
    primes = sito_eratosa(n)
    print(format(n))
    print(*primes, sep=", ")

printed(100)