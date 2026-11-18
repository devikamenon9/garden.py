
import math
import time
import os

WIDTH = 100
HEIGHT = 36

PURPLE = "\033[95m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BROWN = "\033[33m"
RED = "\033[91m"
RESET = "\033[0m"

def put(grid, x, y, char):
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        grid[y][x] = char


def draw_line(grid, x, y1, y2, char="|"):
    for y in range(y1, min(y2, HEIGHT - 1) + 1):
        put(grid, x, y, char)


def lavender(grid, sprig, progress, sway):

    base_x = 25 + sprig * 7
    top_y = 3 + sprig % 3

    for y in range(top_y + 7, 33):

        t = (y - top_y) / (33 - top_y)

        x = round(
            base_x
            + math.sin(t * 1.5 + sprig * 0.5 + sway) * 1.5
        )

        if progress > y - top_y:
            put(grid, x, y, "|")

    buds = [
        (-2, 0), (2, 0),
        (-1, -1), (1, -1),
        (0, -2), (-1, 1), (1, 1)
    ]

    for level in range(6):

        if progress < level * 2:
            continue

        cy = top_y + level
        cx = round(
            base_x
            + math.sin(level * 0.35 + sprig * 0.5 + sway)
        )

        for dx, dy in buds:
            put(grid, cx + dx, cy + dy, "*")


def sunflower(grid, cx, cy, progress, sway):

    angles = list(range(0, 360, 30))

    shift = round(math.sin(sway + cx) * 1)

    for i, angle in enumerate(angles):

        if progress < i:
            continue

        rad = math.radians(angle)

        x = round(cx + shift + 5 * math.cos(rad))
        y = round(cy + 3 * math.sin(rad))

        put(grid, x, y, "o")

    for angle in range(0, 360, 45):

        if progress < 12:
            continue

        rad = math.radians(angle)

        x = round(cx + shift + 4 * math.cos(rad))
        y = round(cy + 2 * math.sin(rad))

        put(grid, x, y, "o")

    if progress >= 15:
        put(grid, cx + shift, cy, "@")
        put(grid, cx - 1 + shift, cy, "@")
        put(grid, cx + 1 + shift, cy, "@")

    if progress >= 5:

        for y in range(cy + 4, 33):
            put(grid, cx + shift, y, "|")

        put(grid, cx - 2 + shift, 23, "/")
        put(grid, cx + 2 + shift, 26, "\\")


def ixora(grid, cx, cy, progress, sway):

    for cluster in range(3):

        center_x = cx + (cluster - 1) * 3
        center_y = cy + cluster % 2

        for i, angle in enumerate(range(0, 360, 60)):

            if progress < cluster * 6 + i:
                continue

            rad = math.radians(angle)

            x = round(
                center_x + 2 * math.cos(rad)
                + math.sin(sway) * 0.5
            )

            y = round(center_y + 1.5 * math.sin(rad))

            put(grid, x, y, "*")

        if progress >= cluster * 6 + 6:
            put(grid, center_x, center_y, "+")

    if progress >= 5:

        for y in range(cy + 3, 33):
            put(grid, cx, y, "|")

        put(grid, cx - 2, cy + 6, "/")
        put(grid, cx + 2, cy + 8, "\\")


def display(grid):

    for row in grid:

        for char in row:

            if char == "*":
                print(PURPLE + char + RESET, end="")

            elif char == "o":
                print(YELLOW + char + RESET, end="")

            elif char == "@":
                print(BROWN + char + RESET, end="")

            elif char == "+":
                print(RED + char + RESET, end="")

            elif char in ["|", "/", "\\"]:
                print(GREEN + char + RESET, end="")

            else:
                print(char, end="")

        print()


def create_garden(frame):

    grid = [
        [" " for _ in range(WIDTH)]
        for _ in range(HEIGHT)
    ]

    sway = math.sin(frame * 0.25) * 0.5

    progress = min(frame, 25)

    sunflower(grid, 13, 8, progress, sway)
    sunflower(grid, 85, 8, progress, sway)

    ixora(grid, 8, 18, progress, sway)
    ixora(grid, 92, 18, progress, sway)

    for sprig in range(7):
        lavender(grid, sprig, progress, sway)

    print("\n")
    print("          M Y   L I T T L E   G A R D E N")
    print("                   ~ in bloom ~")
    print()

    display(grid)

    print("\n       Lavender  |  Sunflowers  |  Ixoras")
    print("                    Grown with love")


def main():

    frame = 0

    try:
        while True:

            os.system("clear")
            create_garden(frame)

            frame += 1

            time.sleep(0.15)

    except KeyboardInterrupt:
        print(RESET + "\n\nYour garden is resting. 💜")


main()
