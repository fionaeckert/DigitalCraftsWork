import React, {useState, useEffect} from 'react'
import BatMoviesDetails from './BatMoviesDetails'

function BatMovies() {
    const [movies, setMovies] = useState([])

    useEffect(()=> {
        const moviesData = async () => {
            let response = await fetch('http://www.omdbapi.com/?s=batman&apikey=b3ea0b07')
            let data = await response.json();
            setMovies(data.Search)
        }
        console.log(movies)
        moviesData()
    },[])

  return (
    <>
    <h1>Click on the below links to explore Batman Movies!</h1>
    <ul>
    {movies.map(moviesObj => {
        return <BatMoviesDetails movie={moviesObj}/>
    })}
    </ul>
    
    
    </>
  )
  
}

export default BatMovies