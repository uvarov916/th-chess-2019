import React from 'react';
import {Board} from "../Board/Board";
import './BoardController.css';
import {Chat} from "../Chat/Chat";
import {TimeController} from "../TimeController/TimeController";
import {init, getBoard} from '../Services/BoardService.js';
import {help, helpStart, helpEnd} from "../Services/HelpService";

export class BoardController extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            history: [
                'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1',
            ],
            messages:[],
            index : 0,
            listening: false,
            possibleMoves: []
        };
        this.answering = false;
        this.speaking = false;
        this.plusHistory=this.plusHistory.bind(this);
        this.minusHistory=this.minusHistory.bind(this);
        this.initGame=this.initGame.bind(this);
        this.whiteMoveEnd=this.whiteMoveEnd.bind(this);
        this.whiteMoveStart=this.whiteMoveStart.bind(this);
        this.analyzeText = this.analyzeText.bind(this);
        this.startListen = this.startListen.bind(this);
        this.stopListen = this.stopListen.bind(this);
        this.addMessageToChat = this.addMessageToChat.bind(this);
        this.speakWords = this.speakWords.bind(this);
    }

    addMessageToChat(text, user) {
        if (text) {
            this.setState({messages:[...this.state.messages, {
                "user": user, 
                "text" : text}]
            });
        }
    }

    speakWords(text) {
        window.speakWords(text);
        this.speaking = true;
        this.stopListen();
        setTimeout(() => {
            this.speaking = false;
            // if (this.shouldBeListening) {
            //     this.startListen();
            // }
        }, 4000)
    }

    startListen() {
        window.startListen(this.analyzeText);
        this.setState({ listening: true });
        console.log('Listening...')
    }

    stopListen() {
        window.stopListen();
        this.setState({ listening: false });
        console.log('Stopped listening.')
    }

    analyzeText(text) {
        if (!this.answering && !this.speaking) {
            this.answering = true;
            console.log('New words: ' + text);
            this.addMessageToChat(text, true);
            // this.stopListen();
            help(this.state.history[this.state.index], text).then((answerData) => {
                console.log('New answer ', answerData);
                this.addMessageToChat(answerData.answer, false);
                this.answering = false;
                this.speakWords(answerData.answer);
                this.setState({'possibleMoves': answerData.possibleMoves || []});
            });
        }
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

    initGame() {
        init().then((data)=>{
            this.setState({
                index: 0,
                history: [data.board]
            });
            console.log('new board: ' + data.board);

            // this.shouldBeListening = true;
            // this.startListen();
        });
    }

    whiteMoveStart() {
        getBoard().then((data)=>{
            this.state.history.push(data.board);
            this.setState({
                index: this.state.history.length - 1,
            });
            console.log('new board: ' + data.board);
            this.answering = true;
            helpStart(data.board).then((answerData)=> {
                console.log(answerData);
                this.addMessageToChat(answerData.answer, false);
                this.answering = false;
                this.speakWords(answerData.answer);
                this.setState({'possibleMoves': []});
                // this.shouldBeListening = true;
                // this.startListen();
            })
        });
    }

    whiteMoveEnd() {
        getBoard().then((data)=>{
            // this.stopListen();
            // this.shouldBeListening = false;

            this.state.history.push(data.board);
            this.setState({
                index: this.state.history.length - 1,
            });
            console.log('new board: ' + data.board);
            this.answering = true;
            helpEnd(data.board).then((answerData)=>{
                console.log(answerData);
                this.addMessageToChat(answerData.answer, false);
                this.answering = false;
                this.speakWords(answerData.answer);
                this.setState({'possibleMoves': []});
            })
        });
    }

    render(){
        return (
            <div className='BorderController-all height-all'>
                <div className='distance-boardController-elements BoardController-time'>
                    <TimeController
                        initCallback={this.initGame}
                        whiteMoveEndCallback={this.whiteMoveEnd}
                        whiteMoveStartCallback={this.whiteMoveStart}
                    />
                </div>
                <div className='flex-board-center'>
                    <div className='justify-center margin-board'>
                        <Board
                            fen = {this.state.history[this.state.index]}
                            possibleMoves={this.state.possibleMoves}
                        />
                    </div>
                    <div className='justify-center margin-board'>
                        <button className='BoardController-button' onClick={this.minusHistory}> Previous </button>
                        <button className='BoardController-button' onClick={this.plusHistory}> Next </button>
                    </div>
                </div>
                <div className='height-all distance-boardController-elements BorderController-chat'>
                    <Chat 
                        messages={this.state.messages}
                        listening={this.state.listening}
                    />
                </div>
            </div>
        );
    }

    componentDidMount() {
        document.addEventListener('keydown', (event) => {
            if (event.keyCode === 13) {
                if (!this.state.listening) {
                    this.startListen();
                } else {
                    this.stopListen();
                }
                
            }
        });
    }
}
