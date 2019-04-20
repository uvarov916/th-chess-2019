from flask import Flask, render_template, request, redirect
import jinja2
import os
import json
import difference
import cv2

app = Flask(__name__)
step = 0

threshold_value = 1500

PREVIOUS = []
REDDOTS = []

def get_notation_difference(changes):
    change_position_array = []
    changes.reverse()
    for x in range(8):
        for y in range(8):
            if (changes[x][y] > threshold_value):
                change_position_array.append([x,y])
    return change_position_array

@app.route('/get_board')
def get_board():
    global PREVIOUS
    cap = cv2.VideoCapture(1)
    frame = cap.read()[1]
    cap.release()
    result = difference.get_difference(PREVIOUS,frame,REDDOTS)
    changes_positions = get_notation_difference(result)
    print(changes_positions)
    PREVIOUS = frame
    return json.dumps(result)


@app.route('/init')
def init():
    global PREVIOUS
    global REDDOTS
    cap = cv2.VideoCapture(1)
    frame = cap.read()[1]
    cap.release()
    PREVIOUS = frame
    REDDOTS = difference.reddots.CoordRedDots(frame)
    return json.dumps({"board": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='127.0.0.1', port=port,debug=True)
#     app.run(host='0.0.0.0', port=port,debug=True)
