# simple calculator

while True:

#ask user for first number
    num1 = float(input("Enter your first number:"))

# ask user for the second number
# 
    num2 = float(input("Enter the second number"))

#as user to input operation

    print("Chose operation")
    print("1 = addition")
    print("2 = substraction")
    print("3 = division")
    print("4 = multiplication")


    choice = input("enter number associated with the operation you wish to perform.")

    if choice == "1":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")

    elif choice == "2":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")

    elif choice == "3":
        if num2 != 0:
            result = num1 / num2
        print(f"{num1} / {num2} = {result}")

    elif choice == "4":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    else:
        print("invalid number or operation, please try again")




