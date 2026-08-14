class TemperatureConverter:
    def __init__(self, temperature):
        self.temperature = temperature

    def convert(self):
        # Check if input starts with C or F
        if not self.temperature or self.temperature[0] not in ["C", "F"]:
            return "Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix."

        # Get the numeric part
        value = self.temperature[1:]

        # Check if the numeric part is valid
        try:
            value = float(value)
        except ValueError:
            return "Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix."

        # Fahrenheit to Celsius
        if self.temperature[0] == "F":
            celsius = (value - 32) * 5 / 9
            return f"{self.temperature} degrees Fahrenheit is converted to {celsius:.2f} degrees Celsius"

        # Celsius to Fahrenheit
        elif self.temperature[0] == "C":
            fahrenheit = (value * 9 / 5) + 32
            return f"{self.temperature} degrees Celsius is converted to {fahrenheit:.2f} degrees Fahrenheit"


# Get input from the user
user_input = input("Enter temperature: ")

# Create an object
converter = TemperatureConverter(user_input)

# Display the result
print(converter.convert())