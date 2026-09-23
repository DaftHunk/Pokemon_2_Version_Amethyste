import os
import requests

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon?limit=2000"

def fetch_pokedex():
    print("Telechargement du Pokedex officiel (PokeAPI)...")

    try:
        response = requests.get(POKEAPI_URL, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Erreur reseau :", e)
        return {}

    data = response.json()

    pokedex = {}

    for entry in data["results"]:
        name = entry["name"].lower()
        # L'ID est à la fin de l'URL
        url = entry["url"]
        number = int(url.rstrip("/").split("/")[-1])
        pokedex[name] = number

    return pokedex


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pokedex = fetch_pokedex()

    if not pokedex:
        print("Impossible de recuperer le Pokedex.")
        return

    print(f"\nDossier analyse : {base_dir}\n")

    for folder in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder)

        if not os.path.isdir(folder_path):
            continue

        lower = folder.lower()

        # Ignore dejà numerote
        if len(folder) > 5 and folder[:4].isdigit() and folder[4] == "_":
            print(f"Ignore (dejà numerote) : {folder}")
            continue

        if lower in pokedex:
            number = pokedex[lower]
            new_name = f"{number:04d}_{lower}"
            new_path = os.path.join(base_dir, new_name)

            if os.path.exists(new_path):
                print(f"Conflit : {new_name} existe deja")
                continue

            os.rename(folder_path, new_path)
            print(f"Renomme : {folder} en {new_name}")
        else:
            print(f"Inconnu : {folder}")

    print("\nTermine.")


if __name__ == "__main__":
    main()