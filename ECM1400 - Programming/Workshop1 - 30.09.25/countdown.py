# Program that aims to simulate the Countdown TV game show

# Function that reads the contents of the words.txt file into a list
def ReadFile():
    # Opens the file
    wordsFile = open("words.txt")
    # Reads all lines at once and returns a list of each line
    listOfWords = wordsFile.readlines()

    # Returns the list of words
    return listOfWords


# Generates the list of random characters the user will use to form the longest word possible
def RandomCharacterSelector():
    # List of all vowels
    listOfVowels = ['a','e','i','o','u']
    # List of all consonants
    listOfConsonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

    # Loop for user to input a sequence of 'c' or 'v' for a total of 9
    print("Enter either a 'c' or 'v':\n")
    for i in range(9):
        userInput = input("-> ")
        
