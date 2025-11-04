################################################
## This is my first python program using APIs ##
## It will use the News API                   ##
################################################

# Import the "requests" library so I can use APIs
import requests, json

# Read in the NewsAPI Key
with open('api-key.json', 'r') as f:
    data = json.load(f)
    api_key = data["News_API"]["API_Key"]

# Create the URl for the News API
url = "https://newsapi.org/v2/top-headlines"
params = {
    "sources":"bbc-news",
    "apiKey": api_key
}

# Send the request
response = requests.get(url, params=params)

# Check if the request was OK
if (response.status_code == 200):
    # Extract the data
    data = response.json()
    
    # Output the data
    for i in range(len(data["articles"])):
        print(data["articles"][i])