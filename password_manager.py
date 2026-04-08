import json
import os

VAULT_FILE = "vault.json"


def load_vault():
    if not os.path.exists(VAULT_FILE):
        return []

    with open(VAULT_FILE, "r") as file:
        return json.load(file)


def save_vault(vault):
    with open(VAULT_FILE, "w") as file:
        json.dump(vault, file, indent=4)


def add_credential(vault):
    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")

    vault.append({
        "website": website,
        "username": username,
        "password": password
    })

    save_vault(vault)
    print("Credential saved!")


def view_credentials(vault):
    if len(vault) == 0:
        print("No credentials saved yet.")
        return

    for item in vault:
        print(f"Website: {item['website']}")
        print(f"Username: {item['username']}")
        print(f"Password: {item['password']}")
        print("-" * 20)
        
        
def search_credentials(vault):
    website_search = input("Search website: ").lower()

    found = False

    for item in vault:
        if item["website"].lower() == website_search:
            print(f"Website: {item['website']}")
            print(f"Username: {item['username']}")
            print(f"Password: {item['password']}")
            found = True
            break

    if not found:
        print("No credential found for that website.")


def main():
    vault = load_vault()

    while True:
        print("\n--- PASSWORD MANAGER ---")
        print("1 - Add Credential")
        print("2 - View Credentials")
        print("3 - Search Credential")
        print("4 - Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_credential(vault)
        elif choice == "2":
            view_credentials(vault)
        elif choice == "3":
            search_credentials(vault)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()