// Write a function leetspeak which is given a string, and 
// returns the leetspeak equivalent of the string. To convert
// text to its leetspeak version, make the following substitutions:
// A => 4 E => 3 G => 6 I => 1 O => 0 S => 5 T => 7

let leetspeak = (word) => {
    leetspeakWord = ''
    leetspeakMap = new Map([
        ['A',4],
        ['E',3],
        ['G',6],
        ['I',1],
        ['O',0],
        ['S',5],
        ['T',7]
    ]);
    for(let i=0; i<word.length;i++){
        console.log(Object.keys(leetspeakMap).length)
    }
    return leetspeakWord
}
console.log(leetspeak('GOAT'))


// leetspeakMap = new Map([
//     ['A',4],
//     ['E',3],
//     ['G',6],
//     ['I',1],
//     ['O',0],
//     ['S',5],
//     ['T',7]
// ])

// console.log(leetspeakMap)


// COPY OVER DRE'S ANSWER

// const leetspeak = (word => {
//     let leet = ''
//     swtich(word[i].toLowerCase()){
//         case 'a':
//             leet += '4';
//     }
// })