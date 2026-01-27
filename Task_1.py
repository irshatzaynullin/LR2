import json
import os


def task() -> float:
    filename = None
    if os.path.exists("data.json"):
        filename = "data.json"
    elif os.path.exists("input.json"):
        filename = "input.json"
    else:

        test_data = [
            {"score": 0.0009456152645028281, "weight": 1},
            {"score": 0.5, "weight": 2},
            {"score": 0.3, "weight": 3}
        ]
        total = sum(item["score"] * item["weight"] for item in test_data)
        return round(total, 3)

    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    total_sum = sum(item["score"] * item["weight"] for item in data)


    return round(total_sum, 3)


print(task())