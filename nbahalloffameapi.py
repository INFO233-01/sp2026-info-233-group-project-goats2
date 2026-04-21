
#All this can do is look up a indivuduals players stats, we need to add code to make sure it will only accept strings.
#Also the part that can compare the two players and come to a results off of that.
#Still needs a second input to meet requirments.

import requests
import webbrowser

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/120.0.0.0',
}


BASE_URL = "https://api.balldontlie.io/v1"
HEADERS = {"Authorization": "37301324-eadc-444d-bcfd-2cec693ee58a"}

def get(endpoint, params=None):
    return requests.get(BASE_URL + endpoint, headers=HEADERS, params=params).json()


# Function to get player stats using get player stats
def get_player_stats(player_name):
    players = get("/players", {"search": player_name})["data"]

    if not players:
        return None

    player = players[0]

    games = points = rebounds = assists = fg_made = fg_attempted = 0

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

    if games and fg_attempted:
        return {
            "name": f"{player['first_name']} {player['last_name']}",
            "team": player["team"]["full_name"],
            "ppg": points / games,
            "rpg": rebounds / games,
            "apg": assists / games,
            "fg": (fg_made / fg_attempted) * 100
        }
    else:
        return None


# Function to compare players
def compare_players(p1, p2):
    score1 = 0
    score2 = 0

    print("\n--- Comparison ---")

    # Compare each stat
    if p1["ppg"] > p2["ppg"]:
        score1 += 1
    else:
        score2 += 1

    if p1["rpg"] > p2["rpg"]:
        score1 += 1
    else:
        score2 += 1

    if p1["apg"] > p2["apg"]:
        score1 += 1
    else:
        score2 += 1

    if p1["fg"] > p2["fg"]:
        score1 += 1
    else:
        score2 += 1

    # Print player stats
    print(f"\n{p1['name']} ({p1['team']})")
    print(f"PPG: {p1['ppg']:.1f} | RPG: {p1['rpg']:.1f} | APG: {p1['apg']:.1f} | FG%: {p1['fg']:.1f}")

    print(f"\n{p2['name']} ({p2['team']})")
    print(f"PPG: {p2['ppg']:.1f} | RPG: {p2['rpg']:.1f} | APG: {p2['apg']:.1f} | FG%: {p2['fg']:.1f}")

    # Decide the winner
    print("\n--- Result ---")
    if score1 > score2:
        print(f"{p1['name']} would win based on stats")
        response_image = requests.get(f"https://4get.lunar.icu/api/v1/images?s={p1}", headers=headers)
        json_image = response_image.json()
        url_image = json_image["image"][0]["source"][0]["url"]
        webbrowser.open(url_image)
    elif score2 > score1:
        print(f"{p2['name']} would win based on stats")
        response_image = requests.get(f"https://4get.lunar.icu/api/v1/images?s={p2}", headers=headers)
        json_image = response_image.json()
        url_image = json_image["image"][0]["source"][0]["url"]
        webbrowser.open(url_image)
    else:
        print("It's a tie!")


#  Main code for comparison 
player1_name = input("Enter Player 1: ")
player2_name = input("Enter Player 2: ")

p1 = get_player_stats(player1_name)
p2 = get_player_stats(player2_name)

if p1 and p2:
    compare_players(p1, p2)
else:
    print("One or both players not found.")

