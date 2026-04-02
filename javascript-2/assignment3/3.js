const dogs = [];
for (let i = 1; i < 7; i++) {
    dogs.push(prompt('Anna koiran numero ' + i + ' nimi.'));
}
const sortedDogs = dogs.slice();
sortedDogs.sort()
sortedDogs.reverse()

const listElement = document.querySelector('#sortedDogs');

let html = '<ul>';
for (const dog of sortedDogs) {
    html += `<li>${dog}</li>`;
}
html += '</ul>';

listElement.innerHTML = html;