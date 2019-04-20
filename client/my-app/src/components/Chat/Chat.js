import React from 'react';
import  './Chat.css';
export class Chat extends React.Component {
    constructor(props) {
        super(props);
    }


    render() {
        return (
            <div className='Chat-div height-all' >
                    <div className='Chat-label' id="chat-scroll">
                        {this.props.messages.map((item, index)=> {
                        return <div className={'Message-style-all ' + ( item.user ?  'Message-style-author1' : 'Message-style-author2' )}>
                                <div key = {index} className={'Message-style-all ' + ( item.user ?  'Message-content-author1' : 'Message-content-author2' )}> {item.text} </div>
                            </div>
                        })}
                    </div>
                    <div className="chat-mic-container">
                        <div className={'gn ' + (this.props.listening ? 'microphone-active' : 'microphone-inactive')}><div className="mc"></div></div>
                    </div>
            </div>
        );
    }

    componentDidUpdate() {
        // Scroll to bottom when adding new messages
        let chatContainer = document.getElementById('chat-scroll');
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }
}