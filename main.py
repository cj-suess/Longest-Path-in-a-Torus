def dfs(curr_x, curr_y, torus, longest_path_dictionary):
    "depth first search with a dictionary mapping visited nodes and their longest paths"
    # if the current position is already in the dictionary then return that longest path
    if (curr_x, curr_y) in longest_path_dictionary:
        return longest_path_dictionary[(curr_x, curr_y)]
    # tuples representing moves that can be made and list for longest path
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    long_path = []
    # unpacks the tuples and assigns to new x,y values using modulus to stay in bounds
    for x_move, y_move in moves:
        new_x = (curr_x + x_move) % len(torus)
        new_y = (curr_y + y_move) % len(torus[0])
        # ensures that the new position is a valid move
        if torus[new_x][new_y] > torus[curr_x][curr_y]:
            current_path = dfs(new_x, new_y, torus, longest_path_dictionary)
            if len(current_path) > len(long_path):
                long_path = current_path
    # updates the dictionary with the coordinates and longest path
    longest_path_dictionary[(curr_x, curr_y)] = [(curr_x, curr_y)] + long_path
    return longest_path_dictionary[(curr_x, curr_y)]


def longest_path(torus):
    "calls dfs on each position in matrix"
    # checks for valid torus
    if torus is None or (len(torus) == 0) or (len(torus[0]) == 0):
        return []

    rows = len(torus)
    columns = len(torus[0])
    # dictionary to store longest paths to avoid redundant calculations
    longest_path_dictionary = {}
    # initiates the dfs for each position in torus and returns the longest path
    long_path = []
    for i in range(rows):
        for j in range(columns):
            path = dfs(i, j, torus, longest_path_dictionary)
            if len(path) > len(long_path):
                long_path = path
    # if the longest path found was never greater than or equal to 2 then return empty list
    if len(long_path) == 1:
        return []

    return long_path
