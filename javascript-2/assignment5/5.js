const numbers = [];

while (true) {
    const number = Number(prompt("Enter a number:"));

    if (numbers.includes(number)) {
        console.log(`Number ${number} was already given. Stopping.`);
        break;
    }

    numbers.push(number);
}

numbers.sort((a, b) => a - b);
console.log("Numbers in ascending order: ", numbers);
document.querySelector('#numbers').textContent = numbers.join(', ');