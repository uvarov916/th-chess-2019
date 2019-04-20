import React, { Component } from 'react';
import './TimeController.css';
import {TimeView} from './TimeView'

export class TimeController extends Component {
    constructor(props) {
        super(props);
        this.state = {whiteTime : 0, blackTime : 0, turn : true}; 
    }
    
    render() {
        return (
            <div className="time-controller">
                <div className="timer-back">
                    <div className="timer-pad">
                        <div className={(!this.state.turn ? 'timer-active' : '') + " timer-black app-timer"}>
                            <TimeView time={this.state.blackTime}/>
                        </div>
                    </div>
                    <div className="timer-pad">
                        <div className={(this.state.turn ? 'timer-active' : '') + " timer-white app-timer"}>
                            <TimeView time={this.state.whiteTime}/>
                        </div>
                    </div>
                </div>  
            </div>
        );
    } 

    static getDerivedStateFromProps(props) {
        this.setState({turn : props.turn})
        console.log(this.state.turn)
    }

    componentDidMount() {
        setInterval(()=> {
            if (this.state.turn) {
                this.setState({
                    whiteTime : this.state.whiteTime + 1
                });
            } else {
                this.setState({
                    blackTime : this.state.blackTime + 1
                });
            }
        }, 1000)
    } 
}
