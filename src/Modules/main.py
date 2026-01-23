
from math_ops import add, multiply
from marks import marks, avgmarks
from string_utils import rev , is_pallindrome ,revery ,is_pal0l




# 1
print(add(2,4))
print(multiply(4,6))

# 2
print( "Total marks is " , marks(50 ,70,80,99,10))
print("And my Avg is " , avgmarks( 50 , 70,80,99,10))

# 3
word = "sudhu"
reversed_str = rev(word)

print("the reverse str is " , rev(word))
print("Is this pallindrome " , is_pallindrome(word , reversed_str))

# 4 manula pallindrom
print("------------")
print(is_pall(word))

# 5 reverse manual
print(revery(word))