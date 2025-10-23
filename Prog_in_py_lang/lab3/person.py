from dataclasses import dataclass, asdict
import json

@dataclass
class Person:
    first_name: str
    last_name: str
    address: str
    postal_code: str
    national_id: str

    def save_to_json(self, file_name: str):
        """Saves the person's data to a JSON file"""
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(asdict(self), file, ensure_ascii=False, indent=4)
        print(f"Data saved to file: {file_name}")

    @classmethod
    def load_from_json(cls, file_name: str):
        """Loads data from a JSON file and returns a Person object"""
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)
        return cls(**data)
