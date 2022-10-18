// const winston = require('winston');
//GET and DELETE should never have a body!!!!!
//DELETE is path parameters
//POST and PUSH have a body
//GET uses query parameters!!!!

//Express allows us to create a server that can host an API. We are hosting the API on localhost(127.0.0.1)
const express = require('express');
const app = express();
const logger = require('./logger.js')
let pokedex = require('./database')
const ejs = require('ejs');
const { response } = require('express');
const pg = require('pg-promise')(); //saying "this package requires pg promise" and also instantiating it with the second set of ()
const db = pg("postgres://fionaeckert@localhost:5432/postgres");
//By default, express server cannot read requests body in JSON so we need to add this function to enable that feature 
app.use(express.json())
app.set('view engine','ejs')


app.all('*', (req, res, next) => { // next tells the computer that we're gonna go to the next function according to whatever the end point is called (so if there are 2 GET calls, it'll recognize both)
    logger.info({
        action: req.method, //returns what the API call is (GET, POST, PUT, etc.)
        path: req.path,
        body: req.body,
        time:new Date(),
    })
    next()
})

//Endpoint
//Getting a resource from the db
// Get should always take parameters as a query (ie /pokemon/?pikachu)
app.get('',function(req,res){
    db.any('SELECT * FROM pokemon').then((pokemon) => response.send(pokemon)); //selecting all Pokemon from the database
    logger.info({
        status_code:response.statusCode,
        response_body: response.body,
        time: new Date()})
})

app.get('/pokemon/', (request, response) => { 
    let pokeName = request.query.name
        db.oneOrNone(`SELECT * FROM pokemon WHERE name = $1,pokeName`, pokeName).then(poke); //$1 signals that the call should increment 
        logger.info({
            status_code:response.statusCode,
            response_body: poke,
            time: new Date()
        }) 
        response.send(poke)    
    })

//Sending a template to the browser
//Template is an html outline where you swap out values
app.get('/poke', (req,res) => {
    res.render("pokedex",{pokedex:pokedex}) //first parameter is the name of the template, second parameter is the actual object
    //res.render will automatically look for a "views" folder
})
//Adding a resource to the db
//Path parameters are added to the end of the uri. They are taken by the API and used to specify which resources in the db we are referring to.
//NOTE: NOT ALL ENDPOINTS USE PATH PARAMS
app.post('/pokemon/',(req,res) => {
    newPokemonObject = {'name': req.body.name, 'hp':req.body.hp}
    pokedex.push(newPokemonObject)
    res.send(`You created a ${newPokemonObject.name} pokemon with an HP of ${newPokemonObject.hp}.`)})

//Modifies a resource that already exists by replacing the entire 
//Example: {Pokemon: Pikachu, HP: 40} -> {Pokemon: Pikachu, HP: 50}

//in a PUT, place fields to be updated in the request body
app.put('/pokemon/:name', (request,response) => {
    let pokemon = request.params.name;

    //Case 1: check if the HP value is positive and within a reasonable range
    if (request.body.hp <= 10 || request.body.hp > 250){
        response.statusCode = 400
        response.send('HP value is not valid.')
    }
    //Case 2: check the type of HP to make sure it's a number
    if(typeof(request.body.hp) != 'number'){
        response.statusCode = 400
        response.send('HP value is not valid.')
    }
    let updated = {}
    for(let i = 0; i < pokedex.length; i++){
        //check if the name of the pokemon in the request is in the db
        if(pokedex[i].name == pokemon){
            //update pokemon's hp to the requested value
            pokedex[i].hp = Math.round(request.body.hp)
            updated = pokedex[i]
        }
    }
    // Send a receipt to the client of exactly what we changed in the db
    response.send(updated);
})

//Deletes resource from db
app.delete('/pokemon/:name', (req,res) => {
    let name = req.params.name
    //Checking if pokemon is in db
    for (let index=0; index<pokedex.length; index++){
        if(pokedex[index].name == name){
            deletedPokemon = pokedex[index]
            pokedex.splice(index,1)
            res.send(deletedPokemon)
        }
    }
    res.statusCode = 400
    res.send("Pokemon doesn't exist.")
})

app.listen(3000)
// console.log('Server is running on port 3000')
