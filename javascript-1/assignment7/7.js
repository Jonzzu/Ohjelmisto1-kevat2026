const rolls = Number(prompt('How many dices to roll?'));
let sum = 0;

for (let i = 0; i < rolls; i++) {
    let roll = Math.floor(Math.random() * 6) + 1;
    sum += roll;
}
document.querySelector('#sumOfDices').innerHTML = 'The sum of ' + rolls + ' dices is ' +sum;