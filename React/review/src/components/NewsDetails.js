import React from 'react'

const NewsDetails = ({article}) => {
  return (
    <>
    <li key={article.title}>

        <h2>{article.title}</h2>
        <img src={article.urlToImage} alt="" height="200px"/>
        <p>{article.description}</p>

    </li>
    
    </>
  )
}

export default NewsDetails