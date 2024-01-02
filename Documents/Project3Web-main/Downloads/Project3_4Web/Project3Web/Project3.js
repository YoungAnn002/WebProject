document.addEventListener('DOMContentLoaded', () =>{
let homeButton = document.getElementById('home');
let animalButton= document.getElementById('animal');
let contactButton = document.getElementById('contact');
let home = document.getElementById('Home_Menu');
let animal = document.getElementById('Animal_List');
let contact = document.getElementById('Contact_Us');

console.log(home, animal, contact);

function ChangeScreens(show, hide1, hide2){
    console.log("I work!");
    window.scroll({
        top:0, left:0, behavior:"smooth"
    });
    show.style = 'display: block';
    hide1.style = 'display: none';
    hide2.style = 'display: none';
}

    
homeButton.addEventListener('click', () => ChangeScreens(home, animal, contact));
animalButton.addEventListener("click", () => ChangeScreens(animal, home, contact));
contactButton.addEventListener('click', () => ChangeScreens(contact, animal, home));
})