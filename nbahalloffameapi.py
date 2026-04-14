import requests

url = "https://nbahalloffameapi.p.rapidapi.com/players"

headers = {
	"x-rapidapi-key": "44a02e71e6msh66d308a13d47d14p16def4jsnd48ba5109296",
	"x-rapidapi-host": "nbahalloffameapi.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

print(response.json())
