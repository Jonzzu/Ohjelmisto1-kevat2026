function isPrime(n) {
    if (n < 2) return false;

    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) return false;
    }

    return true;
}
let number = Number(prompt('Give integer.'));

if (isPrime(number)) {
    document.querySelector('#isPrime').innerHTML = number + ' is a prime number.'
} else {
    document.querySelector('#isPrime').innerHTML = number + ' is not a prime number.'
}