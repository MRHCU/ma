"""
Welcome to Lab 04!

We WILL be grading for Header, Comments, Formatting.

Follow the instructions in the lab document. <---- very important
Write your code to complete the tests in the Gradescope autograder.
You must use ALL of the functions included in the template

Necessary print statements:

"Please select one of the following to convert to meters: cm m km in ft: "
"Please select one of the following to convert to grams: mg g kg lbs: "
"Please select one of the following to convert to meters per second: m/s km/h ft/s mph: "
"Please select one of the following to convert to Celsius: C F K: "

"Please input a value:"
"Unsupported unit"
"Invalid unit type"

"""

def get_property():
    """ 
    Prompts user for propery, validates, and returns
    
    Returns:
        mass/speed/distance/temperature if property is supported, False otherwise
    
    """
    pass
    

def get_unit(property):
    """ Prompts user for unit, validates, and returns
    
    Args: 
        property (str): Property to convert
            E.g. mass, speed
            
    Returns:
        String of the specific unit to convert, False if unit is unsupported
        
    """
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
