def trail_dfs(graph, node, visited=None, count=0):
    def validate_next_node(graph, curr_node, next_node, visited):
        if next_node not in visited and 0 <= next_node[0] < len(graph) and 0 <= next_node[1] < len(graph[0]):
            if graph[next_node[0]][next_node[1]] - graph[curr_node[0]][curr_node[1]] == 1:
                return True
        return False

    curr_count = count
    if visited == None:
        visited = set()

    if node not in visited and 0 <= node[0] < len(graph) and 0 <= node[1] < len(graph[0]):
        visited.add(node) 
        if graph[node[0]][node[1]] == 9:
            curr_count += 1
        else:
            for next_node in [(node[0]-1, node[1]), (node[0]+1, node[1]), (node[0], node[1]-1), (node[0], node[1]+1)]:
                if validate_next_node(graph, node, next_node, visited):
                    curr_count += trail_dfs(graph, next_node, visited, count)

    return curr_count

if __name__ == "__main__":
    res = 0
    grid = [list(int(d) for d in l) for l in open("10/i1.txt").read().splitlines()]
    trailheads = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                trailheads.append((i, j))
    
    for th in trailheads:
        res += trail_dfs(grid, th)
    
    print(res)