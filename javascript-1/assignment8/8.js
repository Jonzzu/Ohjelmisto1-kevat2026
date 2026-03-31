let yearStart = Number(prompt('Give a start year'));
let endYear = Number(prompt('Give an end year.'));

let leapYears = [];

for (let y = yearStart; y <= endYear; y++) {
    if (y % 400 === 0 || (y % 100 !== 0 && y % 4 === 0)) {
        leapYears.push(y);
    }
}

const listElement = document.querySelector('#leapYears');


let html = '<ul>';
for (const year of leapYears) {
    html += `<li>${year}</li>`;
}
html += '</ul>';

listElement.innerHTML = html;