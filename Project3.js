document.addEventListener('DOMContentLoaded', () =>{
let homeButton = document.getElementById('home');
let animalButton= document.getElementById('animal');
let contactButton = document.getElementById('contact');
let home = document.getElementById('Home_Menu');
let animal = document.getElementById('Animal_List');
let contact = document.getElementById('Contact_Us');
let switching = document.getElementById('light-mode');
let light = document.getElementById('light-dark');
let turnOn = 1;

var x = window.matchMedia("(max-width: 500px)");
x.addEventListener("scroll", Queries(x));

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
function LightDark(change){
    if(turnOn == 0){
        change.setAttribute("href", "LightMode.css");
        turnOn = 1;
    }
    else{
        change.removeAttribute("href");
        turnOn = 0;
    }
}


function Queries(x){
    if(x.matches){
        var prevScrollpos = window.pageYOffset;
        window.onscroll = function() {
            var currentScrollPos = window.pageYOffset;
            if (prevScrollpos > currentScrollPos) {
                document.getElementById("red").style.top = "0";
            } else {
                document.getElementById("red").style.top = "-200px";
            }
            prevScrollpos = currentScrollPos;
        }
    }
}


switching.addEventListener('click', () => LightDark(light));
    
homeButton.addEventListener('click', () => ChangeScreens(home, animal, contact));
animalButton.addEventListener("click", () => ChangeScreens(animal, home, contact));
contactButton.addEventListener('click', () => ChangeScreens(contact, animal, home));
})