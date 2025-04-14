a = ('Apple','Samsung','Vivo','Redmi','Google')

#Basic for loop
for i in a:
    print(i)

#Range function & len
for i in range(len(a)):
    print(f'{i}  {a[i]}')       #i will return value number and a[i] will retun value at i index

#While loop
i = 0
while i < len(a):
    print(a[i])
    i += 1