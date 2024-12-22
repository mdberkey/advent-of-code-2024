import math

keypad_graph = {
    "A": (0, 3),
    0: ("A", 2),
    1: (2, 4),
    2: (0, 1, 3, 5),
    3: ("A", 2, 6),
    4: (1, 5, 7),
    5: (2, 4, 6, 8),
    6: (3, 5, 9),
    7: (4, 8),
    8: (5, 7, 9),
    9: (6, 8)
}

dir_graph = {
    "A": ("^", ">"),
    "^": ("v", "A"),
    ">": ("A", "v"),
    "v": ("^", ">", "<"),
    "<": ("v")
}

def get_shortest_paths(graph, seq):
    # do modified BFS to get shortest paths for the seq
    # get all paths
    pass

if __name__ == "__main__":
    lines = open("21/i0").read().splitlines()
    res = 0

    for seq in lines:
        val = int(seq[:-1])
        kp_paths = get_shortest_paths(keypad_graph, seq)
        first_dir_paths = []
        second_dir_paths = []

        for p in kp_paths:
            first_dir_paths.extend(get_shortest_paths(dir_graph, p))
       
        for p in first_dir_paths:
            second_dir_paths.extend(get_shortest_paths(dir_graph, p))
        
        min_p = min(len(p) for p in second_dir_paths)
        res += val * min_p

    print(res)