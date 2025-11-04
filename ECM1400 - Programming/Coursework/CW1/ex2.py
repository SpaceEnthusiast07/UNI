########################################################
## Program that takes a list of first and last names, ##
## along with a domain, and suggests an email         ##
## address for each name                              ##
########################################################

# Defining the email addresses function
def email_addresses(first, last, domain="@exeter.ac.uk"):
    # Declare a list to hold the emails
    emails = []
    
    # Loop through each name combination from first and last
    for i in range(len(first)):
        # Extract the first letter from the first name
        firstLetter = first[i][0]
        # Convert the first letter to lowercase
        firstLetter = firstLetter.lower()

        # Convert the last name to lowercase
        lastName = last[i].lower()

        # Construct the email
        email = f"{firstLetter}.{lastName}{domain}"

        # Add the email to the list of emails
        emails.append(email)
    
    # Return the list of emails
    return emails