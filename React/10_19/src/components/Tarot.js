import React from 'react'
import {useState} from 'react'
import './Tarot.css'
import TarotImage from './TarotImage'

function Tarot() {

  const [card, setCard] = useState({}) 
  

  const getCard = () => {

    fetch("https://rws-cards-api.herokuapp.com/api/v1/cards/random?n=1")
    .then(function (res) {
      return res.json()
    })
    .then(function (data) {

      if (Math.floor(Math.random() * 10) >= 5){
        let newCard = {'name':data.cards[0].name,'meaning':data.cards[0].meaning_up,'g':'Good'}
        setCard(card => ({
          ...card,
          ...newCard
        }))
      }
      else{
        let newCard = {'name':data.cards[0].name,'meaning':data.cards[0].meaning_rev,'g':'Bad'}
        setCard(card => ({
          ...card,
          ...newCard
        }))
      }
      
    })
  }


  return (
    <div id='Tarotmain'>
     
     <TarotImage />
      <br />
      Name: {card.name} ({card.g})
      <br/>
      Meaning: {card.meaning}
      <br/>
      <button onClick={() => getCard()}>Draw a Card</button>
    </div>
  )
}

export default Tarot