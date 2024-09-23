def is_even(n):
    return n % 2 == 0

def type_of_triangle(a,b,c):
    if a==b and b==c :
        return 1
    elif a==b or b==c or c==a :
        return 2
    else:
        return 3

def is_leap(yy):
    if yy % 400 == 0:
        return True
    elif yy % 100 == 0 and yy % 400 != 0:
        return False
    elif yy % 4 == 0 :
        return True
    else:
        return False
    
