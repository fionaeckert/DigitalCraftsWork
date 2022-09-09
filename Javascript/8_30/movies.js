const displayMovieOne = document.getElementById('movie1')
const displayMovieTwo = document.getElementById('movie2')
const displayMovieThree = document.getElementById('movie3')
const displayMovieFour = document.getElementById('movie4')
const displayMovieFive = document.getElementById('movie5')

const posterMovieOne = document.getElementById('poster1')
const posterMovieTwo = document.getElementById('poster2')
const posterMovieThree = document.getElementById('poster3')
const posterMovieFour = document.getElementById('poster4')
const posterMovieFive = document.getElementById('poster5')

const getMovies = () => {
    fetch('https://api.themoviedb.org/3/movie/now_playing?api_key=70f69131b014b417e60b96a4fefe4997&language=en-US&page=1')
    .then(movieResponse => {
        return movieResponse.json();})
    .then(movies => {
        getTop5(movies);
        getTitles();
        getPosters();
    })   
    }

const getTitles = () => {
    displayMovieOne.innerText = (topMovies[0].title)
    displayMovieTwo.innerText = (topMovies[1].title)
    displayMovieThree.innerText = (topMovies[2].title)
    displayMovieFour.innerText = (topMovies[3].title)
    displayMovieFive.innerText = (topMovies[4].title)
}

const getPosters = () => {
    posterMovieOne.src = `https://image.tmdb.org/t/p/original/${topMovies[0].poster_path}`
    posterMovieTwo.src = `https://image.tmdb.org/t/p/original/${topMovies[1].poster_path}`
    posterMovieThree.src = `https://image.tmdb.org/t/p/original/${topMovies[2].poster_path}`
    posterMovieFour.src = `https://image.tmdb.org/t/p/original/${topMovies[3].poster_path}`
    posterMovieFive.src = `https://image.tmdb.org/t/p/original/${topMovies[4].poster_path}`
    
    // for (i=0; i <{topMovies.length; i++){
    //     currentMovie ={topMovies[i].id
    //     fetch('https://api.themoviedb.org/3/movie/${currentMovie}/images?api_key=70f69131b014b417e60b96a4fefe4997&language=en-US')
    // .then(posterResponse => {
    //     return posterResponse.json();
    // })
    // }
}

    
const getTop5 = (movies) => {
    // popScores = [];
    // topPopScores = [];
    // topMovies = [];
    // for (let i = 0; i < movies.results.length; i++){
    //     popScores.push(movies.results[i].popularity);
    // }
    
    // popScores = popScores.sort().reverse();
    // for (let i = 0; i < 5; i ++){
    //     topPopScores.push(popScores[i]);
    // }
    
    // for (let j = 0; j < movies.results.length; j++){
    //     for (let i = 0; i < 5; i++){
    //         if (movies.results[j].popularity == topPopScores[i]) {
    //             topMovies.push(movies.results[j]);
    //         }
    //     }
    // }

    topMovies = [];
    for (let i = 0; i < 5; i++){
        topMovies.push(movies.results[i])
    }

}