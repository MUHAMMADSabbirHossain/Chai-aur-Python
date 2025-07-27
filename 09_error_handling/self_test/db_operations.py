# internal modules
import json

def save_data(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)

def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    except Exception as error:
        print("❌ ", error)
        return []
 