from flask import Flask, render_template, request, redirect
import jinja2
import os
import json
import difference
from fen import Board
import cv2

app = Flask(__name__)
step = 0

threshold_value = 1500

PREVIOUS = []
PREVIOUS_FEN = ""
REDDOTS = []

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
    return change_position_array

@app.route('/get_board')
def get_board():
    global PREVIOUS
    global PREVIOUS_FEN
    global REDDOTS
    frame = get_frame()
    cv2.imwrite('img12.png', frame)
    result = difference.get_difference(PREVIOUS,frame,REDDOTS)
    changes_positions = get_notation_difference(result)
    print(changes_positions)
    board = Board(PREVIOUS_FEN)
    board.apply_changes(changes_positions)
    new_fen = board.get_fen()
    
    #print(board.apply_changes(changes_positions))
    PREVIOUS_FEN = new_fen
    PREVIOUS = frame
    print(result)
    return json.dumps({"board": PREVIOUS_FEN})


@app.route('/init')
def init():
    global PREVIOUS
    global PREVIOUS_FEN
    global REDDOTS
    frame = get_frame()
    cv2.imwrite('img11.png', frame)
    PREVIOUS = frame
    REDDOTS = difference.reddots.CoordRedDots(frame)
    PREVIOUS_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    return json.dumps({"board": PREVIOUS_FEN})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='127.0.0.1', port=port,debug=True)
#     app.run(host='0.0.0.0', port=port,debug=True)
