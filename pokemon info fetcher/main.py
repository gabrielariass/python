import requests

BASE_URL = "https://pokeapi.co/api/v2/"
FILE_PATH = "stuff/pokemon.txt"


def get_pokemon_info(name):
    url = f"{BASE_URL}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    print(f"Failed to retrieve data: {response.status_code}")
    return None


def main():
    pokemon_name = input("Enter a Pokémon name: ").lower()

    pokemon_info = get_pokemon_info(pokemon_name)

    if pokemon_info:
        file_data = (
            f"Name:       {pokemon_info['name']}\n"
            f"ID:         {pokemon_info['id']}\n"
            f"Height:     {pokemon_info['height']}\n"
            f"Weight:     {pokemon_info['weight']}\n\n"
        )

        with open(FILE_PATH, "a") as file:
            file.write(file_data)

        print(f"Data written successfully for {pokemon_name}")


if __name__ == "__main__":
    main()
