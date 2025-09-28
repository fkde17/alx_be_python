FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temp = int(input("Enter the temperature to convert: "))
temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    print (f"{temp}°C is {celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32}°F")
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    print (f"{temp}°F is  {(fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR}°C")

if temp_unit == "C":
    convert_to_fahrenheit(temp)
elif temp_unit == "F":
    convert_to_celsius(temp)