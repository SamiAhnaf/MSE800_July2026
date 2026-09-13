def add_sprinkles(func):
    def wrapper():
        print("You added sprinkles")
        func()
    return wrapper


@add_sprinkles
def get_ice_cream():
    print("Here is your ice cream")


get_ice_cream()