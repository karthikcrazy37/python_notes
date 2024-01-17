naruto= ['Naruto Uzumaki','Kakashi hatake','Sasuke uchiha', 'Might guy','Itachi uchiha']

for i in naruto:
    print(i)

uchiha = [x for x in naruto if 'uchiha' in x ]  
print(uchiha)
# To Print all items by referring to their index number:
# for i in range(len(naruto)):
#     print(i)

numbers= [1,2,3,4,5]

new_list= [i**2 for i in numbers if i%2==0]
print(new_list)

# squared_even_numbers= []

# for x in numbers:
#     if x%2==0:
#         squared_even_numbers.append(x**2)
# print(squared_even_numbers)
