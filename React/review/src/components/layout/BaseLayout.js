import React from 'react'
import { Link } from 'react-router-dom'

// create 2 components: one for Forms, one for News
// add components to react-router to index.js
// add the links to base layout
function BaseLayout(props) {
  return (
    <>
        <ul>
            <li>
                <Link to="/">Home</Link>
            </li>
            <li>
                <Link to="/forms">Forms</Link>
            </li> 
            <li>
                <Link to="/formsclass">Forms Class</Link>
            </li> 
            <li>
                <Link to="/news">News</Link>
            </li>
            <li>
                <Link to="/shoppinglist">Shopping List</Link>
            </li>
            <li>
                <Link to="/addressbook">Address Book</Link>
            </li>
        </ul>

        {props.children}
    </>
  )
}

export default BaseLayout