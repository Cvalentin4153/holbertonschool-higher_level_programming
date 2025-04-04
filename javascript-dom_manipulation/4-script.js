document.addEventListener('DOMContentLoaded', function() {
  const addItemButton = document.getElementById('add_item');
  
  addItemButton.addEventListener('click', function() {
    const myList = document.querySelector('.my_list');
    
    // Create a new li element
    const newListItem = document.createElement('li');
    newListItem.textContent = 'Item';
    
    // Add the new li element to the ul with class my_list
    myList.appendChild(newListItem);
  });
});
