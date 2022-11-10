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

    const validateForm = (e) => {
        // We do not want submitting the form to cause the page to refresh
        e.preventDefault()
        // If user does not enter a name, throw an error
        if(inputField === '') {
            alert('Please enter a name')
            return
        }

        // A name was placed in the form
        setUserData([...userData, inputField])
    }

    // Updating the page to display our text in real time
    const changeText = (e) => {
        console.log(e)
        console.log('Input Field: ', inputField)
        setInputField({
            ...inputField,
            [e.target.name]: e.target.value
        })
    }

  return (
    <div className='App'>
        <h1>Login Page</h1>
        <form action='' onSubmit={(e) => validateForm(e)}>
            <input 
                name='username'
                type='text'
                placeholder='username123'
                onChange={(e) => changeText(e)}
                value={inputField?.username}
            />

            <input 
                name='email'
                type='text'
                placeholder='youremail@email.com'
                onChange={(e) => changeText(e)}
                value={inputField?.email}
            />
            <input type='submit' value='Submit' />
        </form>
        <UserData userData={userData} />
    </div>
  )
}

export default App