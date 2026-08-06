from unicodedata import category


def calculate_bmi(weight, height): #declaring a function to calculate BMI and taking weight and height as parameters
    bmi = weight / (height ** 2) #calculating BMI, BMI = weight (kg) / height (m)^2
    return bmi #returning the calculated BMI value 

def get_bmi_category(bmi):
    """
    Determine BMI category based on BMI value.
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main(): #defining the main function to execute the program
    weight = float(input("Enter your weight (kg): ")) #taking user input for weight in kilograms and converting it to float
    height = float(input("Enter your height (m): ")) #taking user input for height in meters and converting it to float

    bmi = calculate_bmi(weight, height) #calling the calculate_bmi function and storing the result in the variable bmi
    category = get_bmi_category(bmi) #calling the get_bmi_category function and storing the result in the variable category

    print(f"Your BMI is: {bmi:.2f}") #printing the calculated BMI value rounded to 2 decimal places using formatted string literals
    print(f"Category: {category}")

if __name__ == "__main__": 
    main() #calling the main function to execute the program