#Syntax:-  
#if(condition):
#   true statements
#elif(condition2):
#   true staement
#else:
#   false statement


a = int(input("Enter value for a: "))

if(a > 10):
    print (f'{a} is greater than  {10}')     #Must have a space or tab for getting inside if scope
elif(a > 5):
    print(f'{a} is greater than 5 and less than 10')
else:
    print (f'{a} is 5 or smaller than 5')     #Must have a space or tab for getting inside else scope