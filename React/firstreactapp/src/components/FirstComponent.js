import React from 'react'
import './FirstComponent.css'
import Button from 'react-bootstrap/Button'

const classroom = ['Dre','Dez','Doug','Fiona']

function FirstComponent(props) {
  return (
    <div>
    <h3>{props.title}</h3>
    {classroom.map(student => (
        <Button> {student} </Button>
    ))}

    </div>
  )
}

export default FirstComponent