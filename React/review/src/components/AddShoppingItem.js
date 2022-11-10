import React, {useState} from 'react'


//need to get to the onAdd prop 
function AddShoppingItem({onAdd}) {
    const [item, setItem] = useState("");

    const handleSubmit = (e) => { 
        e.preventDefault()

        onAdd(item)
        setItem("")
     }
  return (
    <>
     <form onSubmit={handleSubmit}>
        <input type="text" value={item} onChange={e=>setItem(e.target.value)}/>
        <br />

        <input type="submit" />
      </form>
    
    </>
  )
}

export default AddShoppingItem