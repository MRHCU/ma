"""

Author: Mason Hoffman
Date: 02/05/2026
Assignment: Lab 04
Course: CPSC1051
Lab Section: 002

Description: This program simulates a program that makes a calculator for conversions

"""

def get_property():
    """ 
    Prompts user for propery, validates, and returns
    
    Returns:
        mass/speed/distance/temperature if property is supported, False otherwise
    
    """
    property = input()

    if property == "mass":
        return "mass"
    elif property == "speed":
        return "speed"
    elif property == "distance":
        return "distance"
    elif property == "temperature":
        return "temperature"
    else:
        return "False"
        
    pass
    

def get_unit(property):
    """ Prompts user for unit, validates, and returns
    
    Args: 
        property (str): Property to convert
            E.g. mass, speed
            
    Returns:
        String of the specific unit to convert, False if unit is unsupported
        
    """

    if property == "mass":
        print("Please select one of the following to convert to grams: g, kg, mg, lbs")
        return 
    elif property == "speed":
        print("Please select one of the following to convert to m/s: m, km/h, ft/s, mph")
        return
    elif property == "distance":
        print("Please select one of the following to convert to meters: cm, m, km, in, ft")
        return
    elif property == "temperature":
        print("Please select one of the following to convert to celcius: C, F, K")
        return
    else:
        return "unit is unsupported"

    pass

def convert_mass(unit, value):
    if unit == "kg":
        return value * 1000
    elif unit == "mg":
        return value / 1000
    elif unit == "lbs":
        return value * 453.592
    else:
        return value
    pass
                    
def convert_speed(unit, value):
    if unit == "km/h":
        return value * 0.277778
    elif unit == "ft/s":
        return value * 0.3048
    elif unit == "mph":
        return value * 0.44704
    else:
        return value
    pass
    
def convert_distance(unit, value):
    if unit == "cm":
        return value / 100
    elif unit == "km":
        return value * 1000
    elif unit == "in":
        return value * 0.0254
    elif unit == "ft":
        return value * 0.3048
    else:
        return value
    pass
    
def convert_temperature(unit, value):
    if unit == "F":
        return (value - 32) * (5 / 9)
    elif unit == "K":
        return value - 273.15
    else:
        return value
    pass

if __name__ == "__main__":

    print("Welcome to the SI units calculator!")

    print("Please input a type of unit that you would like to convert. Here are your options: \ndistance \nmass \nspeed \ntemperature\n")
    
    property = get_property() #TODO: Implement get_property() to take in user input and validate it

    get_unit(property)

    unit = input()

    value = float(input("Please input a value "))

    if property == "mass":
        result = convert_mass(unit, value)
    elif property == "speed":
        result = convert_speed(unit, value)
    elif property == "distance":
        result = convert_distance(unit, value)
    elif property == "temperature":
        result = convert_temperature(unit, value)
    else:
        result = "false"
    
    print(f"{value:.0f} {property} in {unit}: {result}")




