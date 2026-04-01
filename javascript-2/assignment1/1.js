let numbers = [];
for (let i = 1; i <= 5; i++) {
    numbers.push(prompt('Enter a number.'));
}
let numbersReversed = [];

for (let i = numbers.length - 1; i >= 0; i--) {
    const valueAtIndex = numbers[i];
    numbersReversed.push(valueAtIndex);
}
document.querySelector('#originalArray').textContent = numbers.join(', ');
document.querySelector('#reversedArray').textContent = numbersReversed.join(', ');