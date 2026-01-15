import random
import os

WIDTH = 20
HEIGHT = 10

player = {"x": 1, "y": 1, "hp": 10, "gold": 0}
monster = {"x": random.randint(2, WIDTH-2), "y": random.randint(2, HEIGHT-2)}

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def draw():
    clear()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if x == player["x"] and y == player["y"]:
                print("🙂", end="")
            elif x == monster["x"] and y == monster["y"]:
                print("👾", end="")
            elif x == 0 or y == 0 or x == WIDTH-1 or y == HEIGHT-1:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print(f"❤️ HP: {player['hp']}   💰 Gold: {player['gold']}")
    print("Bewegen: W A S D | Q = Quit")

def move_monster():
    monster["x"] += random.choice([-1, 0, 1])
    monster["y"] += random.choice([-1, 0, 1])
    monster["x"] = max(1, min(WIDTH-2, monster["x"]))
    monster["y"] = max(1, min(HEIGHT-2, monster["y"]))

while True:
    draw()
    move = input("> ").lower()

    if move == "q":
        print("Spiel beendet 👋")
        break

    dx, dy = 0, 0
    if move == "w": dy = -1
    if move == "s": dy = 1
    if move == "a": dx = -1
    if move == "d": dx = 1

    player["x"] += dx
    player["y"] += dy

    if player["x"] == monster["x"] and player["y"] == monster["y"]:
        player["hp"] -= 1
        monster["x"] = random.randint(2, WIDTH-2)
        monster["y"] = random.randint(2, HEIGHT-2)
        print("👾 Monster hat dich getroffen!")

    if random.random() < 0.2:
        player["gold"] += 1

    move_monster()

    if player["hp"] <= 0:
        clear()
        print("💀 GAME OVER")
        print("Gesammeltes Gold:", player["gold"])
        break
