def find_connected_areas(row: int, col: int, matrix: list) -> int:
    # recursive base case
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return 0
    if matrix[row][col] == "-":
        return 0
    # we set the current position to "-" so we dont search for it again
    matrix[row][col] = "-"
    result = 1
    result += find_connected_areas(row + 1, col, matrix)
    result += find_connected_areas(row - 1, col, matrix)
    result += find_connected_areas(row, col + 1, matrix)
    result += find_connected_areas(row, col - 1, matrix)
    return  result


maze = [[el for el in input()] for _ in range(int(input()))]
result = 0
for row in range(len(maze)):
    for col in range(len(maze[0])):
        if maze[row][col] == ".":
            connected_area = find_connected_areas(row, col, maze)
            if connected_area > result:
                result = connected_area
print(connected_area)
# visualise maze
# for row in maze:
#     print(*row, sep=" ")
