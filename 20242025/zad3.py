liczby = []

def wypelnij_sito(n):
    global liczby
    liczby = [True] * (n+1)
    liczby[0] = liczby[1] = False
    for i in range(2, int(n**0.5) + 1):
        if liczby[i]:
            for j in range(i*i, n+1, i):
                liczby[j] = False

def sito_eratosa(n):
    return [x for x in range(2, n+1) if liczby[x]]

def printed(n):
    wypelnij_sito(n)
    primes = sito_eratosa(n)
    print((n))
    print(*primes, sep=", ")

printed(100)