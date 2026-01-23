from Tools.scripts.findlinksto import visit

nums = [10, 20, 30 ,7 ,5 ,7]

min_ele = nums[0]
for x in nums:
    if min_ele > x:
        min_ele = x

print(min_ele)

# Sum , Average of List Elements
def sum(list):
    total = 0
    for i in nums:
        total += i
    return total , total/len(nums)
print(sum(nums))

# Check if Element Exists in List

def exists(letter):
    found = False
    for i in nums:
        if letter == i :
            found = True
    return found

print(exists(5))

# Remove Duplicates (Preserve Order)

def dup(word):
    found = False
    for i in nums :
        if i == word:
            found = True
            nums.remove(i)
    return nums
# print("Duplicates :" , dup(7))

# Count Occurrence of Each Element

def count():
    visited = []
    for i in nums:
        if i not in visited:
            print(i , nums.count(i))
            visited.append((i))
count()
print("-----------")
def man_count():
    visited = []
    for i in range(len(nums)):
        if nums[i] not in visited:
            count = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count += 1
            print(nums[i] , count)
            visited.append(nums[i])
man_count()

# Reverse a List Using Loop
# fr loop
def reverse(list):
    # start = 0
    # end = nums(len())
    # # while start < end:
    rev =[]
    for x in nums:
        rev.insert(0,x)
    print("using For loop :", rev)
reverse(nums)

# here: 1st - [1,2,3,4]
# 1 at 0
# 2 at 0
# 3 at 0
# 4 at 0
# so all goes abck : [4,3,2,1] Sd postion at 0

# inplace using whileloop
def rev_while(list):
    left = 0
    right = len(nums) -1
    while left < right :
        nums[left] , nums[right] = nums[right] , nums[left]
        left += 1
        right -= 1
rev_while(nums)
print("While loop :", nums)


# Find Second Largest Element#

def sec_large(list):
    largest = nums[0]
    second = -1
    for x in nums:
        if x > largest :
            largest = x
            if x > second :
                second = x
    print(second)

sec_large(nums)

nums = [0, 1, 0, 3, 12]
def zeros_At_end(list):
    new_lst = []
    for i in nums:
        if i != 0:
            new_lst.append(i)

    if len(new_lst) != len(nums):
        for i in range( len(new_lst) ,len(nums)):
            new_lst.append(0)
    return new_lst
print(zeros_At_end(nums))

# Check if List is Sorted

def is_sorted(list):
    nums = [1,2,3,4,1]
    flag = True
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            flag = False
            break
    return flag

print(is_sorted(nums))

# Merge Two Lists

a =[1,2,3,4]
b = [9,8,7,4,16]
a.extend(b)
print(a)
print("-------------")

a =[1,2,3,4 , 7]
b = [9,8,7,4,16]
# Find Common Elements Between Two Lists
def common_ele(a ,b):
    result = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j] and a[i] not in result:
                result.append(a[i])
                break

    return result
print(common_ele(a , b))


# common = []
#
# for x in a:
#     if x in b:
#         common.append(x)
#
# print(common)

