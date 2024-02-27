# 람다로 변경
players = [
    {"name": "John", "height": 189},
    {"name": "Alice", "height": 175},
    {"name": "Bob", "height": 192},
    {"name": "Eva", "height": 170}
]

print(min(players, key = lambda x: x["height"]))
print(max(players, key = lambda x: x["height"]))