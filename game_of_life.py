# 1. Store the board state
# it's a 2dgrid
import random

DEAD = 0
ALIVE = 1

# board_state = [
#    [1, 1, 1, 1, 1, 1, 1, 1],  # 0
#    [1, 1, 1, 1, 1, 1, 1, 1],
#    [1, 1, 1, 1, 1, 1, 1, 1],
#    [1, 1, 0, 1, 1, 1, 1, 1],
#    [1, 1, 1, 1, 1, 1, 1, 1],
#    [1, 1, 1, 1, 1, 1, 1, 1]  # 5
# ]  # 0 to 7

# print(board_state[3][2])


def dead_state(dboard_width=8, dboard_height=6):
    xs = dboard_width
    ys = dboard_height
    xs0 = [0 for z in range(xs)]
    dead_board = [xs0 for r in range(ys)]
    #print(dead_board)
    pass

def random_state(board_width=8, board_height=6):
    state = dead_state(board_width, board_height)

    def state_width(state):
        # ???
        return len(state)
    for x in range(0, state_width(state)):
        for y in range(0, state_height(state)):
            rn = random.randrange(0, 2)
            if rn == 0:
                cell_state = 0
            else:
                cell_state = 1
                state[x][y] = cell_state

    return state




def state_height(state):
    state[y]
    return len(state[0])

# don't even ask, I just wanted to randomize parts in board_width
#    xs0 = [0 for z in range(board_width)]
#    k_random = random.randrange(1, board_width)
#    d = int(k_random)
#    w = random.sample(xs0, k=d)
#    smpl = [rn for d in w]
    tr = [0 for d in range(board_width)]

    def mutate(s=tr, num=board_height, target=rn):
        change_locs = random.sample(range(len(s)), num)
        new_sint = list(s)
        for change_loc in change_locs:
            new_sint[change_loc] = target
            new_s = str(new_sint)
            print(''.join(new_s))
    state_board = mutate()



#def render(state):
    #show_as = {
    #    DEAD: '*',
    #    ALIVE: '$'
    #}
    #lines = []
    #for y in  range(0, )

random_state(30, 20)
