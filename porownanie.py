def compare(list1,list2):
    for i in list1:
        for j in list2:
            if i==j:
                return True
    else:
        return False

print(compare([1,2,0],[4,5,6,1]))