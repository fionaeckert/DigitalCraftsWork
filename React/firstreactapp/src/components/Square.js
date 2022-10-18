import {React, useState} from 'react'
import '../css/Square.css'

function Square(props) {
    const [mined, setMined] = useState(false);
    //each square can have one of three elements: empty, gold, mine
    const [element, setElement] = useState('');
    const [emoji, setEmoji] = useState('🪨')

    const mining = () => {
        setMined = true;
        setElement = props.element
        if(element == 'gold') {
            setEmoji('💰')
        } else if (element =='empty'){
            setEmoji('🚮')
        }
        else if (element =='mine'){
            setEmoji('💣')
        }
        //Check if we clicked on a mine
        if (element == 'mine') {
            //set game over
            props.setGameOver('true')
            return (
                <div>
                    Game Over!
                </div>
            )
        }
    }
  
  //pick a color for our default square
    return (
    <div class="square" onClick={()=> {mining()}}>{emoji}</div>
  )
}

export default Square