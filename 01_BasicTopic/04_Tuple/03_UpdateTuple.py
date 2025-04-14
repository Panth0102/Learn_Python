#To update a tuple, you need to change it to a list first
#Once you update, add or delete a element, you need to change it to tuple again
#Though 2 tuples can be added to each other

a= ('A','B','C','D','E','F','G')
print(a)

b = list(a)         #Coversion to List
b[1] = 'P'
b.append('H')
b.remove('A')

a = tuple(b)        #Conversion to tuple
print(a)

c = ('I',)          #A single value tuple is not possible, so we need to add a comma at the end

a+=c
print(a)

del a               #Deletes tupple
print(a)    