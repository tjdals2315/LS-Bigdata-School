# 딕셔너리 형태의 요소를 가지고 있는 리스트 
players = [
    {"name": "John", "height": 189},
    {"name": "Alice", "height": 175},
    {"name": "Bob", "height": 192},
    {"name": "Eva", "height": 170}
]

# height 콜백함수
def height(players):
    return players["height"]

print("shortest: ", min(players, key = height))
print("highest: ", max(players, key = height))