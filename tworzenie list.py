def identity(n):
    array= [[0]*n for i in range (n)]
    #print([0]*10)
    #print(array)
    for idx,item in enumerate(array):
        item[idx]=1
    return array

print(identity(4))