def rev(n):
    if n == 0:
        return 0
    print(n)
    rev(n -1)
rev(4)

def factorial(n):
    if n == 0:
        return 1
    return n * (n-1)
print(factorial(5))

def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))


def sum_list(numbers):
  if len(numbers) == 0:
    return 0
  else:
    return numbers[0] + sum_list(numbers[1:])

my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))