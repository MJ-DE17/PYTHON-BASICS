class InvalidMarksError(Exception):
    pass
try :
    f = open("marks.txt" ,"r" )
    data = f.read().strip()
    marks = int(data)

    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100")
except FileNotFoundError as e :
    print("file not found " , e)
except ValueError as e :
    print("Invalid data in name" , e)

except InvalidMarksError as e :
    print(e)
else :
    print("MArks accepted")
finally :
    if 'f' in locals():
        f.close()