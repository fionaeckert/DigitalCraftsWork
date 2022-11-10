import React, { Component, useRef } from 'react'


const textConversation = []


export default class Message extends Component {
  constructor(props) {
    super(props);
    this.myRef = React.createRef();
    this.state = {
        userTurn: true, 
        message: '',
        userClass: 'User1'
    };
};
sendText = (text) => { 
  text.preventDefault()
  console.log(text)
  console.log(text.value)
  this.setState({
      message: this.state.message + text.target.value,
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
  textConversation.push(this.state.message);
  console.log(textConversation)
}


  render() {
    return (
     <div>
        <div className='messageDiv'>
              {
                  textConversation.map((i) => {
                  for(let i =0; i <textConversation.length; i++){
                  <li key={i}>{this.state.message}</li>
                  }}
                )
            }
        </div>
        
        <h5>message: {textConversation}</h5>
        {/* {console.log(this.state.textConversation)} */}
        
        <div className="user1">
            <form>
                <input 
                  name='messageBox'
                  type="text" 
                  placeholder="send message"
                  onChange={(text) => this.sendText(text)}
                  value={this.state.message?.messageBox}
                />
                <button type="submit">Send</button>
            </form>
        </div> 
    </div>
    )
  }
}
