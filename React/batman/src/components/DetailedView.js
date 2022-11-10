import React from 'react'



function DetailedView({movieDetails}) {
  return (
    <>
    <li key={movieDetails.imdbID}>
        <img src={movieDetails.Poster} alt="" height="200px"/>
        <p>Year: {movieDetails.Year}</p>
        <p>Rated: {movieDetails.Rated}</p>
        <p>Released: {movieDetails.Released}</p>
        <p>Director: {movieDetails.Director}</p>
    </li>
    </>
  )
}

export default DetailedView