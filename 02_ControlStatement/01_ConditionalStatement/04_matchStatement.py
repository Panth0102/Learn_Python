#match(expression/variable):
#   case 1:
#       true block of case 1
#   case 2:
#       true block of case 2
#   case _:
#       default block

day = int(input('Enter a day number (1-7):'))

match(day):
    case 1:
        print('Its is Monday')
    case 2:
        print('Its is Tuesday')
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print('Invalid Entry')
