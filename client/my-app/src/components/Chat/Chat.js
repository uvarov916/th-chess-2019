import React from 'react';
import  './Chat.css';
export class Chat extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            messages: [
                {user: true, message: 'Hi'},
                {user: false, message: 'Hi'},
                {user: true, message: 'How are you?'}
            ]
        }
    }

    render() {
        console.log(this.state.messages);
        return (
            <div className='Chat-div height-all'>
                    <div className='Chat-label'>
                        {this.state.messages.map((item, index)=> {
                        return <div className={'Message-style-all ' + ( item.user ?  'Message-style-author1' : 'Message-style-author2' )}>
                                <div key = {index} className={'Message-style-all ' + ( item.user ?  'Message-content-author1' : 'Message-content-author2' )}> {item.message} </div>
                            </div>
                        })}
                    </div>
            </div>
        );
    }
}