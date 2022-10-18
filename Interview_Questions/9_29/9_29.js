const { response } = require("express");

`Hurricane Ian has caused massive power outages across FL 
and we need to determine how many people are without power. 
Using the random data API, create a database that holds customers 
of Florida Power and store their name, phone number, and address. 
Only people with FL, GA, SC, and NC addresses should be stored. 
Add to each customer a field that indicates if they have power or not. 
Write db query that retrieves all users from the db without power. `

const e = require('express');
const logger = require('./logger');
const express = require('express');
const app = express();
const { Sequelize } = require('sequelize');
const { userDatabase } = require('./models');
let affectedUsers = [];
let userList = [];
let users = [];

const sequelize = new Sequelize('postgres://fionaeckert@localhost:5432/9_29')


app.use(express.json())

app.all('*', (req, res, next) => {
    logger.info({
        "time" : new Date(),
        "path" : req.path,
        "body" : req.body,
        "method" : req.method
    })
    next()
})
//-----------------------------------------------------------------------------

const getUsers = async() => {
    await fetch('https://random-data-api.com/api/v2/users?size=100')
    .then(response => response.json())
    .then(response => {
        response = userData;
        let randbool = Math.random() < .5;
        for(let i = 0; i < 99; i++)
            if(userData[i].address.state == 'Florida' || userData[i].address.state == 'Georgia' || userData[i].address.state == 'South Carolina' || userData[i].address.state == 'North Carolina'){
            const user = userDatabase.create({
                first_name: userData[i].first_name,
                last_name: userData[i].last_name,
                state: userData[i].state,
                affected: randbool
            })
        }
        
    





    })
}
//-----------------------------------------------------------------------------
app.listen(3000, async () => {
    console.log('Server is running on http://localhost:3000');

    try {
        await sequelize.authenticate();
        console.log('Connection has been established successfully.');
      } catch (error) {
        console.error('Unable to connect to the database:', error);
      }
});


