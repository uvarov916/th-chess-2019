import React from 'react';
import {Board} from "../Board/Board";
import './BoardController.css';
import {Chat} from "../Chat/Chat";
import {TimeController} from "../TimeController/TimeController";

export class BoardController extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            history: [
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
            ],
            index : 0
        };
        this.plusHistory=this.plusHistory.bind(this);
        this.minusHistory=this.minusHistory.bind(this);
    }

    plusHistory() {
        if (this.state.index < this.state.history.length - 1) {
            this.setState({ index : this.state.index + 1});
        }
    }
    minusHistory() {
        if (this.state.index > 0) {
            this.setState({ index : this.state.index - 1});
        }
    }

    render(){
        return (
            <div className='BorderController-all height-all'>
                <div className='distance-boardController-elements BoardController-time'>
                    <TimeController/>
                    </div>
                <div className='flex-board-center'>
                    <div className='justify-center margin-board'>
                        <Board
                        fen = {this.state.history[this.state.index]}
                        />
                    </div>
                    <div className='justify-center margin-board'>
                        <button className='BoardController-button' onClick={this.minusHistory}> Previous </button>
                        <button className='BoardController-button' onClick={this.plusHistory}> Next </button>
                    </div>
                </div>
                <div className='height-all distance-boardController-elements BorderController-chat'>
                    <Chat />
                </div>
            </div>
        );
    }
}
