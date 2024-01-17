# #lists
Avengers=['Hulk','Ironman','Captain America','Scarlet witch','Thor']
#  print(Avengers)
#  print(Avengers[0])

# slicing will exclude the last element3 and include first element 0 so 0 to 2 three values
slicing= Avengers[0:3]
print(slicing)
slicing1= Avengers[2:]
print(slicing1)

slicing_negative= Avengers[-1]
print(slicing_negative)

#same goes over here it includes -2 that is second last value scarlet witch and exclude the -1 the last value.
slicing_negative_1 = Avengers[-2:-1]
print(slicing_negative_1)
slicing_negative_2 = Avengers[-2:]
print(slicing_negative_2)

#changing values in list
Avengers[0]= 'SheHulk'
print(Avengers)

#changing values in multiple places
Avengers[1:3]= ['Deadpool', 'Captain marvel']
print(Avengers)

#adding new values in list(append) append will add the values in last index
Avengers.append('Hulk')
print(Avengers)

#using insert we can add values with index
Avengers.insert(1,'Wolverine')

#removing values in list
Avengers.remove('SheHulk')
print(Avengers)

#with pop function we can remove values using index values
Avengers.pop(4)
print(Avengers)
