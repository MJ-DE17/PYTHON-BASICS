def ams(n):
    a = 0
    count = len(str(n))
    temp = n
    while n != 0:
        dig = n % 10
        a = a  + (dig ** count)
        n = n //10
    print(a)

    if temp == a:
        print("An Amstrong")
    else:
        print("Not an Amstrong")

ams(153)