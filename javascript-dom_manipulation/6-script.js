document.addEventListener('DOMContentLoaded', function() {
  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      const characterElement = document.getElementById('character');
      characterElement.textContent = data.name;
    })
    .catch(error => {
      console.error('There was a problem with the fetch operation:', error);
    });
});
