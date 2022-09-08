const momentum = document

const loginContainer = momentum.querySelector("#loginContainer");
const weatherContainer = momentum.querySelector("#weatherContainer");
const clockContainer = momentum.querySelector("#clockContainer");
const todoContainer = momentum.querySelector("#todoContainer");
const quoteContainer = momentum.querySelector("#quoteContainer");
const greeingContainer = momentum.querySelector("#greeingContainer");

const greeting = momentum.querySelector("#greeting");
const loginForm = momentum.querySelector("#login-form");
const loginInput = loginForm.querySelector("input");

const HIDDEN_CLASSNAME = "hidden";
const USERNAME_KEY = "username";



function onLoginSubmit(event) {
    event.preventDefault();
    const username = loginInput.value;
    localStorage.setItem(USERNAME_KEY, username);
    loginContainer.classList.add(HIDDEN_CLASSNAME);
    paintGreetings(username);
}

function paintGreetings(username) {
    greeting.innerHTML = `Hello, ${username}.`;
    greeingContainer.classList.remove(HIDDEN_CLASSNAME);
    weatherContainer.classList.remove(HIDDEN_CLASSNAME);
    clockContainer.classList.remove(HIDDEN_CLASSNAME);
    todoContainer.classList.remove(HIDDEN_CLASSNAME);
    quoteContainer.classList.remove(HIDDEN_CLASSNAME);
}


const savedUsername = localStorage.getItem(USERNAME_KEY);

if(savedUsername === null){
    loginContainer.classList.remove(HIDDEN_CLASSNAME);
    loginForm.addEventListener("submit", onLoginSubmit);
} else {
    paintGreetings(savedUsername);
}

