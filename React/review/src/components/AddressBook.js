import React, {useState} from 'react'
import AddressBookDetails from './AddressBookDetails'
import {v4 as uuidv4} from 'uuid'


// try to add delete and sorting functionality to address book

function AddressBook() {
    const [addressBook, setAddressBook] = useState([])
    const [name, setName] = useState("")
    const [number, setNumber] = useState("")
    const [email, setEmail] = useState("")
    const [address, setAddress] = useState("")
    const [state, setState] = useState("")
    const [city, setCity] = useState("")
    const [zipcode, setZipcode] = useState("")

    const handleDelete = (id) => {
        let newAddressBook = addressBook.filter(contact => {
            return id !== contact.id
        })
        setAddressBook(newAddressBook)
    }

    const handleSubmit = (e) => {
    e.preventDefault()
    let contact = {
        name, email, number, address, city, state, zipcode,
        id: uuidv4()
    }
    let newAddressBook = [...addressBook, contact]
    setAddressBook(newAddressBook)

    setName("")
    setNumber("")
    setEmail("")
    setAddress("")
    setCity("")
    setState("")
    setZipcode("")
}

  return (
    <>
    <h2>Address Book</h2>
    <br />
    <form onSubmit={handleSubmit}>
        <input type="text" value={name} placeholder="Full name" onChange={e=>setName(e.target.value)}/>
        <br />
        <br />
        <input type="email" value={email} placeholder="Email" onChange={e=>setEmail(e.target.value)}/>
        <br />
        <br />
        <input type="text" value={number} placeholder="Phone number" onChange={e=>setNumber(e.target.value)}/>
        <br />
        <br />
        <input type="text" value={address} placeholder="Address" onChange={e=>setAddress(e.target.value)}/>
        <br />
        <br />
        <input type="text" value={city} placeholder="City" onChange={e=>setCity(e.target.value)}/>
        <br />
        <br />
        <input type="text" value={state} placeholder="State" onChange={e=>setState(e.target.value)}/>
        <br />
        <br />
         <input type="text" value={zipcode} placeholder="Zip code" onChange={e=>setZipcode(e.target.value)}/>
        <br />
        <br />
        <input type="submit" />

        <ul>
            {addressBook.map((placeholder) => {
                return <AddressBookDetails key={placeholder.id} obj={placeholder} onDelete={handleDelete} />
            })}  
        </ul>
    </form>
    </>
  )
}

export default AddressBook

