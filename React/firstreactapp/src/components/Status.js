import {React, useState} from 'react'

function Status() {
    const [status, setStatus] = useState('Away');
    const [emoji, setEmoji] = useState('🟡')

    const updateStatus = (newStatus, newEmoji) => {
        setStatus(newStatus)
        setEmoji(newEmoji)
    }
  return (
    <div>
        <h3>Status: {status}{emoji}</h3>
        <button onClick={() => updateStatus('Active','🟢')}>Active</button>
        <button onClick={() => updateStatus('Away','🟡')}>Away</button>
        <button onClick={() => updateStatus('Vacation','🌴')}>Vacation</button>
        <button onClick={() => updateStatus('In a Meeting',	'📅')}>In a Meeting</button>
        <button onClick={() => updateStatus('Commuting','🚌')}>Commuting</button>


    </div>
  )
}

export default Status