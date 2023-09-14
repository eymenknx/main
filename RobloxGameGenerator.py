from bs4 import BeautifulSoup
import requests
import random
import json

error = True

minimumVisits = 1000 # Change to desired visits

while error:

    id = str(random.randint(1,12633075485))
    url = "https://www.roblox.com/games/" + id

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    elements_with_data_universe_id = soup.find_all(attrs={"data-universe-id": True})


    printed_ids = set()

    for element in elements_with_data_universe_id:
        data_universe_id = element.get("data-universe-id")
        getinfo = "https://games.roblox.com/v1/games?universeIds="+data_universe_id
        response2 = requests.get(getinfo)
        json_data = json.loads(response2.text)
        visits = json_data["data"][0]["visits"]
        if data_universe_id not in printed_ids:
            if visits >= minimumVisits:
                print("Game has been found! "+url+" and has "+str(visits)+" visits.")
                printed_ids.add(data_universe_id)
                error = False
        else:
            if visits >= minimumVisits:
                pass
            else:
                print(url+" is missing "+str(minimumVisits-visits)+" visits.")
    if error:
        print(url+" could not be found.")