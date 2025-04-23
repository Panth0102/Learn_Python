#Syntax:-  
#if(condition):
#   true statements
#else:
#   false statement


a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

if(a > b):
    print (f'{a} is greater than  {b}')     #Must have a space or tab for getting inside if scope
else:
    print (f'{b} is greater than  {a}')     #Must have a space or tab for getting inside else scope