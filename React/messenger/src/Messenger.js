import React, { Component } from 'react'

const textConversation = []

export class Messenger extends Component {
    constructor(props) {
        super(props);
        this.state = {
            userTurn: true,
            message: '',
            userClass: 'User1'
        };
    };

    sendText = (text) => {
        this.setState({
            message: this.state.message + text,
            userTurn: !this.state.userTurn
        })
    
        if (this.state.userTurn === true) {
            this.setState({
                userClass: 'User1'
            })
        }

        else {
            this.setState({
                userClass: 'User2'
            })
        }

        textConversation.push(this.state.message.valueOf);
    }

  render() {
    
    return (
      <div>
        <h1>Messenger</h1>

        <div>
            {
                textConversation.map((message,i) => 
                <li key={i}>{message}</li>)
            }
            
            <h5>message: {this.state.message.valueOf}</h5>
        </div>

        <div className={`input+${this.state.userClass}`}>
            <form onSubmit={this.sendText()}>
                <input ref="text" type="text" placeholder="send message"/>
                <button type="submit">Send</button>
            </form>
        </div>
      </div>
    )
  }
}

export default Messenger