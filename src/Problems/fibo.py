def fact(n):
    fib = 0
    a = 0
    b = 1

    if n == 0:
        return 0
    print(a)

    if n == 1:
        return 1
    print(b)

    for i in range(2, n + 1):
        fib = a + b
        print(fib)
        a = b
        b = fib


n = int(input("Enter the number : \n"))

fact(n)


