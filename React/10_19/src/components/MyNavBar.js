import React from 'react';
import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import NavDropdown from 'react-bootstrap/NavDropdown';
import "./MyNavBar.css"


function MyNavBar() {
  return (
<div>
    <Navbar className="navbar" bg="light" expand="lg">
      <Container>
        <Navbar.Brand href="#home"></Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
          <Nav.Link href="/">Home</Nav.Link>
          <Nav.Link href="/contact">Contact</Nav.Link>
          <Nav.Link href="/tictactoe">TicTacToe</Nav.Link>
          <Nav.Link href="/tarot">Tarot</Nav.Link>
          <NavDropdown title='👤'>
            <NavDropdown.Item href="/login">Login</NavDropdown.Item>
                    <NavDropdown.Divider />
                    <NavDropdown.Item href="/logout">Sign Out</NavDropdown.Item>
            </NavDropdown>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
</div>
  )
}
export default MyNavBar;