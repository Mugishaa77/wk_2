#Create an empty list called my_list
my_list = []

#Append the following elements to my list
list_two = [10, 20, 30, 40]
my_list.extend(list_two)

print(f'new list = {my_list}')

#Insert the value 15 at the second position in the list.
my_list[1] = 15
print(my_list)

#Extend my_list with another list: [50, 60, 70]
another_list = [50, 60, 70]
my_list.extend(another_list)

print(f'New extended List = {my_list}')

#Remove the last element from my_list
del my_list[-1]
print(f'List with deleted element= {my_list}')

#Sort my_list in ascending order
sorted_list = sorted(my_list)  
print(f'Sorted list = {sorted_list}')

#Find and print the index of the value 30 in my_list

my_list = sorted_list

if 30 in my_list:
    index_30 = my_list.index(30)
    print("Index of 30:", index_30)
else:
    print("30 is not in the list")
