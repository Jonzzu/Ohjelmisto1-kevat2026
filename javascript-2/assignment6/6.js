function rollDice() {
    return Math.floor(Math.random() * 6) + 1;
}


const listElement = document.querySelector('#diceRolls');
let html = '<ul>';
let roll;

do {
    roll = rollDice();
    html += `<li>${roll}</li>`;
} while (roll !== 6);

html += '</ul>';
listElement.innerHTML = html;