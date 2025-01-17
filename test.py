def move(player_position, x, y):
    new_player_position = player_position[:]
    new_player_position[0] += x
    new_player_position[1] += y
    if 0 <= new_player_position[0] <= 8 and 0 <= new_player_position[1] <= 8:
        maze[player_position[0]][player_position[1]] = " . "
        maze[new_player_position[0]][new_player_position[1]] = " x "
        return new_player_position
    else:
        return player_position


maze = [
    [" . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . "],
    [" . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . "],
    [" . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . "],
    [" . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . "],
    [" . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . "],
    [" . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . "],
    [" . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . "],
    [" . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . "],
    [" . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . "],
]

player_position = [4, 4]
maze[player_position[0]][player_position[1]] = " x "

while True:
    for row in maze:
        for space in row:
            print(space, end="")
        print()
    print(player_position)
    player_move = input("Enter w, a, s, d, or x: ")
    match player_move:
        case "x":
            break
        case "w":
            player_position = move(player_position, -1, 0)
        case "s":
            player_position = move(player_position, 1, 0)
        case "a":
            player_position = move(player_position, 0, -1)
        case "d":
            player_position = move(player_position, 0, 1)
