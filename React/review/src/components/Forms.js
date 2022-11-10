import React, { useState } from 'react'

const Forms = () => {
    const [count, setCount] = useState(0) // let count = 0
    const [text, setText] = useState("") // let text = ""
    const [isValid, setIsValid] = useState(true)
    const [city, setCity] = useState("Seattle")
const handleSubmit = (e) => {
    e.preventDefault()

    let dataObj = {
        text,
        isValid,
        city

    }
    console.log(dataObj)
}  
  
return (
    <>
        <h2>{count}</h2>
        <h2>{text}</h2>
        <h3>{isValid ? "true" : "false"}</h3>
        <h1>{city}</h1>
        <button onClick={() => setCount(count + 1)}>click</button>
        
        <form onSubmit={handleSubmit}>
            <input type="text" value={text} onChange={e=>setText(e.target.value)}/>
            <br />
            <input type="checkbox" value={isValid} defaultChecked={isValid} onChange={e=>setIsValid(e.target.checked)}/>
            <br />
            <select value={city} onChange={e=>setCity(e.target.value)}>
                <option value="Houston">Houston</option>
                <option value="Atlanta">Atlanta</option>
                <option value="Seattle">Seattle</option>
                <option value="Chicago">Chicago</option>
                <option value="Boston">Boston</option>
                <option value="NYC">NYC</option>
            </select>
            <input type="submit" />
        </form>

    </>
  )
}

export default Forms