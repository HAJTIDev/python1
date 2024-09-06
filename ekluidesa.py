def calc(a,b):
    while a!=b:
        if a>b:
            a = a-b
        else:
            b = b-a
    return a
a = int(input("Wprowadz a: "))
b = int(input("Wprowadz b: "))
result = calc(a,b)
print("Wynik: ", result)