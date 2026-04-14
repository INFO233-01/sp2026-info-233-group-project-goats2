import requests
import json

url = "https://free-nba.p.rapidapi.com/players"

querystring = {"page":"0","per_page":"25"}

headers = {
	"x-rapidapi-key": "44a02e71e6msh66d308a13d47d14p16def4jsnd48ba5109296",
	"x-rapidapi-host": "free-nba.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
def get_player_stats(player_name):
	pass
try:
	response=request.get(API_URL, params=("search":name))
	data=response.json()

user_players = input("Please enter the Name of a two NBA Hall of Famers and I will compare them based off their stats.")


import random 
