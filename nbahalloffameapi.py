import requests
from datetime import date

# Your API key
API_KEY = "c7512eb4-b681-4fe4-81b9-45bd83001e5b"
BASE_URL = "https://api.balldontlie.io"

# Set up headers with authentication
headers = {"Authorization": API_KEY}

# Get today's date
today = date.today().isoformat()

# Fetch today's NBA games
response = requests.get(
    f"{BASE_URL}/v1/players",
    headers=headers,
)

# Print the results
data = response.json()
print(data)



