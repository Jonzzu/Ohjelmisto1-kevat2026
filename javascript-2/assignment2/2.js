const numberOfParticipants = Number(prompt('Give number of participants'));
let namesOfParticipants = [];

for (let n = numberOfParticipants; n > 0; n--) {
    namesOfParticipants.push(prompt('Give participant name.'));
}

let sortedNamesOfParticipants = namesOfParticipants.slice(); // copy, not reference
sortedNamesOfParticipants.sort();

const listElement = document.querySelector('#sortedParticipants');

let html = '<ul>';
for (const name of sortedNamesOfParticipants) {
    html += `<li>${name}</li>`;
}
html += '</ul>';

listElement.innerHTML = html;
