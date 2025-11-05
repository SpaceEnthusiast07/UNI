##############################################
## Program that detects if a word or phrase ##
## is palindrome                            ##
##############################################

# Import the regular expressions module
import re

# Defining the plaindrome function
def palindrome_detector(phrase):
    # Convert the phrase to lowercase
    phrase = phrase.lower()

    # Remove all spaces in the phrase
    #phrase = ''.join(phrase.split(' '))

    # I will use regular expressions to remove everything except letters
    # re.sub(<pattern>, <replacement>, <string>)
    # Pattern:
    #   ^ = not these characters
    #   A-Za-z = all upper and lower case letters
    # Idea: Replaces every character (including spaces) that isn't either A-Z or a-z with ""
    cleanedPhrase = re.sub(r'[^A-Za-z]', '', phrase)

    # Flip the cleaned phrase, e.g. "helloworld" becomes "dlrowolleh"
    # I will use string slicing to flip the phrase
    # string[<start>:<stop>:<step>]
    # Idea: step=-1 tells python to move backwards through the string, from the end
    flippedCleanPhrase = cleanedPhrase[::-1]

    # If cleanedPhrase and flippedCleanPhrase are the same, we have a palindrome
    if (cleanedPhrase == flippedCleanPhrase):
        isPalindrome = True
    else:
        isPalindrome = False
    
    # Return the result from the decision if the phrase is a palindrom'e
    return isPalindrome