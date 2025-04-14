a = "Hello World"

print(a.capitalize())   #Init Cap
print(a.casefold())     #Converts Lower
print(a.center(20))     #Makes string Center of given number
print(a.encode())        #Encode string   
print(a.endswith('d'))      #Returns true if the argument is same as end of string
print(a.expandtabs())       #Sets the tab size of the string

print(a.find('o'))       #Finds value and returns index
print(a.count('ll'))     #Counts occurence of event
print(a.index('W'))      #Finds index of argument
print(a.isalnum())       #true if contains numbers and chars   
print(a.isalpha())       #true if only number   
print(a.isascii())      #true if ascii characters 
print(a.isdecimal())    #true id it contains decimal
print(a.isdigit())      #true if contains only digits
print(a.islower())      #true if case is lower
print(a.isnumeric())    #true if case is numberic
print(a.isspace())      #true if contains only space
print(a.istitle())      #true if init cap
print(a.isupper())      #true if case is upper
print(a.strip())        #Removes extra spaces
print(a.split())        #Creates array of strings, if no value is passed to params, separates from space
print(a.replace("Hello","Welcome"))     #Replaces the string
