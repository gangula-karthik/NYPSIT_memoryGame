function revealCard(card) {
    const front = card.querySelector('.card-front');
    const back = card.querySelector('.card-back');

    front.style.display = 'block';
    back.style.display = 'none';
}


let timeRemaining = 60; // Time remaining in seconds
let gameEnded = false; // Flag to keep track of game state

function endGame(message, successful) {
gameEnded = true;
alert(message);
clearInterval(timerInterval); // Stop the timer

if (successful) {
// Prompt for the username and admin number
const username = window.prompt("Please enter your username");
const adminNumber = window.prompt("Please enter your admin number");

// Send the time to the server
const timeTaken = 60 - timeRemaining;
fetch('/record-time', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        name: username,
        adminNumber: adminNumber,
        score: timeTaken
    }),
})
.then(response => response.json())
.then(data => console.log(data))
.catch((error) => console.error('Error:', error));

// Redirect to the leaderboard
window.location.href = '/';
} else {
// Redirect to the homepage
window.location.href = '/';
}
}



let timerInterval = setInterval(() => {
timeRemaining--;

// Display the time remaining
document.getElementById('timer').textContent = `Time remaining: ${timeRemaining} seconds`;

// Check if the time is up
if (timeRemaining <= 0) {
    endGame('Time is up!', false);
}


if (Array.from(allCards).every(card => card.classList.contains('matched'))) {
    endGame('Congratulations! You have matched all cards.', true);
}
}, 1000);

let selectedCards = [];

function flipCard(card) {
const allCards = document.querySelectorAll('.card');

if (gameEnded || card.classList.contains('matched') || selectedCards.length >= 2) {
// Don't allow flipping a matched card or flipping more than two cards at once, or if game has ended
return;
}

card.classList.toggle('flipped');

if (card.classList.contains('flipped')) {
selectedCards.push(card);
} else {
selectedCards = selectedCards.filter(c => c !== card);
}

if (selectedCards.length === 2) {
// Check for a match
const match1 = selectedCards[0].getAttribute('data-match');
const match2 = selectedCards[1].getAttribute('data-match');

if (match1 === match2) {
    // It's a match
    selectedCards.forEach(c => {
        c.classList.add('matched');
        c.classList.remove('flipped');
    });
    selectedCards = []; // Clear the selectedCards array

    // Check if all cards are matched
    if (Array.from(allCards).every(card => card.classList.contains('matched'))) {
        endGame('Congratulations! You have matched all cards.', true);
    }

} else {
    // It's not a match
    setTimeout(() => {
        selectedCards.forEach(c => {
                c.classList.remove('flipped');
            });
        selectedCards = []; // Clear the selectedCards array
    }, 1000);
}
}
}

