import React from 'react'
import {useState} from 'react'
import UserData from './UserData'

function App() {
    const defaultState = {
        username: '',
        email: ''
    }

    const defaultUserData = [{username: '', email: ''}]
    const [inputField, setInputField] = useState(defaultState)
    const [userData, setUserData] = useState(defaultUserData)
    //e is just a common variable name -- stands for "event"
    const validateForm = (e) => {
        //we do not want submitting the form to cause the page to refresh
        e.preventDefault()
        //if user does not enter a name, throw an error
        if(inputField === ''){
            alert('Please enter a name')
            return
        }
        //a name was placed in the form (i.e. form is not empty)
        setUserData([...userData, inputField])
        
        //updating the page to display our text in real time
        const changeText = (e) => {
            setInputField({
                ...inputField,
                //sets the username state to whatever is located inside of the box below
                [e.target.username]: e.target.value
            })
        }
    }
  return (
    <div className='App'>
        <h1>Login Page</h1>
        <form action='' onSubmit={(e) => validateForm(e)}>
            <input
                username = 'username'
                type = 'text'
                placeholder='username123'
                // detects if a field has been changed
                onChange={(e) => changeText(e)}
                //grabs the value from the boxes and saves it in the variable
                value = {inputField?.username}
            />
            <input
                email = 'email'
                type = 'text'
                placeholder='email@email.com'
                onChange={(e) => changeText(e)}
                value = {inputField?.email}
            />
            <imput type='submit' value='Submit'/>
        </form>
        <UserData userData={userData}/>
    </div>
  )
}

export default App