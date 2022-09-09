const getUsers = async() => {
    await fetch('https://random-data-api.com/api/v2/users?size=100')
    .then(response => {
        return response.json();
    })
    .then(userData => {
        console.log(userData)
        
    for (let i = 0; i < 99; i++) {

        let newCard = document.createElement('div')
            newCard.className = 'card'
            document.getElementById('content').appendChild(newCard)


        let userImage = document.createElement('img')       // adding image to each card
        console.log(typeof(newCard))
        userImage.src = userData[i].avatar
        newCard.appendChild(userImage)
       
        
        let userTitle = document.createElement('h5')        //adding username to each card
        userTitle.innerText = userData[i].username
        newCard.appendChild(userTitle)

        let userMessage = document.createElement('p')      // adding message to each card
        userMessage.innerText = "Hi, my name is " + userData[i].first_name + " " + userData[i].last_name + ". I am a " + userData[i].employment.title + ".";
        newCard.appendChild(userMessage)
    
        let hoverText = document.createElement('button') // adding button to each card
        hoverText.className = "btn btn-secondary"
        hoverText.innerText = 'More Info'
        hoverText.title = `${userData[i].first_name} ${userData[i].last_name}\n ${userData[i].address.state}, ${userData[i].address.country}\n ${userData[i].subscription.status}`  // adding tool tip capabilities to button created above
        newCard.appendChild(hoverText)   
}

    })
}