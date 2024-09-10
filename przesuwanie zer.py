def transfer_zeros(k):
    for elem in k:
        if elem == 0:
            k.remove(0)
            k.append(0)
    print(k)


print(transfer_zeros([3,4,0,2,0,5,1,6,2]))