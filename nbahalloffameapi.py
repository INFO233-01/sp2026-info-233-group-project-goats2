import requests

API_KEY = "c7512eb4-b681-4fe4-81b9-45bd83001e5b"
BASE_URL = "https://api.balldontlie.io"

headers = {"Authorization": API_KEY}

# Get player stats for a specific game
response = requests.get(
    f"{BASE_URL}/nba/v1/stats",
    headers=headers,
    params={"game_ids[]": game_id}
)

data = response.json()
print(f"Player stats for game {game_id}:\n")


