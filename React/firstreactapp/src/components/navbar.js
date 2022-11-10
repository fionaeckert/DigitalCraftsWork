import React from 'react'
import { NavLink } from 'react-router-dom'
import './Navbar.css'

function navbar() {
  return (
    //Unlike href, navlink cannot go to outside servers
    <div id='navBar'>
        <div><NavLink to='/'>Home</NavLink></div>
        <div><NavLink to='/minesweeper'>Minesweeper</NavLink></div>
        <div><NavLink to='/jokes'>Jokes</NavLink></div>
        <div><NavLink to='/login'>Login</NavLink></div>

    </div>
  )
}

export default navbar