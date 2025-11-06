################################################
## Program that performs a series of steps to ##
## obfuscate a peice of text                  ##
################################################

# Import the regular expressions module
import re

# Function that replaces a char in a string using an index
def replaceChar(text, newChar, index):
    # Convert string to a list of chars
    chars = list(text)

    # Replace char at index <index> with <newChar>
    chars[index] = newChar

    # Convert text back to a string
    text = "".join(chars)

    # Return result
    return text

# Define function to replace "the" with "and" and visa versa
def swapAndThe(text):
    # "\b" ensures words are replaced, not part of words
    # "re.IGNORECASE" replaces the word regardless of capitalisation

    # Replace all occurences of "the" with "ad"
    text = re.sub(r"\bthe\b", "ad", text, flags=re.IGNORECASE)

    # Replace all occurences of "and" with "the"
    text = re.sub(r"\band\b", "the", text, flags=re.IGNORECASE)

    # Replace all occurences of "ad" with "and"
    text = re.sub(r"\bad\b", "and", text, flags=re.IGNORECASE)

    # Return the modified text
    return text

# Define fucntion to make every third letter uppercase
def uppercase(text):
    # Loop through each character and make the third one uppercase
    for i in range(0, len(text), 3):
        try:
            # Try to change the char to uppercase
            text = replaceChar(text=text, newChar=text[i].upper(), index=i)
        except:
            # If failed, leave it
            # May fail if char is not a letter
            text = text
    
    # Return the modified text
    return text

# Function to reverse the letters in every fifth word
def reverseFifthWord(text):
    # Check if a space if present at the start
    if (text[0] == " "):
        spaceAtStart = True
    else:
        spaceAtStart = False
    
    # Split up the text into words
    segmentedText = text.split()

    # Loop through each fifth word, starting at the first fifth word
    for i in range(4,len(segmentedText),5):
        # Reverse the chars in the word
        segmentedText[i] = segmentedText[i][::-1]
    
    # Set text to a space if there was a space at the start
    if (spaceAtStart):
        text = " "
    else:
        text = ""
    
    # Join the words back together and put back in text
    text += " ".join(segmentedText)

    # Return the modifed text
    return text

# Function to apply a caeser cipher shift of key 1 to every other word
def applyCaeserShift(text):
    # Check if a space is present at the start
    if (text[0] == " "):
        spaceAtStart = True
    else:
        spaceAtStart = False
    
    # Split up the text into words
    segmentedText = text.split()

    # Loop through every other word, applying the caser cipher
    for i in range(1,len(segmentedText),2):
        # Store the current word
        word = segmentedText[i]

        # Loop through each letter in the word
        for j in range(len(word)):
            # Convert the char to ascii
            asciiLetter = ord(word[j])

            # Shift by 1
            asciiLetter += 1

            # Convert back to a char
            letter = chr(asciiLetter)

            # Replace the old letter with the new one
            word = replaceChar(text=word, newChar=letter, index=j)
        
        # Store the new word in the segmented text
        segmentedText[i] = word
    
    # If space at start, add this back
    if (spaceAtStart):
        text = " "
    else:
        text = ""
    
    # Join the segmented text back together and join onto text
    text += " ".join(segmentedText)
    
    # Return the modifed text
    return text


# Define the obfuscate function
def obfuscate(text):
    # Swap "the" with "and", and visa versa
    text = swapAndThe(text)

    # Take every thrid letter and make it uppercase
    text = uppercase(text)

    # Reverse the letters in every fifth word
    text = reverseFifthWord(text)

    # Apply a caeser shift, with key 1, to every other word
    text = applyCaeserShift(text)

    # Return the obfuscated text
    return text