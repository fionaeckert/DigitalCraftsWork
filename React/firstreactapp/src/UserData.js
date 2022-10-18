// after people have gone to the App component, this component will be triggered to show who else has logged in

import React from 'react'

function UserData( { userData }) {
  return (
    <div>
        <h1>
            Logged In:
        </h1>
        <form action=''>
            <div className='formData'>
                {userData.map((user) => {
                    if(user.username === ''){
                        return null
                    } else {
                        return (
                            <>
                            <input type='text' disabled value={user.username}/>
                            <input type='text' disabled value={user.email}/>
                            </>
                        )
                    }
                })}
            </div>
        </form>
    </div>
  )
}

export default UserData