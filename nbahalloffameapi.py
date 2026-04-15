import requests

API_KEY = "your-api-key"
BASE_URL = "https://api.balldontlie.io"

headers = {"Authorization": API_KEY}

# Get player stats for a specific game
game_id = 18447166  # NYK vs ORL game
response = requests.get(
    f"{BASE_URL}/nba/v1/stats",
    headers=headers,
    params={"game_ids[]": game_id}
)

data = response.json()
print(f"Player stats for game {game_id}:\n")

# Sort by points and show top performers
players = sorted(data["data"], key=lambda x: x["pts"], reverse=True)
for stat in players[:5]:
    player = stat["player"]
    team = stat["team"]["abbreviation"]
    print(f"{player['first_name']} {player['last_name']} ({team}): "
          f"{stat['pts']} pts, {stat['reb']} reb, {stat['ast']} ast")

