"""
ECM1414 - Data Structures and Algorithms

Weekly Exercie 1
"""

import os
import time

def sum_of_even(numbers: list[float]) -> float:
    """Takes a list of numbers and returns the sum of all the even numbers."""

    # Initialise a sum of even numbers variable
    sum_of_even_numbers = 0
    # Loop through each number in the list
    for i in range(len(numbers)):
        # Check if the number is even
        if numbers[i] % 2 == 0:
            # Add this even number to the sum
            sum_of_even_numbers += numbers[i]

    # Return the sum
    return sum_of_even_numbers


def check_if_float(text: str) -> bool:
    """Checks if the input can be converted to a float."""
    try:
        number = float(text)
        return True
    except:
        return False


def check_input(user_input: str):
    """Checks the user input to see if it is separated by commas and only contains floats."""

    # Try block to catch any errors
    try:
        # Separate the list at each comma
        separated_list = user_input.split(",")

        # Initialise a list to hold all the numbers
        numbers = []

        # Loop through to check each item is a number
        for i in range(len(separated_list)):
            # Check if a number
            if check_if_float(separated_list[i]) is True:
                # Add this float to the list
                numbers.append(float(separated_list[i]))
            else:
                return {"valid": False}
        
        # Return the list of floats
        return {
            "valid": True,
            "list": numbers
        }
    except:
        return {"valid": False}


def main():
    """
    Main entry point.
    
    Handles the input and validation of a list of numbers.
    """

    # Boolean that keeps track of whether the user wants/needs to input another list
    more_input = True

    # Loop to allow the user to input more than one array
    while more_input is True:
        # Clear the console screen
        os.system('cls')

        # Print app title
        print("=== Sum of all even numbers in given list ===")

        # Ask the user to input a list of numbers
        user_input = input("Input a list of nums separated by a comma:\n >> ")

        # Validate the list
        validation_result = check_input(user_input)

        # Check if the validation is a success
        if validation_result["valid"] is False:
            # Inform the user that the list if invalid
            print("List is invalid!")
            # Allow the user to read the message
            time.sleep(0.75)
            # Restart input process
            continue

        # Retrieve the converted numbers
        list_of_numbers = validation_result["list"]

        # Calculate the sum of all the even numbers
        sum_of_even_numbers = sum_of_even(list_of_numbers)

        # Ouput the sum
        print(f"Sum = {sum_of_even_numbers: .4f}")

        # Ask the user if they want to input another list or exit
        user_input = input("\nWould you like to restart? y/n: ")

        # Check if the user wants to restart
        if user_input == "y":
            continue
        else:
            break

if __name__ == "__main__":
    main()
