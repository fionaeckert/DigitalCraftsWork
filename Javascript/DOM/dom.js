// // Maps - similar to a dictionary; technically a hashmap
// let map1 = new map ();
// let map2 = new map ();

// Dom is where JS shines

 // <-- allows you to write JS within HTML, not recommended because difficult to track -->
//  console.log('Inside our HTML file')
//  const headerElement = document.querySelector('h1');
//  const navList = document.getElementById('nav-list');
//  console.log(headerElement);
//  console.log(headerElement.innerText);
 
//  const username = document.getElementsByName('username');
//  console.log(username);
//  const links = document.getElementsByClassName('link');
//  console.log(links); //returns collection of links
//  console.log(links[0].innerText) //returns specific link

//  function alertUser(){
//      alert('You have clicked the login button.')
//  };



 function getUserInfo(){
    username = document.getElementById('username').value;
    password = document.getElementById('password').value;
    login = document.getElementsByTagName('button');
    // adding event listener to log in button
    login[0].addEventListener('click',checkPassword);
    console.log(`Username: ${username}, Password: ${password}`);
    checkUsername(username);
    console.log(checkUsername(username));
    checkPassword(username,password);
    }

// you should be checking for these things both on the front end and back end
// function checkUsername(username) {
//     let myRegex = /^[A-Za-z]$/
//     return myRegex.test(username)
// }


 function checkPassword(username,password){
    let mockDb = new Map();
    mockDb.set = ('fionaeckert','password123')
    // Checking to see if the username is in the database
    // Username was not found
    if(mockDb.get(username) == undefined) {
        alert('No account found with that username.')
    // Check if password matches what is in the db.
    } else if(mockDb.get(username) == password) {
        alert('You are signed in.')
    // Username exists but password is wrong
    } else {
        alert('Wrong password.')
    }
 }

 function createUser(username,password,){
    let mockDb = new Map();
    passwordRegex = /^[A-Za-z0-9]+$/
    // checks if username length is > 0
    if(username.length == 0){
        console.log('Must type in valid username')
    } 
    // checks if password meets minimum combination of characters
    else if(!passwordRegex.text('password')){
        console.log('Must use letters and numbers for password.')
    }
    newuser = {'username':username, 'password':password, 'country':country}
 }