def prime(n):
    for x in range(2,n):
        is_prime = True
        for i  in range(2,int(x**0.5)+1):
            if x % i == 0:
                is_prime = False
                break
        if is_prime:
            print(x)
prime(10)

print("----")

def lam_prime(x):
    if x <= 1:
        return False
    is_p = lambda x :all(x % i != 0 for i in range(2, int(x**0.5)+1))
    return is_p(x)
print(lam_prime(7))

x = int(input("Enter the limit: "))

for i in range(2 , x+1):
    if lam_prime(i):
        print(i)




# int(x**0.5) + 1
# means:
# Calculate square root
# Convert to integer
# Add 1 so range includes the limit