const API_KEY = "553fd07e8b09de09928ffdec025423c8";

function onGeoOk(position) {
  const lat = position.coords.latitude;
  const lon = position.coords.longitude;
  const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`;
  fetch(url).then((response) =>
    response.json().then((data) => {
      const weather = document.querySelector("#weatherContainer #weather");
      const city = document.querySelector("#weatherContainer #city");
      const cityName = data.name;
      const weatherState = data.weather[0].main;
      const tempC = Math.round(data.main.temp);
      weather.innerHTML = `${weatherState} @ ${tempC} °C`;
      city.innerHTML = cityName;
    })
  );
}
function onGeoError() {
  alert("Can't find you. No weather for you.");
}

navigator.geolocation.getCurrentPosition(onGeoOk, onGeoError);
