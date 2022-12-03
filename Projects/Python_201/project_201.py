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
data = req.json()

print(f"Pokemon name is {data['name']}")
print("Abilities:")

for ability in data["abilities"]:
    print(ability['ability']['name'])
    print("List of pokemon with this ability:")
    req = requests.get(ability['ability']['url'])
    list = req.json()
    for poke in list['pokemon']:
        print(poke['pokemon']['name'])
    print("\n")