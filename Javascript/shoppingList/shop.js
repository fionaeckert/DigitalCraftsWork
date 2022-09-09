const form = document.getElementById('cerealform');
const list = document.getElementById('inStock');
const input = document.getElementById('cereal');

form.addEventListener('submit',function(event) {
    // making sure the item added by the user actually sticks in the list
    // default list is just 3 cereals so this prevents the default from taking place
    // stops webpage from reloading
    event.preventDefault();
    // creating a new element on the page when someone submits the form
    const newCereal = document.createElement('li');
    // adding submitted form item to the original list of cereals
    newCereal.innerText = cereal.value;
    list.append(newCereal);
    // reseting the form to remove the value the user entered
    form.reset();
})

