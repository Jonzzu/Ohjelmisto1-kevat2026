const calculationInput = document.getElementById('calculation');
const calculateButton = document.getElementById('start');
const resultParagraph = document.getElementById('result');

calculateButton.addEventListener('click', () => {
    const input = calculationInput.value;
    let result;

    if (input.includes('+')) {
        const [num1, num2] = input.split('+').map(Number);
        result = num1 + num2;
    } else if (input.includes('-')) {
        const [num1, num2] = input.split('-').map(Number);
        result = num1 - num2;
    } else if (input.includes('*')) {
        const [num1, num2] = input.split('*').map(Number);
        result = num1 * num2;
    } else if (input.includes('/')) {
        const [num1, num2] = input.split('/').map(Number);
        result = num1 / num2;
    } else {
        result = 'Calculation failed';
    }

resultParagraph.textContent = `Result: ${result}`;
});