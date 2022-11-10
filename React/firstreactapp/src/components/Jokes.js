import React, {useState, useEffect} from 'react'

function Jokes() {
    const [joke, setJoke] = useState('');

    //This will update our page to display the joke automatically
    useEffect(() => {
     let newDiv = document.createElement('div');
     let divContent = document.createTextNode(joke);
     newDiv.appendChild(divContent)
     document.body.insertBefore(newDiv )
        console.log('inside useEffect hook')
        //Call the joke API from here

    })

    const getJoke = () => {
        fetch('https://api.chucknorris.io/jokes/random')
        .then((res) => res.json())
        .then((data) => {
            console.log(data.value);
            setJoke(data.value)
        })
    }
  return (
    
    <div>
        {joke}
    <button onClick={()=>getJoke()}></button>

    </div>
  )
}

export default Jokes