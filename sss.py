my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list=[]
for number in my_list:#Browse all numbers from the source list.
  if number not in new_list:#if the number doesnt appear within the new list
    new_list.append(number)#add number to new list.
my_list=new_list[:]#make copy of new_list
print("The list with unique elements only:")
print(my_list)