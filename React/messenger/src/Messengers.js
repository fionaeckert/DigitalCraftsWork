import React from 'react'
import { useState } from 'react'

function Messengers() {
    const defaultState = {
        userTurn: true,
        message: ''
    }


    const [textConvoField, setTextConvoField] = useState(defaultState)
    const [textBubble, setTextBubble] = useState()
    
    
  
  
    const sendMessage = (e) => {
        e.preventDefault()
        setTextConvoField({
            ...textConvoField,
            [e.target.text]: e.target.value
        })
        console.log('sent message')
    }
  
    return (
    <div className='Messenger'>
    <form action="" onSubmit={(e) => sendMessage(e)}>
        <input
        name='composeText' 
        type="text"
        placeholder='Send message'
        onChange={(e) => sendMessage(e)}
        value={textConvoField?.composeText} 
        />
    </form>
    </div>
    
  )
}

export default Messengers