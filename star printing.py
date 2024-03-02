n = int(input("Enter an integer:"))
enter = str(input("Enter 1 or 0, one for flipped and zero for upright:"))


if enter == '0':
    for i in range(0, n):
        print("*"* int(i), "\n")
elif enter == '1':
    for i in range(n, 0, -1):
        print("*"* int(i), "\n")