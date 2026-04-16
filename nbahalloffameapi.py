import requests
from datetime import date

# Your API key
API_KEY = "37301324-eadc-444d-bcfd-2cec693ee58a"
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
data = response.json()

for player in data["data"]:
    print(f"Name: {player['first_name']} {player['last_name']}")
    print(f"Position: {player['position']}")
    print(f"Team: {player['team']['full_name']}")
    print("-" * 30)
    
    response = requests.get(
    f"{BASE_URL}/v1/stats",
    headers=headers,
    params={"per_page": 10}
)

data = response.json()

for stat in data["data"]:
    player = stat["player"]
    
    print(f"{player['first_name']} {player['last_name']}")
    print(f"Points: {stat['pts']}")
    print(f"Rebounds: {stat['reb']}")
    print(f"Assists: {stat['ast']}")
    print("-" * 30)
    player_name = input("Enter player name: ").lower()

for stat in data["data"]:
    player = stat["player"]
    full_name = f"{player['first_name']} {player['last_name']}".lower()
    
    if player_name in full_name:
        print(f"{full_name.title()}")
        print(f"Points: {stat['pts']}")
        print(f"Rebounds: {stat['reb']}")
        print(f"Assists: {stat['ast']}")



