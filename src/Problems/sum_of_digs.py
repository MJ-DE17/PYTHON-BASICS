def sum_num(n):
    sum =0
    while n != 0 :
        dig = n % 10
        sum += dig
        n = n //10
    print(sum)

n = int(input("enter number:"))

sum_num(n)


def count_dig(n):
    count =0
    while n != 0 :
        dig = n % 10
        count +=1
        n = n //10
    print(count)

n = int(input("enter number:"))

count_dig(n)