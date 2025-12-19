def find_ship(board):

    visited = set()
    ship_coords = []
    rows = len(board)
    cols = len(board[0])

    def dfs(x, y):

        if x < 0 or x >= rows or y < 0 or y >= cols:
            return

        if (x,y) in visited:
            return
        
        visited.add((x, y))

        if board[x][y] == 1:
            ship_coords.append((x, y))
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)

    for x in range(rows):
        for y in range(cols):

            if board[x][y] == 1:
                dfs(x, y)

    return ship_coords


# Example usage:
if __name__ == '__main__':
    board = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1]
    ]
    
    ship = find_ship(board)
    if ship:
        print("Ship found at coordinates:")
        for coord in ship:
            print(coord)
    else:
        print("No ship found on the board.")