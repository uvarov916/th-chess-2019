def init_board(fen):
    board = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'], 
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], 
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], 
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
    state = fen.split(' ')
    states = state[0].split('/')
    for row in range(8):
        column = list(states[row])
        j = 0
        for grid in column:
            if (grid >='A' and grid <= 'Z') or (grid >='a' and grid <= 'z'):
                board[row][j] = grid
                j += 1
            else:
                for i in range(int(grid)):
                    board[row][j] = None
                    j += 1
    return board



print(init_board('bqkbnrrn/pppppppp/8/8/3P4/8/PPP1PPPP/BQKBNRRN w KQkq - 0 1'))