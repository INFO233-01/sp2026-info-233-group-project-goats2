
#All this can do is look up a indivuduals players stats, we need to add code to make sure it will only accept strings.
#Also the part that can compare the two players and come to a results off of that.
#Still needs a second input to meet requirments.


import requests
#API pull from balldont lie
BASE_URL = "https://api.balldontlie.io/v1"
HEADERS = {"Authorization": "37301324-eadc-444d-bcfd-2cec693ee58a"}

def get(endpoint, params=None):
    return requests.get(BASE_URL + endpoint, headers=HEADERS, params=params).json()
#User enters types what player they want to see 
player_name = input("Player: ")


players = get("/players", {"search": player_name})["data"]

if players:
    player = players[0]
    print(f"{player['first_name']} {player['last_name']} - {player['team']['full_name']}")

    # Sets all stats to zero so the api can add to them accuratly
    games = points = rebounds = assists = fg_made = fg_attempted = 0

    # Uses range to see all stats from 2018 through 2025 and turns them into averages
    for year in range(2018, 2025):
        result = get("/season_averages", {"player_id": player["id"], "season": year})["data"]

        if result:
            stats = result[0]
            g = stats["games_played"]

            games += g
            points += stats["pts"] * g
            rebounds += stats["reb"] * g
            assists += stats["ast"] * g
            fg_made += stats["fgm"] * g
            fg_attempted += stats["fga"] * g

    # Print out all the stats 
    if games and fg_attempted:
        print(
            f"PPG: {points/games:.1f} | "
            f"RPG: {rebounds/games:.1f} | "
            f"APG: {assists/games:.1f} | "
            f"FG%: {(fg_made/fg_attempted)*100:.1f}"
        )
    else:
        print("No stats available")
else:
    print("No player found")
