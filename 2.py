# 1. Store the board state
# it's a 2dgrid
import random


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
    print(dead_board)


def random_state(board_width=8, board_height=6):
    state = dead_state(board_width, board_height)
    for x in range(0, state_width(state)):
        for y in range(0, state_height(state)):
            rn = random.randrange(0, 2)
            if rn == 0:
                cell_state = 0
            else:
                cell_state = 1
            state[x][y] = cell_state

    return state


def state_width(state):
    """Get the width of a state.
    Parameters
    ----------
    state: a Game state
    Returns
    -------
    The width of the input state
    """
    return len(state)


def state_height(state):
    """Get the height of a state.
    Parameters
    ----------
    state: a Game state
    Returns
    -------
    The height of the input state
    """
    return len(state[0])


state_width(dead_state)
