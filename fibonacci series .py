def fib(n):
    x = 0
    y = 1
    if n <= -1:
        print(" THE   ENTER   NUMBER  IS  INVALID .")
        print("PLEASE   RECHECK  THE  VALUE  YOU  ENTERED")

    elif n == 0:
        print(x)
    elif n == 1:
        print(y)

    else:
        for i in range(2, n):
            z = x+y
            x = y
            y = z
        print(z)


fib(n=int(input("enter the number you required:  ")))