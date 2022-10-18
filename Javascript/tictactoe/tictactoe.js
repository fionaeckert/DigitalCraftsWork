let chai = require('chai');
let assert = chai.assert;
let expect = chai.expect;
// let should = chai.should();


board = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
console.log(board)
for(let row = 0; row <= board.length; row++){
    console.log(expect(board[row]).to.have.lengthOf(3))
}
count = 0
player = 'Player 1'
symbol = 'X'
gameOver = false
p1count = 0
p2count = 0
p1c = 1
p2c = 1

function setCord(x,y) {
    if (board[x][y] == ' ') {
        board[x][y] = symbol
        setTimeout(document.getElementById('tile'+x+y).innerText = symbol,3000)
        //count ++
        gameOver = checkWin(symbol,player)

        if (count >= 4){
            console.log(assert.equal(gameOver,true))
        }

        if (count < 9) {
            if (gameOver == false){
                if (count % 2 == 0) {
                    // player = 'Player 1'
                    // symbol = 'X'
                    // alert(player+' turn')
                    count ++
                    comp()
                }
           
                // else {
                //     player = 'Player 2'
                //     symbol = 'O'
                //     alert(player+' turn')
                // }
            }
            else if (gameOver == true) {
                if (player == 'Player 1'){
                    p1count++
                    console.log('Player wins: ', p1count)
                    document.getElementById('player1').innerText = 'Player 1: X Wins: ' + p1count
                    console.log(assert.equal(p1count, p1c++,'p1 count increased by 1'))
                }
                else if(player == 'Computer'){
                    p2count++
                    document.getElementById('player2').innerText = 'Player 2: O Wins: ' + p2count
                    console.log(assert.equal(p2count, p2c++,'p2 count increased by 1'))
                }
            }  
        }
        else {
            alert('Tie')
        }
        
    }
    
}

function checkWin(sym, play) {
    if (sym == board[0][0] && sym == board[0][1] && sym == board[0][2]){
        alert(play + " has won!")
        return true
    }
    else if (sym == board[1][0] && sym == board[1][1] && sym == board[1][2]){
        alert(play + " has won!")
        return true
    }
    else if (sym == board[2][0] && sym == board[2][1] && sym == board[2][2]){
        alert(play + " has won!")
        return true
    }
    else if (sym == board[0][0] && sym == board[1][0] && sym == board[2][0]){
        alert(play + " has won!")
        return true
    }
    else if (sym == board[0][1] && sym == board[1][1] && sym == board[2][1]){
        alert(play + " has won!")
        return true
    }
    else if (sym == board[0][2] && sym == board[1][2] && sym == board[2][2]){
        alert(play + " has won!")
        return true
    }
    else if (sym == board[0][0] && sym == board[1][1] && sym == board[2][2]){
        alert(play + " has won!")
        return true
    }
    else if (sym == board[2][0] && sym == board[1][1] && sym == board[0][2]){
        alert(play + " has won!")
        return true
    }
    else {
        return false
    }
}


function reset() {
    board = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
    count = 0
    player = 'Player 1'
    symbol = 'X'  
    gameOver = false
    document.getElementById('tile00').innerText = ' '
    document.getElementById('tile01').innerText = ' '
    document.getElementById('tile02').innerText = ' '
    document.getElementById('tile10').innerText = ' '
    document.getElementById('tile11').innerText = ' '
    document.getElementById('tile12').innerText = ' '
    document.getElementById('tile20').innerText = ' '
    document.getElementById('tile21').innerText = ' '
    document.getElementById('tile22').innerText = ' '

}

function comp() {
    player = 'Computer'
    symbol = 'O'

    xAxis = Math.round(Math.random() * (2))
    yAxis = Math.round(Math.random() * (2))

    while (board[xAxis][yAxis] !=  ' '){
        xAxis = Math.round(Math.random() * (2) )
        yAxis = Math.round(Math.random() * (2) ) 
    }

    // setTimeout async(setCord(xAxis,yAxis),3000)
    setCord(xAxis,yAxis)
    if (gameOver == false) {
        count ++
        player = 'Player 1'
        symbol = 'X'
    // alert(player+' turn')
    }
}
//--------------------------------------------------------------------------------------------------------------------------------------------
// 3 unit tests:
// player counts
// check for infinite loop
// check for "game over == True" when game is over
// let assert = require('chai').assert;
// let greeting = 'hello'
// console.log(assert.typeOf(greeting, 'string'))



