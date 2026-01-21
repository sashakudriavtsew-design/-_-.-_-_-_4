import json


def task() -> float:
    json_data = '''
    [
        {"score": 0.001, "weight": 1},
        {"score": 0.5, "weight": 2},
        {"score": 0.295, "weight": 1},
        {"score": 0.3, "weight": 3},
        {"score": 0.1, "weight": 1}
    ]
    '''

    data = json.loads(json_data)
    total = sum(item["score"] * item["weight"] for item in data)
    return round(total, 3)


print(task())