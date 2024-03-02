user_age = int(input("Enter your age: "))

if 100 > user_age > 18 :
    print("Yes you can drive!!")

elif user_age == 18:
    print("we cannot decide whether you can drive a car or not. You have to appear in a driving test")

elif user_age > 100:
    print("are you insane")

else:
    print("you cannot drive")
