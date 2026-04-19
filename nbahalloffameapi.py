
#All this can do is look up a indivuduals players stats, we need to add code to make sure it will only accept strings.
#Also the part that can compare the two players and come to a results off of that.
#Still needs a second input to meet requirments.


import requests
#API pull from balldontlie
BASE_URL = "https://api.balldontlie.io/v1"
HEADERS = {"Authorization": "37301324-eadc-444d-bcfd-2cec693ee58a"}

def get_player_stats(player_name):

    players = get("/players", {"search": player_name})["data"]

    if not players:
        print(f"No player found for {player_name}")
        return None, None

    player = players[0]
    print(f"\n{player['first_name']} {player['last_name']} - {player['team']['full_name']}")

    games = points = rebounds = assists = fg_made = fg_attempted = 0

    # loop through seasons
    for year in range(2018, 2025):
        result = get("/season_averages", {
            "player_ids[]": player["id"],
            "season": year
        })["data"]

        if result:
            stats = result[0]
            g = stats["games_played"]

            games += g
            points += stats["pts"] * g
            rebounds += stats["reb"] * g
            assists += stats["ast"] * g
            fg_made += stats["fgm"] * g
            fg_attempted += stats["fga"] * g

    if games and fg_attempted:
        stats_dict = {
            "ppg": round(points / games, 1),
            "rpg": round(rebounds / games, 1),
            "apg": round(assists / games, 1),
            "fg_pct": round((fg_made / fg_attempted) * 100, 1)
        }

        print(
            f"PPG: {stats_dict['ppg']} | "
            f"RPG: {stats_dict['rpg']} | "
            f"APG: {stats_dict['apg']} | "
            f"FG%: {stats_dict['fg_pct']}"
        )

        return player_name, stats_dict

    else:
        print("No statitics available")
        return None,None 

       
