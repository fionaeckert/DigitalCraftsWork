import React from 'react'
import MyNavBar from './MyNavBar'

function PageTemplate(props) {
  return (
    <div>
        <MyNavBar />
        {props.children}

    </div>
  )
}

export default PageTemplate