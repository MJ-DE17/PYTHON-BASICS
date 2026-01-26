f1 = 1
n = int(input("Enter number :"))
for i in  range (1 , n+1):
    f1 = f1 * i
print(f1)


def fact(nn):
    if nn == 1 or nn == 0:
        return 1
    return nn * fact(nn-1)
print(fact(4))



