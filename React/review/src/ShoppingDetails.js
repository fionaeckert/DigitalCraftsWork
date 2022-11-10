import React from 'react'

// itemDetailObject is a prop with id and item 
/**
 * {
 * id 
 * item
 * }
 */
const ShoppingDetails = ({itemDetailObject, onDelete}) => {
    
  return (
    <>
      <li key={itemDetailObject.id}> {itemDetailObject.item}</li>
      <button onClick={()=>onDelete()}>Delete?</button>
    </>
  )
}

export default ShoppingDetails