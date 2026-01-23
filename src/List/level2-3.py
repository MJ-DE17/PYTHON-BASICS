nums = [10, 20, 30, 40 , 70 ,50 ,60,80,]
# index:  0   1   2   3

# accesing
print(nums[0])
print(nums[-1])

# slicing
print(nums[1:2]) #20
print(nums[:2])  #[10, 20]
print(nums[::2]) #[10, 30]
print(nums[2:])

# slicing with step
# list[start : end : step]
print(nums[::-1]) # -1 step goesbackward
print(nums[-1::-1])

# modify

nums[1:4] = [1,3,4]
print(nums)

# replace and change size
nums[1:3] = [99]
print(nums)

# delete using slice
nums[1 :3] = []
print(nums)

nums = [1, 2, 3]
nums[1] = [9, 9]
print(nums)

