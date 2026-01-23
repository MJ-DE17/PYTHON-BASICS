

try :
    a = int(input("Enter a num 1 : "))
    b =int( input("Enter a num 2 :"))

    result = a /b
except ZeroDivisionError as e:
    print("Cant divide by zero")
    print(e)

except ValueError as e:
    print("Only Integers")
    print(e)
except Exception as e:
    print("something went wrong")
    print(e)
else :
    print(result)
finally:
    print("did Exception handling")
