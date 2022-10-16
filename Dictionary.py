


dict1 = { 'name':'rajith','age':22,'location':'wikkala' }

#directory is unordered data stuctures so it might be in different order  in print 
print(dict1)

print(dict1['age'])

dict1['name'] = 'sanjaya'
print(dict1)

#add new value by add new value and its referece as updating
dict1['hoby'] = 'no'
print(dict1)

#use del to remove item from dictonary 
del dict1['hoby']
print(dict1)

#empty the dictonary 
dict1.clear()
print(dict1)

#remove the entire directory
del dict1
print(dict1)