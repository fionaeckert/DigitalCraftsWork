const dealerHand = document.getElementById("dealerHand");
const playerHand = document.getElementById("playerHand");

const dealButton = document.getElementById('dealButton')
const hitButton = document.getElementById('hitButton')
// console.log(dealButton)

var suits = ["spades", "diamonds", "clubs", "hearts"];
var values = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"];
let deck = new Array();

let dealerCardsValue = 0;
let playerCardsValue = 0;

function buildDeck(){
	

	for(let i = 0; i < suits.length; i++)
	{
		for(let x = 0; x < values.length; x++)
		{
			let card = {Value: values[x], Suit: suits[i]};
			deck.push(card);
		}
	}

	return deck;
}
buildDeck()
// console.log(buildDeck)
console.log(deck[Math.round(Math.random()*51)])

// let newCardTest = deck[Math.round(Math.random()*51)]
// console.log(newCardTest)
// let cardTest = `${newCardTest.Value}_of_${newCardTest.Suit}.png`
// console.log(cardTest)
// const cardPath = "./PNG-cards-1.3/"
// let imgCardMakeTest = cardPath + cardTest
// console.log(imgCardMakeTest)


//let newCardTest = deck[Math.round(Math.random()*51)]
//let cardTest = `${newCardTest.Value}_of_${newCardTest.Suit}.png`

// function makeCardDisplay(){
//   let newCardTest = deck[Math.round(Math.random()*51)];
//   let cardTest = `${newCardTest.Value}_of_${newCardTest.Suit}.png`;
//   const cardPath = "./PNG-cards-1.3/";
//   let imgCardMakeTest = cardPath + cardTest;
//   return imgCardMakeTest;
// }
// function getPlayerPoints(cardValue){
//   playerCardsValue += playerCardsValue +cardValue

//   return playerCardsValue

// }




// function shuffleDeck() {
//   for (let i = 0; i < deck.length; i++) {
//       let j = Math.floor(Math.random() * deck.length); 
//       let temp = deck[i];
//       deck[i] = deck[j];
//       deck[j] = temp;
//   }
//   console.log(deck);
// }
// shuffleDeck()

dealButton.addEventListener("click", function (event) {
  event.preventDefault();
  deal()
});
 
function deal() {
  for (let i = 0; i < 2; i ++){
  const newDeal = document.createElement("img");
  let newCardTest = deck[Math.round(Math.random()*51)]
  let cardTest = `${newCardTest.Value}_of_${newCardTest.Suit}.png`
  const cardPath = "./PNG-cards-1.3/"
  let imgCardMakeTest = cardPath + cardTest
  newDeal.src = imgCardMakeTest;
  const card = document.getElementById("dealerCard");
  newDeal.className = "card";
  dealerHand.append(newDeal);

    // const newCard = document.createElement("img");
    // newCard.src = imgCardMakeTest;
    // //newCard.src = "./PNG-cards-1.3/2_of_clubs.png";
    // // newCard.src = cardPath + cardTest;
    // const card = document.getElementById("dealerCard");
    // newCard.className = "card";
    // x=buildDeck();
    // x.shift();
    // dealerHand.append(newCard);
    // //console.log(dealerHand);
    // console.log(x.shift())
  }
  for (let j = 0; j < 2; j++){
    const newDeal = document.createElement("img");
    let newCardTest = deck[Math.round(Math.random()*51)]
    let cardTest = `${newCardTest.Value}_of_${newCardTest.Suit}.png`
    const cardPath = "./PNG-cards-1.3/"
    let imgCardMakeTest = cardPath + cardTest
    newDeal.src = imgCardMakeTest;
    const card = document.getElementById("playerCard");
    newDeal.className = "card";
    playerHand.append(newDeal);

    // const newCard = document.createElement("img");
    // newCard.src = imgCardMakeTest;
    // //newCard.src = "./PNG-cards-1.3/2_of_clubs.png";
    // const card = document.getElementById("playerCard");
    // newCard.className = "card";
    // x=buildDeck();
    // x.shift();
    // playerHand.append(newCard);
    // //console.log(playerHand)
    // console.log(x.shift())
  }

  
  //console.log(newCard.src);
}
 

hitButton.addEventListener("click", function (event) {
  event.preventDefault();
  hit()
});

function hit() {{
  const newHit = document.createElement("img");
  let newCardTest = deck[Math.round(Math.random()*51)]
  let cardTest = `${newCardTest.Value}_of_${newCardTest.Suit}.png`
  const cardPath = "./PNG-cards-1.3/"
  let imgCardMakeTest = cardPath + cardTest
  newHit.src = imgCardMakeTest;
  const card = document.getElementById("dealerCard");
  newHit.className = "card";
  dealerCard.append(newHit);
}
{
  const newHit = document.createElement("img");
  let newCardTest = deck[Math.round(Math.random()*51)]
  let cardTest = `${newCardTest.Value}_of_${newCardTest.Suit}.png`
  const cardPath = "./PNG-cards-1.3/"
  let imgCardMakeTest = cardPath + cardTest
  newHit.src = imgCardMakeTest;
  
  
  newHit.src = imgCardMakeTest;
  const card = document.getElementById("playerCard");
  newHit.className = "card";
  playerCard.append(newHit);
}
}
 
function getValue() {  /// Is this a parameter?
  let value = `${newCardTest.Value}`;
  if (isNaN(value)) {
    if (value == "ace") {
      return 11;
    }
    return 10;
  }
  console.log(value)
}
getValue()







          
// function dealButton() {
//   let img = document.createElement('img');
//   img.src = "./PNG-cards-1.3/9_of_clubs.png"
//   document.getElementById('playersHand').appendChild(img); 
// } 


// const deck = [];
// const suits = ["hearts", "spades", "clubs", "diamonds"];
// const ranks = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"];
// const makeDeck = (rank, suit) => {
//   const card = {
//     rank: rank,
//     suit: suit,
//     pointValue: rank > 10 ? 10 : rank,
//   };
//   deck.push(card);
// };

// for (let suit of suits) {
//   for (const rank of ranks) {
//     makeDeck(rank, suit);
//   }
// }

// var deck;

// function buildDeck() {
//   const suits = ["hearts", "spades", "clubs", "diamonds"];
//   const ranks = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"];
//   deck = [];

//   for (let i=0, i < suits.length; i++) { // For each suits
//     for (let j=0; j < ranks.length; j++) { // For each ranks
//       deck.push(ranks[j] + "_of_" + suits.[i]); // Create an arry of each card, named in that img filename format
//     }
//   }
// }

// function shuffleDeck () {
//   for (let i=0, i < deck.length, i++) {
//     let j = Math.floor(Math.random() * deck.length);
//     let tempDeck = deck[i];
//     deck[i] = deck[j];
//     deck[j] = tempDeck
//   }
// }

// window.addEventListener("DOMContentLoaded", () => {
//   // Execute after page load
// });

// fuction calc
