text = str(input("pierwsze zdanie "))
text2 = str(input("drugie zdanie "))
text = text.lower()
text2 = text2.lower()
s = text + " " + text2
s = s.split(" ")
tab = []

for i in range(len(s) - 1, 0, -1):
    j = 0
    for k in range(1, i + 1):
        if s[j] < s[k]:
            j = k
    temp = s[i]
    s[i] = s[j]
    s[j] = temp

for i in s:
    if i not in tab and i != "":
        tab.append(i)
print(tab)