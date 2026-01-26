def rev_str(str):
    # print(str[::-1])
    for i in range(len(str)+1 , -1):
        print(i)


rev_str("Hey")

s = "Hello"

rev= "".join(reversed(s))
print(rev)

print("-----")


rev = ""
for ch in s:
    rev = ch + rev
print(rev)

# while loop:
print("-While----")

i = len(s)-1
while i >= 0:
    rev += s[i]
    i-=1

print(rev)

# if  rev == s :
