const { userTables } = require('./models')
const express = require('express');
const ejs = require('ejs');
const { default: axios } = require('axios');
const app = express();
app.set('view engine', 'ejs');
app.use(express.json())


app.get('/userinfo', async (req,res) => {
    res.render("newUser")
    await createUser()
})

async function createUser(){
    let newUser = {
        'firstName': document.getElementById('firstName-box').value,
        'lastName': document.getElementById('lastName-box').value,
        'email': document.getElementById('email-box').value,
        'street': document.getElementById('street-box').value,
        'state': document.getElementById('state-box').value,
        'zipcode': document.getElementById('zip-box').value
    }   
    }

app.post('/createuser', async(req,res)=>{
    console.log('called createuser endpoint')
    userTables.create({
        'firstName': 'hi',
        'lastName': 'hi',
        'email': 'hi',
        'street': 'hi',
        'state': 'hi',
        'zipcode': 1
    })
    res.send('hi')
})

app.listen(3000)
console.log("Server is running on port 3000") 