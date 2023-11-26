# TODO решите задачу
import json

filename = "input.json"
def task() -> float:
    result = 0
    with open(filename) as file:
        data = json.load(file)
        for el in data:
            result += el["score"] * el["weight"]
    return round(result, 3)

print(task())
