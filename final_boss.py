def solve_maze(maze, start, end):

    rows = len(maze)
    cols = len(maze[0])


    visited = [[False] * cols for _ in range(rows)]

    path = []

    def is_valid(row, col):

        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False

        if maze[row][col] == '#':
            return False

        if visited[row][col]:
            return False

        return True

    def recursive_search(row, col):

        if (row, col) == end:
            path.append((row, col))
            return True


        if not is_valid(row, col):
            return False

        visited[row][col] = True


        path.append((row, col))

        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc


            if recursive_search(new_row, new_col):
                return True


        path.pop()
        return False


    start_row, start_col = start

    if recursive_search(start_row, start_col):
        return path
    else:
        return None



def print_maze_with_path(maze, path):

    maze_copy = [list(row) for row in maze]

    for i, (r, c) in enumerate(path):
        if i != 0 and i != len(path) - 1:
            maze_copy[r][c] = '*'

    for row in maze_copy:
        print(''.join(row))


def main():

    maze = [
        "########",
        "#s-----#",
        "#####--#",
        "#----#-#",
        "#-##-#-#",
        "#----#-#",
        "##-----#",
        "########"
    ]


    start = None
    end = None

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 's':
                start = (i, j)
            elif maze[i][j] == 'x':
                end = (i, j)

    print("Исходный лабиринт:")
    for row in maze:
        print(row)

    path = solve_maze(maze, start, end)

    if path:
        print(f"\nНайден путь длиной {len(path)} шагов:")
        print(f"Старт: {start}")
        print(f"Финиш: {end}")
        print(f"Полный путь: {path}")

        print("\nЛабиринт с отмеченным путем:")
        print_maze_with_path(maze, path)

        print("\nИнструкция по движению:")
        for i in range(1, len(path)):
            prev_r, prev_c = path[i - 1]
            curr_r, curr_c = path[i]

            if curr_r > prev_r:
                direction = "вниз"
            elif curr_r < prev_r:
                direction = "вверх"
            elif curr_c > prev_c:
                direction = "вправо"
            else:
                direction = "влево"

            print(f"Шаг {i}: с {path[i - 1]} на {path[i]} ({direction})")
    else:
        print("\nПуть не найден!")


if __name__ == "__main__":
    main()