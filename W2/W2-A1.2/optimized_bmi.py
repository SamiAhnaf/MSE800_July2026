def is_float(n): #If string can be converted to a floating number, returns that number. Otherwise returns False.
    
    try:
        return float(n)
    except ValueError:
        return False


def input_float(hint): #Prints hint and asks the user to enter a number. Repeats until a valid decimal number is entered.
    
    while True:
        value = is_float(input(hint))

        if value is not False:
            return value

        print("Please enter a number.")


class BMICalculator:

    def get_data(self): #Gets weight in kilograms and height in centimetres. Height is converted to metres.
        
        self.weight = input_float("Please enter your weight in kilograms: ")
        self.height = input_float("Please enter your height in centimetres: ") / 100

    def calculate(self): #Calculates and returns BMI.
            
        return round(self.weight / (self.height ** 2), 2)


def main():
    print("\n" + "=" * 42 + "\n")
    print("Wanna know your BMI?")

    calculator = BMICalculator()
    calculator.get_data()

    bmi = calculator.calculate()

    print(f"Your BMI is {bmi}")
    print("\n" + "=" * 42 + "\n")


if __name__ == "__main__":
    main()