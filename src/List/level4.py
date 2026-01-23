b = [1,2,3,4,5,6,7,8,9,0]
b.append([3,4]) # adds at last
b.extend([6,78]) # adds another iterable , like [4,6]
b.insert(1 ,23) # (pos ,elem)

print(b)

r= [1,2,3,4,55,6,7,8,9,0]

r.remove(55) #value
r.pop(0) #index
r.pop() #pops last ele
# r.clear()


# returns indexing :

print(r.index(9))
print(r.count(2))
print(r)

# sorting:

nums = [3, 1, 4, 2]
nums.sort()
nums.sort(reverse=True) #reverse desc
print(nums)
# revesrsing
nums.reverse()
print(nums)

# coping:
a = [1, 2, 3]
c = a.copy()

print(c)

