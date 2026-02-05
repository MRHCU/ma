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
        print("Please select one of the following to convert to grams: kilograms, milligrams, or pounds")
        return 
    elif property == "speed":
        print("Please select one of the following to convert to meters per second: km/h, ft/s, or miles/hour")
        return
    elif property == "distance":
        print("Please select one of the following to convert to meters: cm, m, km, in, or ft")
        return
    elif property == "temerature":
        print("Please select one of the following to convert to celcius: f, or k")
        return
    else:
        return "unit is unsupported"

    pass

def convert_mass(unit, value):
    pass
                    
def convert_speed(unit, value):
    pass
    
def convert_distance(unit, value):
    pass
    
def convert_temperature(unit, value):
    pass

if __name__ == "__main__":

    print("Welcome to the SI units calculator!")

    print("Please input a type of unit that you would like to convert. Here are your options: \ndistance \nmass \nspeed \ntemperature\n")
    
    property = get_property() #TODO: Implement get_property() to take in user input and validate it

    get_unit(property)



