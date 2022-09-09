
// FRONT END
//Client - someone on a computer requesting information (the HTML) from a server; Postman is still a client
//GUI - stuff built into your computer
//Server - a computer somewhere in the world which takes in requests, authenticates clients, and sends back response to client


// BACK END (HTTP request flow)
//going to a website and wanting to change something related to our account info. Need to change it in the database
//request goes to server, which communicates with the database. the database completes the request and sends it back to the server, which sends it back to the user

//How do I make a request to any server? What does it look like?
//Typically takes the form of a JSON (JavaScript Object Notation) and looks like this:
// {"email":"fionaeckert@wustl.edu",
//     "api_key":"asdfie233",
//     "city":"Chicago"}
//Server knows what to do with a JSON because JS is built in to all browsers
//The JSON gets sent to Apple, for example, with the following address: https:apple.com/accounts
//The server then takes the email and update it
//Once it's complete, the server will either say the change was successful or failed in the format {success} or {fail}

//CRUD API - create, read, update, delete
// Post: create a enw todo
// Create: get a previously made todo
// Put: change the todo item
// Delete: delete a todo item

//MODERN API
// Create: POST - add a new resource to the server 
// Read: GET - get data back from the server
// Update: PUT - changing the attributes of an existing resource
// Delete: DELETE - delete a resource from the server

// FUNCTIONS
// POST: createTodo(description){logic}
// GET: getTodo(username){logic return}
// PUT: updateTodo(username,id){logic}
// DELETE: deleteTodo(username,id){logic}

// STATUS CODES
// 200: OK, request was received and granted
// 401: Unauthenticated - you are not someone we recognize; usually the result of having an invalid API key
// 403: Forbidden - we have verified that you are who you say you are, but you do not have permission to perform the action
// 404: Not found
// there are dozens, these are just the most common



//const displayTemp = document.getElementbyID('tempNum');
//const displayHeat = document.getElementbyID('heatNum');
// const weather = () => {
//    let currentWeather = {
        //creating current weather object to put API info into later
        // temp:0,
        // realFeel:0,
        // cloudCover:''
        // }
//     fetch('API key')
//     .then(response => {
//         // response.json() converts the response to json, which we can more easily manipulate
//         // variable "response" does not need to be called "response"
//         console.log(response.status)
//         if(response.status=='401'){
//             //can handle the error this way
//         }
//          return response.json
//          ^converts the API response to a JSON type
//     })
//      .then(data => {
        // displayTemp.innerText = Math.round(data.main.temp)
        // heatIndex.innerText=Math.rount(data.main.feels_like)
        // })


// console.log(data.main.temp))
//                      getting temperature from API
// }

// units is a query parameter, so you can put that into the API key call

// Dre created an HTML page which has a button that triggers the API call on the click

// to grab info after API is called:
// Promises - introduction into asynchronous programming; a contract in your code that promises that a variable will be assigned at some point in the future

// Promise states:
    // pending, fullfilled, cancelled
    // the promise is assigned to the variable after .then()