list1= [1,2,3,4,5]

print(list1)

list2 = [1,2,'li','st',3,4,5]

print(list2[2])

print(list2[2:4])

list2[2] = 3

print(list2[:])

#add item to end of the list
list2.append('end')
print(list2[:])

#delete selected index value from list
del list2[3]
print(list2[:])

#remove paramter value from the list
list2.remove('end')
print(list2[:])