nums = [10, 20, 30 , 5 ,7]
for x in nums :
    print(x)

for i in range(len(nums)):
    print(nums[i])

for i  , v in enumerate(nums):
    print(i ,v)

# while loop

i =0
while i < len(nums):
    print(nums[i])
    i += 1

for x in nums[::-1]:
    print(x)
print("---------------")
for x in reversed(nums):
    print(x)

print("---------------")

for i in nums :
    if i % 2 ==0 :
        print(i)
print("---------------")
ecount = 0
ocount = 0
for i in nums:
    if i % 2 ==0:
        ecount += 1
    else :
        ocount += 1
print(ecount , ocount)

print("---------------")
numss = [10, 20, 30 , 5 ,7]

max_val = numss[0]

for x in numss:
    if max_val < x :
        max_val = x
print(max_val)

print("---------------")

nest = [[1, 2], [3, 4]]
for sub in nest:
    for x in sub:
        print(x)

print("---------------")
