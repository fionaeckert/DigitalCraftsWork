const axios = require('axios').default;
const { pokemon, trainers, gymleaders } = require('./models')
const express = require('express');
// const gymleaders = require('./models/gymleaders');
const app = express()

app.use(express.json())

// 1). Modify the code so that the drawPokemon function gets 5 cards and stores them to the database
// 2). Convert this into an API, so each function will be called by its corresponding (use express)
// 3). Add additional safeguards to make sure the API calls do not crash the server

// Draws a random pokecard
app.post('/pokemon/:id', async (req, res)=> {
    // Check if the trainers exists
    let trainerExist = await trainers.findOne({
        where: {
            id: req.params.id
        }
    })

    if(trainerExist == '') {
        // If not, return the error
         // Trainer does not exist in database
         res.statusCode = 400
         res.send('Trainer does not exist')
    } 
    else {
        let draw = []
        let deck = []
        // Make an API call to get a list of cards
        await axios.get('https://api.pokemontcg.io/v2/cards?q=nationalPokedexNumbers:[1 TO 151]')
        .then( async function(response) {
            for(let i = 0; i < 5; i++) {
                 // We pick at random one of the cards in the list
                let cardNum = Math.round(Math.random() * response.data.count);
    
                // Place desired card attributes into an object and add to the db
                let card = {
                    "id": response.data.data[cardNum].id,
                    "name": response.data.data[cardNum].name,
                    "type": response.data.data[cardNum].types[0],
                    "level": response.data.data[cardNum].level,
                    "hp": response.data.data[cardNum].hp,
                    "images": response.data.data[cardNum].images.large
                }
                // Check if pokemon already exists in the db
                let pokeCheck = await pokemon.findOne({
                    where: {
                        id: response.data.data[cardNum].id
                    }
                })
                // Card does not already exists
                if(pokeCheck == '') {
                    draw.push(card);
                    //Adding the id of the pokemon to our deck
                }
                deck.push(card.id)
            }
            pokemon.bulkCreate(draw);

             // Place our deck of cards in the trainer table
            trainers.update({
                deck: deck
            },
            { 
                where: {
                    id: req.params.id
                }
            })
            res.send(draw)
           
        })
        .catch(function (error) {
            // handle error
            res.statusCode = 500 // Internal Server Error
            res.send('Unable to generate cards');
        })
    } 
})   

app.delete('/pokemon/:id', async (req, res) => {
    let id = req.params.id;
    if(typeof(id) != string) {
        res.statusCode = 400 // Bad Request
        res.send('ID should be a string')
    }

    // Check that card exists in db before trying to delete
    let pokeDelete = await pokemon.findOne({
        where: {
            id: id
        }
    })

    if(pokeDelete == null) {
        res.statusCode = 400
        res.send('Card not in deck')
    } else {
    // Remove card from db
    pokemon.destroy({
        where: {
            id: id
        }
    })
    }
    res.send(pokeDelete)  
})

// Get all pokemon in your deck
app.get('/pokemon', async (req, res)=> {
    if(Object.keys(req.body) == []) {
        res.statusCode = 400
        res.send('GET request should not have body')
    } else{
        let deck = await pokemon.findAll({
            order: [
                // Orders the deck from A-Z
                ['id', 'ASC']
            ]
        });
        res.send(deck)
    }
})

app.post('/trainers', async (req, res)=> {
    trainers.create({
        id: req.body.id,
        firstname: req.body.firstname,
        lastname: req.body.lastname,
        email: req.body.email
    })
    res.send('Success')
})

app.post('/gymleaders', async (req, res)=> {
    gymleaders.create({
        name: req.body.name,
        type: req.body.type,
    })
    res.send('CREATE GYM LEADER: Success ')
})

app.post('/gymleaders/gen1', async (req, res)=> {
    gymleaders.create({
        name: 'Brock',
        type: 'Fighting',
    })
    gymleaders.create({
        name: 'Misty',
        type: 'Water',
    })
    gymleaders.create({
        name: 'Lt. Surge',
        type: 'Lightning',
    })
    gymleaders.create({
        name: 'Erika',
        type: 'Grass',
    })
    gymleaders.create({
        name: 'Koga',
        type: 'Colorless',
    })
    gymleaders.create({
        name: 'Sabrina',
        type: 'Psychic',
    })
    gymleaders.create({
        name: 'Blaine',
        type: 'Fire',
    })
    gymleaders.create({
        name: 'Giovanni',
        type: 'Colorless',
    })

    res.send('CREATE GYM LEADER from Gen1: Success ')
})

app.get('/trainers', async (req, res) => {
    let trainerList = await trainers.findAll({
        order: [
            // Orders the trainer from A-Z by lastname
            ['lastname', 'ASC']
        ]
    })

    res.send(trainerList)
})

app.post('/gymleaders/pokemon/:id', async (req, res)=> {
    let draw = []
    let deck = []
    let leaderExist = await gymleaders.findOne({
        where: {
            id: req.params.id
        }
    })
    await axios.get(`https://api.pokemontcg.io/v2/cards?q=types:${leaderExist.type}`)
        .then( async function(response) {
            
            // for(let i = 0; i < 6; i++) {
            let i = 0
            let found = false
            while(i<6){
                 // We pick at random one of the cards in the list
                let cardNum = Math.round(Math.random() * response.data.count);
                console.log(i)
                // Place desired card attributes into an object and add to the db
                let card = {
                    "id": response.data.data[cardNum].id,
                    "name": response.data.data[cardNum].name,
                    "type": response.data.data[cardNum].types[0],
                    "level": response.data.data[cardNum].level,
                    "hp": response.data.data[cardNum].hp,
                    "images": response.data.data[cardNum].images.large
                }
                // Check if pokemon already exists in the db
                let pokeCheck = await pokemon.findOne({
                    where: {
                        id: response.data.data[cardNum].id
                    }
                })

                for(j=0;j<deck.length;j++){
                    if(card.id == deck[j]){
                        found = true
                    }
                }

                // Card does not already exist
                console.log(typeof(card.level))
                console.log(card.level)
                if(pokeCheck == null && card.type == leaderExist.type && found == false) {
                    draw.push(card);
                    i++;
                    deck.push(card.id)
                    //Adding the id of the pokemon to our deck
                }

                found = false
                
            }
            pokemon.bulkCreate(draw);

             // Place our deck of cards in the trainer table
            gymleaders.update({
                deck: deck
            },
            { 
                where: {
                    id: req.params.id
                }
            })
            res.send(draw)
           
        })
})


app.listen(4000, ()=> {
    console.log('Server is running on port 4000')
})

