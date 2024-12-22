lines = open("21/i0").read().splitlines()
res = 0

keypad = {
    "A": (3, 2),
    "0": (3, 1),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
}

rev_keypad = {}
for k, v in keypad.items():
    rev_keypad[v] = k

dirpad = {
    ">": (1, 2),
    "v": (1, 1),
    "<": (1, 0),
    "^": (0, 1),
    "A": (0, 2)
}

DIR_MAP = {'U': (-1,0), 'D': (1,0), 'L': (0,-1), 'R': (0,1)}

rev_dirpad = {}
for k, v in dirpad.items():
    rev_dirpad[v] = k

def get_moves(pad, seq, is_keypad):
    curr_pos = pad["A"]
    moves = []
    # can't move left up or down right for keypad, can't move up right or left down for controlpad
    for k in seq:
        target = pad[k]
        vert = target[0] - curr_pos[0]
        hor = target[1] - curr_pos[1]

        if is_keypad:
           
           if hor > 0:
                moves.extend([">"] * abs(hor))
           if vert > 0:
                moves.extend(["v"] * abs(vert))
           if vert < 0:
                moves.extend(["^"] * abs(vert))
           if hor < 0:
                moves.extend(["<"] * abs(hor))
        else:
            if vert > 0:
                moves.extend(["v"] * abs(vert))
            if hor < 0:
                moves.extend(["<"] * abs(hor))
            if hor > 0:
                moves.extend([">"] * abs(hor))
            if vert < 0:
                moves.extend(["^"] * abs(vert))

        moves.append("A")
        curr_pos = target
    return moves
        
        
for seq in lines:
    val = int(seq[:-1])
    curr_pos = keypad["A"]
    moves = get_moves(keypad, seq, True)
    moves2 = get_moves(dirpad, moves, False)
    moves3 = get_moves(dirpad, moves2, False)
    print(len(moves3), val)
    res += val * len(moves3)

print(res)
