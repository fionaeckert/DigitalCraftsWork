import React, {useState, useEffect} from 'react'
import DetailedView from './DetailedView'

const BatMoviesDetails = ({movie}) => {
    const [selectedMovie, setSelectedMovie] = useState([])

    return (
      <>
      <li key={movie.imdbID}>
        
        <h2 onClick={useEffect(()=>{
        const selectedMovieData = async () =>{
            let response = await fetch('http://www.omdbapi.com/?i=tt0372784&apikey=b3ea0b07')
            let data = await response.json();
            setSelectedMovie(data)
        }
        selectedMovieData()
        },
        [])}>
            {movie.Title}
        </h2>
        <img src={movie.Poster} alt="" height="200px"/>
        </li>
        <br />
        <br />
        <ul>
        {selectedMovie.map(selectedMovieObj => {
            return <DetailedView movieDetails={selectedMovieObj} />
        })}
        </ul>
      </>
    )
  }
  
  export default BatMoviesDetails