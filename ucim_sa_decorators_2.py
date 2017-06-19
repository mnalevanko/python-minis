from functools import wraps

def kontrola(func):
    @wraps(func)
    def wrapper(*args):
##        print(args)
        if args[1] != 0:
            return func(*args)
        return 'Sorry, you can\'t divide by zero.'
    return wrapper

@kontrola
def divide(a, b):
    return 'Vysledok: {}/{} = {}'.format(a, b, a/b)

print(divide(5, 2))
print(divide(13, 8))
print(divide(4, 0))
print(divide(7, 3))

    
