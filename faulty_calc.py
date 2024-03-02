operator = input("enter you operator:")
num1 = int(input("Enter the number :"))
num2 = int(input("Enter the number :"))

if operator == "+":
    if num1 == 56 and num2 == 9:
        print("56+9=77")
    elif num1 != 56 and num2 != 9:
        print(num1 + num2)

elif operator == "-":
    print(num1 - num2)

elif operator == "*":
    if num1 == 45 and num2 == 3:
        print("45*3=555")
    elif num1 != 45 and num2 != 3:
        print(num1 + num2)

elif operator == "/":
    if num1 == 56 and num2 == 6:
        print("56/6=4")
    elif num1 != 56 and num2 != 6:
        print(num1 + num2)
