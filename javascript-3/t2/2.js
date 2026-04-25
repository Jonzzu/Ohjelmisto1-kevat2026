const element1 = document.createElement('li');
element1.textContent = 'First item';

const element2 = document.createElement('li');
element2.textContent = 'Second item';

const element3 = document.createElement('li');
element3.textContent = 'Third item';

const target = document.getElementById('target');
target.appendChild(element1);
target.appendChild(element2);
target.appendChild(element3);