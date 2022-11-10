import React, {useState, useEffect} from 'react'
import NewsDetails from './NewsDetails'

function News() {


//these are pieces of state
  const [articles, setArticles] = useState([]) //this will hold the articles from our API
  const [filteredArr, setFilteredArr] = useState([]) //this will hold the FILTERED articles from the API
  const [text, setText] = useState('') // this will keep track of what's being searched

  useEffect(()=> {
    const newsData = async () => {
      let response = await fetch('https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=8ee1818a1ab24120883dad71b85e5644')
      let data = await response.json();
      setArticles(data.articles)
      setFilteredArr(data.articles)
    }
    newsData()
  },[])

// in order to incorporate search functionality, we need to keep the original API data as well as the new API data that's rendered when a search is entered
// need to keep track of both states

const handleChange = (e) => {
  setText(e.target.value)
  let filteredResults = articles.filter(articleObj => {
    return articleObj.title.toLowerCase().includes(text.toLowerCase)
  })

  setFilteredArr(filteredResults)
}

  return (
    <>
    <h1>News</h1>
    <input type="text" onChange={handleChange}/>
    <ul>
    {filteredArr.map(articleObj =>{
      return <NewsDetails article={articleObj} />
    })}
    </ul>
    </>
  )
}

export default News