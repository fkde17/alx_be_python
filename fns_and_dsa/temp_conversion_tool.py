temp = int(input("Enter the temperature to convert: "))
temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

def convert_to_fahrenheit(celsius):
    global temp
    print (f"{temp}°C is {(5 / 9) * (celsius - 32)}°F")
def convert_to_celsius(fahrenheit):
    global temp
    print (f"{temp}°F is  {(9/5)*fahrenheit + 32}°C")

if temp_unit == "C":
    convert_to_fahrenheit(temp)
elif temp_unit == "F":
    convert_to_celsius(temp)