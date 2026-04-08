let numbers = [];
let number;

while (number !== 0) {
    number = Number(prompt('Enter a number. 0 stops.'));
    if (number !== 0) numbers.push(number);
}

numbers.sort((a, b) => a - b);
numbers.reverse()
console.log(numbers);

const listElement = document.querySelector('#sortedNumbers');

let html = '<ul>';
for (const number of numbers) {
    html += `<li>${number}</li>`;
}
html += '</ul>';

listElement.innerHTML = html;