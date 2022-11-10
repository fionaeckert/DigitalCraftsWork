import React, { useEffect, useState } from 'react'

function App() {
  const [count, setCount] = useState (0)
  const [count2, setCount2] = useState (0)
  // const [text, setText] = useState ("")
  const [comments, setComments] = useState([])
  
useEffect(() => {
  const apiCall = async() => { 
    let results = await fetch('https://jsonplaceholder.typicode.com/comments')
    let data = await results.json();

    setComments(data)
   }
   apiCall()
}, [])


  const handleClick = () => {
    console.log("button clicked")
  }

  useEffect(()=>{
    console.log('component did mount')

    return () =>{
      //acts like component did unmount
      console.log('component did unmount')
    }
  },[count2,count])
  //you can have multiple states being changed here ^ you just have to separate them by a comma


  // useEffect(() => {
  //   first
  
  //   return () => {
  //     second
  //   }
  // }, [third])
  
  
  console.log("hello world")
  
  return (
    <>
    {Date.now()}
    <h1>{count}</h1>
      <button onClick={handleClick}>hello</button>
      <button onClick={() => setCount(count+1)}>Update UI</button>
      <button onClick={() => setCount2(count2+1)}>Update UI</button>
    <ul>
    {comments.map(obj=>{
      return <li key={obj.name}>{obj.name}</li>
    })}

    </ul>
    
    </>
  )
}

export default App
