from flask import Flask, render_template, request, redirect
from flask_cors import CORS
import jinja2
import os
import json
import difference
from fen import Board
import cv2

import chess

app = Flask(__name__)
CORS(app)
step = 0

threshold_value = 1500 #950

PREVIOUS = []
PREVIOUS_FEN = ""
REDDOTS = []

DEMO_STEP = 0
DEMO_STATUS = False
demo_states = [
        'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1',
        'rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1',
        'rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR w KQkq e6 0 2',
        'rnbqkbnr/pppp1ppp/8/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2',
        'r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 3',
        'r1bqkbnr/pppp1ppp/2n5/4p3/4P3/2N2N2/PPPP1PPP/R1BQKB1R b KQkq - 3 3',
        'r1bqkb1r/pppp1ppp/2n2n2/4p3/4P3/2N2N2/PPPP1PPP/R1BQKB1R w KQkq - 4 4',
        'r1bqkb1r/pppp1ppp/2n2n2/4p3/4P3/P1N2N2/1PPP1PPP/R1BQKB1R b KQkq - 0 4',
        'r1bqkb1r/ppp2ppp/2n2n2/3pp3/4P3/P1N2N2/1PPP1PPP/R1BQKB1R w KQkq d6 0 5',
        'r1bqkb1r/ppp2ppp/2n2n2/3Pp3/8/P1N2N2/1PPP1PPP/R1BQKB1R b KQkq - 0 5',
        'r1bqkb1r/ppp2ppp/2n5/3np3/8/P1N2N2/1PPP1PPP/R1BQKB1R w KQkq - 0 6',
        'r1bqkb1r/ppp2ppp/2n5/3np3/8/P1N2N2/1PPPBPPP/R1BQK2R b KQkq - 1 6',
        'r1bqkb1r/ppp2ppp/2n5/3n4/4p3/P1N2N2/1PPPBPPP/R1BQK2R w KQkq - 0 7',
        'r1bqkb1r/ppp2ppp/2n5/3n4/4N3/P4N2/1PPPBPPP/R1BQK2R b KQkq - 0 7',
        'r1bqkb1r/ppp2ppp/2n5/8/4Nn2/P4N2/1PPPBPPP/R1BQK2R w KQkq - 1 8',
        'r1bqkb1r/ppp2ppp/2n5/8/4Nn2/P4N2/1PPPBPPP/R1BQ1RK1 b kq - 2 8',
        'r1bqkb1r/ppp2ppp/2n5/8/4N3/P4N2/1PPPnPPP/R1BQ1RK1 w kq - 0 9',
        'r1bqkb1r/ppp2ppp/2n5/8/4N3/P4N2/1PPPQPPP/R1B2RK1 b kq - 0 9',
        'r2qkb1r/ppp2ppp/2n5/8/4N1b1/P4N2/1PPPQPPP/R1B2RK1 w kq - 1 10',
        'r2qkb1r/ppp2ppp/2n2N2/8/6b1/P4N2/1PPPQPPP/R1B2RK1 b kq - 2 10'
]

def get_frame():
    camera = cv2.VideoCapture(0)
    frame = camera.read()[1]
    camera.release()
    return frame
#condition 

#def test() :

def get_notation_difference(changes):
    change_position_array = []
    for x in range(8):
        for y in range(8):
            if (changes[x][y] > threshold_value):
                change_position_array.append([x,y])

    # Find 2 maxes
    temp = changes.copy()
    max_change_positions = []
    max_val = -1
    max_idx = [-1,-1]
    for x in range(8):
        for y in range(8):
            if (temp[x][y] > max_val):
                max_val = temp[x][y]
                max_idx = [x,y]

    max_change_positions.append(max_idx)
    temp[max_idx[0]][max_idx[1]] = -1
    max_val = -1
    max_idx = [-1,-1]
    for x in range(8):
        for y in range(8):
            if (temp[x][y] > max_val):
                max_val = temp[x][y]
                max_idx = [x,y]

    max_change_positions.append(max_idx)
    
    if (len(change_position_array) == 4):
        line_num = change_position_array[0][0]
        if not (line_num == 0 or line_num == 7):
            return max_change_positions
        else:
            for change in change_position_array:
                if change[0] != line_num:
                    return max_change_positions
            return change_position_array
    else:
        return max_change_positions

@app.route('/get_board')
def get_board():
    global demo_states
    global PREVIOUS
    global PREVIOUS_FEN
    global REDDOTS
    global DEMO_STEP
    global DEMO_STATUS

    if (DEMO_STATUS == False):
        frame = get_frame()
        # cv2.imwrite('img12.png', frame)
        result = difference.get_difference(PREVIOUS,frame,REDDOTS)
        changes_positions = get_notation_difference(result)
        # print(changes_positions)
        board = Board(PREVIOUS_FEN)
        print("difference", result)
        print("changes", changes_positions)
        board.apply_changes(changes_positions)
        new_fen = board.get_fen()
        PREVIOUS_FEN = new_fen
        PREVIOUS = frame
        return json.dumps({"board": PREVIOUS_FEN})
    else:
        DEMO_STEP = DEMO_STEP + 1
        # print(result)
        # print(PREVIOUS_FEN)
        # print(chess.Board(PREVIOUS_FEN))
        if (DEMO_STEP < len(demo_states)):
            return json.dumps({"board": demo_states[DEMO_STEP]})
        else:
            return json.dumps({"board": demo_states[len(demo_states)-1]})


@app.route('/init')
def init():
    global PREVIOUS
    global PREVIOUS_FEN
    global REDDOTS
    global DEMO_STATUS
    DEMO_STATUS = False
    frame = get_frame()
    # cv2.imwrite('img11.png', frame)
    PREVIOUS = frame
    REDDOTS = difference.reddots.CoordRedDots(frame)
    PREVIOUS_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    return json.dumps({"board": PREVIOUS_FEN})

@app.route('/mocinit')
def mocinit():
    global PREVIOUS_FEN
    global DEMO_STATUS
    global DEMO_STEP
    DEMO_STEP = 0
    DEMO_STATUS = True
    PREVIOUS_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    return json.dumps({"board": PREVIOUS_FEN})

@app.route('/swap', methods=['POST'])
def swap():
    global PREVIOUS_FEN
    json_req = request.get_json()
    swap_cells = json_req["cells"]
    board = Board(PREVIOUS_FEN)
    if (len(swap_cells) == 2):
        board.swap_cells(swap_cells[0], swap_cells[1])
    new_fen = board.get_fen()
    PREVIOUS_FEN = new_fen
    return json.dumps({"board": PREVIOUS_FEN})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    # app.run(host='127.0.0.1', port=port,debug=True)
    app.run(host='0.0.0.0', port=port,debug=True)
