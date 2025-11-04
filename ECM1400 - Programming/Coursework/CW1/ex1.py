#############################################
## Program that converts Celcius to Kelvin ##
## and back again                          ##
#############################################


# Defining temperature conversion function
def kelvin(temperature, to_kelvin=True):   
    # Check if the temp should be converted to kelvin
    if (to_kelvin == True):
        # Convert temp to kelvin
        convertedTemperature = temperature + 273.3
        # Round the converted temperature to the nearest integer
        convertedTemperature = round(convertedTemperature)
    # Check if the temp should be converted to celcius
    elif (to_kelvin == False):
        # Convert temp to celcius
        convertedTemperature = temperature - 273.3
        # Round the converted temperature to the nearest integer
        convertedTemperature = round(convertedTemperature)
    
    # Return the converted temperature
    return convertedTemperature