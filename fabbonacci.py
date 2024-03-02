def fabbonacci(n):
    if n ==1 :
        return 0
    elif n == 2:
        return 1
    else:
        return "0", fabbonacci(n-1)