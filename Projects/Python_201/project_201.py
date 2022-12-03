# 1. Ask for user input -> ditto/pikachu/bulbasaur
# 2. Create a dynamic URL based on step 1
# 3. Fetch the data from the URL in step 2
# 4. Convert JSON to a dictionary
# 5. Print out pokemon data

import requests

pokemon = input("Choose your favourite Pokemon: ")
pokemon = pokemon.lower()

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

req = requests.get(url)
if req.status_code == 200:
    data = req.json()
    
    print(f"Pokemon name is {data['name']}\n")
    x = 0
    y = 0
    for ability in data["abilities"]:
        x += 1
        print(f"{x}. Ability: {ability['ability']['name']}\n")
        print("List of pokemon with this ability:")
        req = requests.get(ability['ability']['url'])
        list = req.json()
        for poke in list['pokemon']:
            y += 1
            print(f"{y}. {poke['pokemon']['name']}")
        y = 0
        print("\n")
else:
    print("Pokemon does not exist! Try again.")
