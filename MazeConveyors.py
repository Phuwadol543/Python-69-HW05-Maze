def maze_solver_with_conveyors(maze: list[list[str]]) -> dict:
    
    S = []
    E = []
    
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if maze[x][y] == 'S':
                S += [x, y]
            if maze[x][y] == 'E':
                E += [x, y]
        if len(S) == 2 and len(E) == 2:
            break
    path_ = [S]
    count = 0
    p = S.copy()
    
    walks = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    
    con = {'>': [0, 1], '<': [0, -1], 'v': [1, 0], '^': [-1, 0]}
    
    while path_[-1] != E:
        moved = False
        for dr, dc in walks:
            n_r, n_c = p
            n_r += dr
            n_c += dc
            if n_r >= len(maze) or n_r < 0 or n_c >= len(maze[p[0]]) or n_c < 0:
                continue
            
            if maze[n_r][n_c] == '#':
                continue
            
            if maze[p[0]][p[1]] == "#":
                continue
            
            if [n_r, n_c] in path_:
                continue
            
            if maze[n_r][n_c] == ".":
                p = [n_r, n_c]
                path_.append(p)
                count += 1
                moved = True
                break
            
            elif maze[n_r][n_c] in con.keys():
                p = [n_r, n_c]
                path_.append(p)
                count += 1
                while maze[p[0]][p[1]] in con.keys():
                    con_p_r, con_p_c = con[maze[p[0]][p[1]]]
                    p = [p[0] + con_p_r, p[1] + con_p_c]
                    path_.append(p)
                moved = True
                break
            
            elif maze[n_r][n_c] == "E":
                p = [n_r, n_c]
                path_.append(p)
                count += 1
                moved = True
                break
            else:
                break
        
        if not moved:
            break
    
    result = {"distance": count, "path": path_}
    
    if path_[-1] != E:
        result["distance"] = -1
        result["path"] = []
        return result
    
    if path_[-1] == E:
        return result

if __name__ == "__main__":
    maze = [
        ['S', '.', '>', '>', 'E'],
        ['#', '#', '#', '#', '#']
    ]
    result = maze_solver_with_conveyors(maze)
    print(result)
    #Output: {'distance': 2, 'path': [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]}

    maze = [
        ['S', '.', '>', '#', 'E'],
        ['#', '#', '#', '#', '#']
    ]
    result = maze_solver_with_conveyors(maze)
    print(result)
    #Output: {"distance": -1, "path": []}


    maze = [
        ['S', '.', 'v', '.', 'E'],
        ['#', '#', 'v', '.', '#'],
        ['.', '.', 'v', '.', '.'],
        ['#', '#', '.', '.', '#'],
        ['.', '.', '.', '.', '.']
    ]
    result = maze_solver_with_conveyors(maze)
    print(result)
    #Output: {'distance': 7, 'path': [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [3, 2], [3, 3], [2, 3], [1, 3], [0, 3], [0, 4]]}
