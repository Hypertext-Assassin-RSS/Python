tuple1 = (1,2,3,4,5)

tuple2 = (1,'to',3,4,'fi')

print(tuple1[1])

print(tuple2[:])

#tuple is imutable so can't updat or delete but it can delete whole tuple
del tuple2
print(tuple2[:])