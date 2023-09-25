const button = document.getElementById('button');
const hidden = document.getElementById('hidden');

function populateText() {
    hidden.textContent = 'WoW!'
    hidden.style.color = 'red'
    hidden.style.fontSize = 30
}

button.addEventListener('click', populateText);
