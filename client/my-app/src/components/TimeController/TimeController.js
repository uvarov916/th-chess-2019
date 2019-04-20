import React, { Component } from 'react';
import './TimeController.css';
import {TimeView} from './TimeView'
import {getBoard} from "../services/BoardService";

export class TimeController extends Component {
    constructor(props) {
        super(props);
        this.state = {whiteTime : 0, blackTime : 0, turn : null};
    }

    render() {
        return (
            <div className="time-controller">
                <div className="timer-back">
                    <div className="timer-pad">
                        <div className={(this.state.turn===false ? 'timer-active' : '') + " timer-black app-timer"}>
                            <TimeView time={this.state.blackTime}/>
                        </div>
                    </div>
                    <div className="timer-pad">
                        <div className={(this.state.turn===true ? 'timer-active' : '') + " timer-white app-timer"}>
                            <TimeView time={this.state.whiteTime}/>
                        </div>
                    </div>
                </div>  
            </div>
        );
    }


    componentDidMount() {
            setInterval(()=> {
                if (this.state.turn===true) {
                    this.setState({
                        whiteTime : this.state.whiteTime + 1
                    });
                }
                if (this.state.turn===false) {
                    this.setState({
                        blackTime : this.state.blackTime + 1
                    });
                }
            }, 1000);

            let self = this;
        document.addEventListener("keydown", (event)=> {
            if (event.keyCode === 32) {
                if (self.state.turn !== null) {
                    if (self.state.turn)  {
                        self.props.whiteMoveEndCallback();
                    } else {
                        self.props.whiteMoveStartCallback();
                    }
                    self.setState({turn: !self.state.turn});

                } else {
                    self.setState({turn: true});
                    self.props.initCallback();
                }
            }
        }, false);
    }
}
