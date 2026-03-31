const year = prompt('Enter a year');
if (year % 400 === 0 || year % 100 !== 0 && year % 4 === 0) {
    document.querySelector('#leapYear').innerHTML = year + ' is a leap year!';
} else {
    document.querySelector('#leapYear').innerHTML = year + ' is not a leap year!';
}