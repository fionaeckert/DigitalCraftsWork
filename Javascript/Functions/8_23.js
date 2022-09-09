// Basic function
function area(length, width) {
    return length * width;
}

// several ways to write a function in JS
// Arrow function - called more often than basic function above
let circumference = (radius) => {
    const PI = 3.14
    return PI * (radius^2)
}
circumference(5)

//Anonymous function
const sum = function(number1,number2){
    return number1 + number2
}
sum(4,5)


//Anonymous function - will only run code in block
() => {
    console.log('Fona')   
}