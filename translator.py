import json
import os

def load_language(lang="en"):
    file_path = os.path.join("translations", f"{lang}.json")
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
