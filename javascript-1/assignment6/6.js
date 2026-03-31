let answer = confirm('Should I calculate the square root?');
if (answer === true) {
    let number = prompt('Give a number')
    number = Number(number);
    if (number < 0) {
        document.querySelector('#answer').innerHTML = 'The square root of a negative number is not defined'
    } else {
        let squareRoot = number ** 0.5;
        document.querySelector('#answer').innerHTML = 'The square root of ' + number + ' is: ' + squareRoot;
    }} else {
    document.querySelector('#answer').innerHTML = 'The square root is not calculated.'
}