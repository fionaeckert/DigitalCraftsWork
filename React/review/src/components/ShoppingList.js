import React, {useState} from 'react'
import ShoppingDetails from '../ShoppingDetails'
import AddShoppingItem from './AddShoppingItem'
import {v4 as uuidv4} from 'uuid'


/**
 * {
 *  id: uuid
 *  item: Item 
 *  
 * }
 */
const ShoppingList = () => {
  const [list, setList] = useState([]);  //["". "", ""]   // [{}, {}, {}, {}]

//newItem is a string which documents the grocery list added 
  const handleAdd = (newItem) => { //new item is a string
//build new item
    let newItemObj = {
      id: uuidv4(),
      item: newItem
    }
//add new item to our local state list
    let newList = [newItemObj, ...list]

//update local state
    setList(newList)

  }
  
  const handleDelete = (id) => {
    let newList = list.filter(shoppingObj => {
        return id !== shoppingObj.id

    })
    setList(newList)
  }

//do not need handleSubmit anymore because this is being handled in the children

  // const handleSubmit = (e) => {
  //   e.preventDefault();

  //   let newItemObj = {
  //     id: uuidv4(), 
  //     item
  //   }
  //   // let newList = [item, ...list] //array of strings
  //   let newList = [newItemObj, ...list]  //array of objs

  //   setList(newList)
  //   setItem("")  //reset our input field

  //   console.log(list);
  // }
    
  return (
    <>
      <h2>Shopping List</h2>
      <br />

      <h3>Add new Item:</h3>

    
     <AddShoppingItem onAdd={handleAdd}/>


    <ul>

    {list.map(listItem =>{
        return <ShoppingDetails key={listItem.id} itemDetailObject={listItem} onDelete={handleDelete}/>
      })}
    </ul>

    </>
  )
}

export default ShoppingList