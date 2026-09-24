#creating the food classes
class Pizza:
    def prepare(self):
        print("Preparing Pizza")
class Burger:
    def prepare(self):
        print("Preparing Burger")
class Sandwich:
    def prepare(self):
        print("Preparing Sandwich")

#create the food factory class
class FoodFactory:
    @staticmethod
    def get_food(food_type):
        if food_type == "Pizza":
            return Pizza()
        elif food_type == "Burger":
            return Burger()
        elif food_type == "Sandwich":
            return Sandwich()
        else:
            raise ValueError("Invalid food type")

#use the food factory
food = FoodFactory.get_food("Pizza")
food.prepare()  # Output: Preparing Pizza