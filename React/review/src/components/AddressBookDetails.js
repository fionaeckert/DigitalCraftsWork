import React from 'react'

function AddressBookDetails({obj, onDelete}) {
  return (
    <>
    <li key={obj.id}>
        <p>{obj.name}</p>
        <p>{obj.email}</p>
        <p>{obj.phone}</p>
        <button onClick={()=>onDelete(obj.id)}>Delete?</button>
    </li>
    
    </>
  )
}

export default AddressBookDetails