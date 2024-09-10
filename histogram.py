#items = ['x','y','z','y','x','y','y','z','x']
#slownik = {}
#i=1

#for elem in items:
 #   if elem not in slownik:
  #      slownik[elem]=i
   # else:
    #    slownik[elem]+=i

#print(slownik)
k= []
items= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
def flatten():
    for elem in items:
        for l in elem:
            k.append(l)

flatten()
print(k)