#Any comparission condition can be passed to paramters of if block (==,!=,>,<,>=,<=)
#To join more than one condition, logical operators ccan be used (AND, OR, NOT)

#Syntax:-  
#if(condition):
#   true statements


a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

if(a > b):
    print (f'{a} is greater than  {b}')     #Must have a space or tab for getting inside if scope