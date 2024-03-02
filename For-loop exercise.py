List = [1, 2, 3, 4, 5, 123, 23, 45, 67, 21, 692, 43546]

for i in List:
    if str(i).isnumeric() and i > 6:
        print(i)
