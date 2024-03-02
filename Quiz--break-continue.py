while(True):
    i = int(input("Enter a number:"))
    print(i)
    if i <= 100:
        continue
    else:
        print("Congrats, you printed number greater than 100")
        break
