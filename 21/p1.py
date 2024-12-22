lines = open("21/i1").read().splitlines()
res = 0

keypad = {
    "A": (3, 2),
    0: (3, 1),
    1: (2, 0),
    2: (2, 1),
    3: (2, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (0, 0),
    8: (0, 1),
    9: (0, 2),
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

def get_moves(pad, rev_pad, seq):
    curr_pos = pad["A"]
    moves = []
    # can't move left up or down right for keypad, can't move up right or left down for controlpad
    for num in seq:
        target = pad[num]
        


for seq in lines:
    val = int(seq[:-1])
    curr_pos = keypad["A"]
    moves = 0

    for num in seq:

        kp_moves = abs(curr_pos[0] - keypad[num][0]) + abs(curr_pos[1] - keypad[num][1])



        


print(res)