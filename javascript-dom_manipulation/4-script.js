document.addEventListener('DOMContentLoaded', function() {
  const addItemButton = document.getElementById('add_item');
  
  addItemButton.addEventListener('click', function() {
    const myList = document.querySelector('.my_list');
    const newListItem = document.createElement('li');
    newListItem.textContent = 'Item';
    myList.appendChild(newListItem);
  });
});
