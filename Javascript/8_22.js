// This is a JS comment
/* This is block comment in JS
ASDD 
HEYO 
STILL GOIN!
*/

/* JS Types
    number,
    string,
    boolean,
    object,
    array,
    date
*/

// Always put semi colons

// This is how you declare a variable
var fullName = 'Fiona Eckert';
console.log(fullName);

// This is how you declare a variable with modern JS
let city = 'Chicago';

// In JS we must declare our constants. Constants cannot be changed once instantiated
const PI = 3.14;



// Javascript uses the number class instead of integer, there are no floats
console.log(typeof(35));
console.log(typeof(3.12233));

//Booleans are lower case
isRaining = false

// Working with arrays in JS
let scores = [3,5,2,8]
console.log(scores);
// Length function belongs to array class. To find the length of an array, use the length method that belongs to the array class.
console.log(scores.length);


// Objects -- use curly braces; as opposed to printing out where in the computer the object lives, the console.log argument will print the contents of the object
let player = {
    name:"Tim Bo Bim",
    number:17,
    position:"Shortstop",
    IR: false    
};
console.log(player);

// Access a property within an object 
console.log(player.name)
//prints Tim Bo Bim

// JS has a built-in Date type; we use the keyword 'new' to declare a new instance of a class
let todaysDate = new Date();
console.log(todaysDate);

// JS Functions have a different keyword (function)
function salutations(username){
    console.log('Hello', username)
}

salutations('Fiona')

function salutations1(username){
    return 'Hello '+username
}
console.log(salutations1('Fiona'))

// String concatenation
fullName = 'Fiona' + 'Eckert'

// String interpolation
let month = 'August';
let date = 22;
let year = 2022;
console.log(`Today is ${month} ${date}, ${year}`)

// JS has incrementors/decrementors
let count = 0;
count++;
count++;
count--;
count+=4;
console.log('Count: ', count)

// Keywords such as 'and', 'or', etc do NOT exist. Must use operators in order to write expression
// If statements need parentheses 
// Check if it is raining and the month is August
if(isRaining && month =='August'){
    console.log(`We're in the dog days of summer.`)
}

// Check if it's sunny OR if the year is 2022
if(isRaining==false || year == 2022){
    console.log(`No time like the present.`)
}
// Does same thing as checking if is Raining is false: if(!isRaining)

// Difference between == and ===
// Loose comparison: ==
// Strict comparison: ===; checks not only the value but the type

console.log(5%2); // returns 1
console.log(5/2); // returns 2.5

// Conditional statements

if (!isRaining){
    console.log('You can go outside.')
} else if  (!isRaining) {
    console.log('It is raining, stay inside.')
}

// Switch statement - typically used when you have a number of conditions to check
let day = new Date().getDay();
console.log(day)
switch (day) {
    case 0:
        console.log('Sunday Scarries')
        break;
    case 1:
        console.log('Hating today')
        break;
    case 2:
        console.log('Worst day of the week')
        break;
    case 3:
        console.log('Getting better')
        break;
    case 4:
        console.log('LETS GOOOOO almost Friday')
        break;
    case 5:
        console.log('OH YEAH NO THOUGHTS JUST VIBES')
        break;
    case 6:
        console.log('La la laaaa Saturdayyyyyy')
        break;
    default:
        console.log('Enter a valid day of the week.')
}
// Looping 
let days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
// For loops
for(let i = 0; i < days.length; i++) {
    console.log(days[i]);
}
// Loops don't know when to begin and when to end. We use variables and declare variables to determine that.
// In the above example, i is the variable. Each group of characters before a semicolon is an argument.
// Break condition is in the middle.
// Incrementor is on the right.

// While loops
let i = 0;
while(i < days.length) {
    console.log(days[i]);
    i++;
}

// Iterate days of week in reverse
for(let i = days.length-1; i>=0; i--) {
    console.log(days[i]);
}

// Print every day of the week that falls on an odd index
for(let i = 0; i < days.length;i++){
    if(i%2==1){
        console.log(days[i]);
    }
}
// Below does the same as above
for(let i = 1; i < days.length;i+=2){
    console.log(days[i]);
}

// When given two strings from the user, write a function that checks if each string is an anagram of the other. If yes, return true, otherwise false

function sortList(word) {
    word = word.toLowerCase();
    word = word.split("");
    word = word.sort();
    //console.log(word);
    return word;
    
    
}

function isAnagram(word1,word2) {
    word1 = sortList(word1);
    word2 = sortList(word2);
    
    word1 = word1.toString();
    word2 = word2.toString();

    console.log(word1);
    console.log(word2);


    if (word1 === word2) {
        return "is an Anagram";
    } 
    else if (word1 !==  word2) {
        return "is not an Anagram";
    }
}

// let firstword = window.prompt("Enter a word.");
// let secondword = window.prompt("Enter a word.");

console.log(isAnagram('dog','god'));


// FOR HW: EXPLORE JS LIBRARY AND FIGURE OUT WHAT IS MOST SIMILAR TO A DICTIONARY

dict = {1:'hello',2:'hey'}
console.log(dict[1])
