import React, { Component } from 'react';

class TimeView extends Component {
    constructor(props) {
        super(props);
        this.state = {strTime : TimeView.timeToStr(props.time)};
    }
    static timeToStr (time) {
        let strTime;
        let sec = (time % 60).toFixed();
        let min = (time / 60).toFixed();
        let hour = (min / 60).toFixed();
        if (min == 60) {
            min = 0; hour = Number.parseInt(hour) + 1;
        }
        if (sec < 10) {
            sec = 0 + sec;
        }
        if (min < 10) {
            min = 0 + min;
        }
        if (hour < 10) {
            hour = 0 + hour;
        }
        if (hour > 0) {
            strTime = hour + ":" + min + ":" + sec;
        } else {
            strTime = min + ":" + sec;
        }
        return strTime;
    }
    render() {
        return (
            <div>
            <h1> {this.state.strTime} </h1>
            </div>
        );
    }
    static getDerivedStateFromProps(props) {
        return {strTime : TimeView.timeToStr(props.time)};
    }
};

export default TimeView;
