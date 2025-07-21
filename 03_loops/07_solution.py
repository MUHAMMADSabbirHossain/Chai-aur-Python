while True:
    number = int(input("Enter value b/w 1 and 10: "))
    if 1 <= number <= 10:
        print("Number is: ",number)
        break
    else:
        print("Invalid number. Try again")