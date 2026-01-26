def rev_num(n):
    rev = 0
    old = n
    while n != 0 :
        dig = n % 10
        rev = rev *10 + dig
        n = n //10
    print(rev)
    if rev == old :
        print(True)
    else:
        print(False)
n = int(input("enter number:"))


rev_num(n)
