import {React, useState} from 'react'

export default function FunctionalCounter() {
    //count is the name of the state
    //setCount replaces the setState function and changes the value of the state
    //the useState function sets the default
    //whatever the first variable is called, the second should mirror with 'set' in front (i.e. price, setPrice)
const [count, setCount] = useState(0);

  return (
    <div>
    <span>{ count }</span>
    <button onClick={() => setCount(count + 5)}>Add 5</button>
    <button onClick={() => setCount(count + 50)}>Add 50</button>
    <button onClick={() => setCount(count + 150)}>Add 150</button>
    </div>
  )
}
