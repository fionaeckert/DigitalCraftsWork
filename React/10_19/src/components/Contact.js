import React from 'react'
import Card from 'react-bootstrap/Card';
import Badge from 'react-bootstrap/Badge';
import './Contact.css'

function Contact() {
  return (
    <div>
      <div id="header">
        <svg xmlns="http://www.w3.org/2000/svg" width="45" height="45" fill="currentColor" className="bi bi-code" viewBox="0 0 16 16">
          <path d="M5.854 4.854a.5.5 0 1 0-.708-.708l-3.5 3.5a.5.5 0 0 0 0 .708l3.5 3.5a.5.5 0 0 0 .708-.708L2.707 8l3.147-3.146zm4.292 0a.5.5 0 0 1 .708-.708l3.5 3.5a.5.5 0 0 1 0 .708l-3.5 3.5a.5.5 0 0 1-.708-.708L13.293 8l-3.147-3.146z"/>
        </svg>
        <h2>
          Developer Team<Badge bg="secondary"></Badge>
        </h2>
        <svg xmlns="http://www.w3.org/2000/svg" width="45" height="45" fill="currentColor" className="bi bi-code-slash" viewBox="0 0 16 16">
          <path d="M10.478 1.647a.5.5 0 1 0-.956-.294l-4 13a.5.5 0 0 0 .956.294l4-13zM4.854 4.146a.5.5 0 0 1 0 .708L1.707 8l3.147 3.146a.5.5 0 0 1-.708.708l-3.5-3.5a.5.5 0 0 1 0-.708l3.5-3.5a.5.5 0 0 1 .708 0zm6.292 0a.5.5 0 0 0 0 .708L14.293 8l-3.147 3.146a.5.5 0 0 0 .708.708l3.5-3.5a.5.5 0 0 0 0-.708l-3.5-3.5a.5.5 0 0 0-.708 0z"/>
        </svg>
      </div>
      <div id="card">
      <Card style={{ width: '18rem' }}>
        <Card.Body>
          <Card.Title>Co-Developer</Card.Title>
          <Card.Text>
            Jonathan Batalla
          </Card.Text>
        </Card.Body>
      </Card>
      <Card style={{ width: '18rem' }}>
        <Card.Body>
          <Card.Title>Co-Developer</Card.Title>
          <Card.Text>
            Khanh Trinh
          </Card.Text>
        </Card.Body>
      </Card>
      <Card style={{ width: '18rem' }}>
        <Card.Body>
          <Card.Title>Co-Developer</Card.Title>
          <Card.Text>
            Fiona Eckert
          </Card.Text>
        </Card.Body>
      </Card>
      </div>
    </div>
  )
}

export default Contact