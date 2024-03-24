import json

def load_username(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)['username']
    except FileNotFoundError:
        return None

def save_username(filename, username):
    with open(filename, 'w') as file:
        json.dump({'username': username}, file)

def main():
    json_filename = 'username.json'
    username = load_username(json_filename)

    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What's your username? ")
        save_username(json_filename, username)
        print(f"Nice to meet you, {username}!")

if __name__ == "__main__":
    main()
