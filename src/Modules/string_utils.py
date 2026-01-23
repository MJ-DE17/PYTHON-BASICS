

def rev(str):
    result = ""
    for i in range(len(str)-1 , -1 , -1) :
        result += str[i]
    return result

def is_pallindrome(str , result):
    if result.lower() == str.lower():
        return True
    return False

def is_pall(s):
    s =s.lower().strip()

    start = 0
    end = len(s)-1

    while start <= end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

def revery(str):
    rev = ""
    i = len(str) - 1
    while i >= 0 :
        rev += str[i]
        i -= 1
    return rev