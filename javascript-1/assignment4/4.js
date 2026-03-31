const name = prompt('Enter your name.');

function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

const randomInteger = getRandomInt(4);

if (randomInteger === 0) {
    document.querySelector('#selectedHouse').innerHTML = name + ', you are Ravenclaw';
} else if (randomInteger === 1) {
    document.querySelector('#selectedHouse').innerHTML = name + ', you are Gryffindor';
} else if (randomInteger === 2) {
    document.querySelector('#selectedHouse').innerHTML = name + ', you are Hufflepuff';
} else if (randomInteger === 3) {
    document.querySelector('#selectedHouse').innerHTML = name + ', you are Slytherin';
}