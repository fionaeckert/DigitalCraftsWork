import {React, useState} from 'react'
import Square from './Square';
import '../css/Minesweeper.css'

// // Objective: mining for gold, get 3 pieces of gold without hitting the mine
// Assign items to each spot: 1 mine, 5 pieces of gold, 10 spots empty
function Minesweeper() {
    const [gameOver, setGameOver] = useState(false);
    const [gold, setGold] = useState(0);
    const [turns, setTurn] = useState(0);
    //const [minePosition, setMinePosition] = useState(0,2);
    //const [safeSpaces, setSafeSpaces] = useState(0)
  return (
    <div>
        <div className = 'row'>
            <Square element="empty"/>
            <Square element="gold"/>
            <Square element="empty"/>
            <Square element="empty"/>
        </div>
        <div className = 'row'>
            <Square element="empty"/>
            <Square element="gold"/>
            <Square element="empty"/>
            <Square element="mine" game={setGameOver}/>
        </div>
        <div className = 'row'>
            <Square element="empty"/>
            <Square element="gold"/>
            <Square element="empty"/>
            <Square element="empty"/>
        </div>
        <div className = 'row'>
            <Square element="empty"/>
            <Square element="gold"/>
            <Square element="empty"/>
            <Square element="gold"/>
        </div>
    </div>
  )
}

export default Minesweeper