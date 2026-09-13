def decor(func):
    def wrapper(a,b):
        result = func(a,b)
        return result **2
    return wrapper
@decor
def add(a,b):
    return a + b
print(add(2,3))