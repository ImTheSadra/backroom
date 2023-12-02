import json as pickle

class DB:
    path = "./data.json"
    data:dict = {}
    def __init__(self) -> None:
        self.load()

    def load(self):
        with open(self.path, "rb") as f:
            self.data = pickle.load(f)

    def save(self):
        with open(self.path, "wb") as f:
            pickle.dump(self.data, f)