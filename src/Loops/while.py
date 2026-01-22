i = 1
while i <= 8 :
    print(i)
    i += 1
j = 5
while  j >= 1 :
    print(j)
    j -= 1
print("END")

a =1
tot =0
while a <= 10:
    tot += a
    a +=1
print(tot)

print("Sum of even numbers from 1 to 20")

a =1
tot = 0
while a <= 20:
    if a % 2 == 0:
        tot += a
    a +=1
print(tot)

print("Count digits in a number")

num = 13453
count = 0
while num >0:
    count += 1
    num //= 10

print(count)

print('Reverse numeber')

num = 13453
rev = 0
while num > 0:
     dig = num % 10
     rev = rev * 10 + dig
     num //= 10
print(rev)

i =1
while i <=10 :
    if i ==3 :
        break   #this  ends hte loop when 3 comes ,  t ngh executes
    elif i == 5 :
        i += 1
        continue
    print(i)
    i +=1

a =1
i =1
while i <=4:
    j = 1
    while j <= i :
        print(a , end="")
        a =a +1
        j +=1
    print()
    i += 1

# 1
# 23
# 456
# 78910

num = 1
i =1
while i <=4:
    j =1
    while j <= i:
        print( i , end="")
        j+=1
    print()
    i += 1

name = "Sudharsana"
i =0

while i < len(name):
    print(name[i] , end=" ")
    i += 1

word = "programming"
i = 0
count = 0

while i < len(word):
    if word[i] in "aeiou":
        count += 1
    i += 1

print(count)
