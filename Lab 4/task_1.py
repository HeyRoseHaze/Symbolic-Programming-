

def convert(temperature):
    Celsius = temperature - 273.15
    return Celsius

while True:
    Kelvin = float(input('\nEnter the temperature in Kelvin: '))
    if Kelvin < 0:
        print("Please enter a value above 0")
    else:
        temperature = convert(Kelvin)
        print(f"{Kelvin} Kelvin is {temperature:.2f} degree Celsius")
