const num1Input = document.getElementById('num1');
const num2Input = document.getElementById('num2');
const operationSelect = document.getElementById('operation');
const calculateButton = document.getElementById('start');
const results = document.getElementById('result');

calculateButton.addEventListener('click', () => {
    const num1 = Number(num1Input.value);
    const num2 = Number(num2Input.value);
    const operation = operationSelect.value;

    let result;

    if (operation === 'add') {
        result = num1 + num2;
    } else if (operation === 'sub') {
        result = num1 - num2;
    } else if (operation === 'multi') {
        result = num1 * num2;
    } else if (operation === 'div') {
        result = num2 !== 0 ? num1 / num2 : "Can't divide by 0."
    }

    results.textContent = `Result: ${result}`;
});