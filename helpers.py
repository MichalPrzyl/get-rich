import json
import os

def ensure_json_file_exists(file_path):
    if not os.path.exists(file_path):
        data = {
            "income_sources": [],
            "outcome_sources": [],
            "random_outcome_sources": [],
        }
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
