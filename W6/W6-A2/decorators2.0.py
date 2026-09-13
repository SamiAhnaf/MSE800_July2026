def add_sprinkles(func):
    def wrapper():
        print("You added sprinkles")
        func()
    return wrapper


def add_chocolate(func):
    def wrapper():
        print("You added chocolate")
        func()
    return wrapper


@add_sprinkles
@add_chocolate
def get_ice_cream():
    print("Here is your ice cream")


get_ice_cream()