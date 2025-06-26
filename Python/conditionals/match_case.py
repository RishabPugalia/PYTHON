a = int(input("Enter a number bw 1 and 10: "))

match a:
    case 1:
        print("You won charger")
    case 7:
        print("You won a phone")
    case 9:
        print("You won a laptop")
    case _:
        print("Btter luck next time")