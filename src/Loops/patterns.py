for i in range(1 ,10):
    print(i)
    

for i in  range(1 ,5):
    for j in range(i):
        print("*" , end="")
    print()
    
# *
# **
# ***
# ****
print("\n")
for i in range(5 ,0 , -1):
    for j in range(i):
        print("*" ,end="")
    print()

# *****
# ****
# ***
# **
# *
for i in range(1 ,6):
    for j in range(1 , 6):
        print("*" , end="")
    print()

# *****
# *****
# *****
# *****
# *****

for i in range(1 ,6):
    # for j in range(i):
        print("*")
    # print()
# *
# *
# *
# *
# *


for i in  range(1 ,5):
    for j in range(i):
        print(i , end="")
    print()
# 1
# 22
# 333
# 4444


for i in  range(1 ,5):
    for j in range(i): #range always starts with 0 so i = 0 , when we want  i=1 then i +1
        print(j+1, end="")
    print()

# 1
# 12
# 123
# 1234
a =1
for i in range(1 , 5):
    for j in range(i):
        print(a , end=" ")
        a = a + 1
    print()

# 1
# 2 3
# 4 5 6
# 7 8 9 10