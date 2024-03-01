players = [
    {"name": "John", "height": 189},
    {"name": "Alice", "height": 175},
    {"name": "Bob", "height": 192},
    {"name": "Eva", "height": 170}
]

# 콜백 함수의 매개변수 이름은 딕셔너리 이름과 같지 않아도 됨 (players != i)
def height(i):
    return i["height"]

print("shortest: ", min(players, key = height))
print("highest: ", max(players, key = height))