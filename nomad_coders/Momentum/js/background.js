const images = ["0.jpg", "1.jpg"];

const chosenImage = images[Math.floor(Math.random() * images.length)];

// const bgImage = document.createElement("img");

// bgImage.src = `./img/${chosenImage}`;
// document.body.appendChild(bgImage);

const bgWrap = document.querySelector("#wrap");
bgWrap.style.backgroundImage = `url(./img/${chosenImage})`;
bgWrap.style.backgroundSize = "cover";
