let tg = window.Telegram.WebApp;

// Appni to‘liq ekran qilish
tg.expand();

// OpenWeather API kaliti
const API_KEY = "4c6858dd3be683e4f9e22545fdbf7ebd";

// Ob-havo olish funksiyasi
async function getWeather(city = "Tashkent") {
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_KEY}&units=metric`;

    const response = await fetch(url);
    const data = await response.json();

    return data;
}

// Tugma bosilganda
document.getElementById("btn").addEventListener("click", async () => {
    const weather = await getWeather("Tashkent");

    const message = `
Shahar: ${weather.name}
Harorat: ${weather.main.temp}°C
Namlik: ${weather.main.humidity}%
Ob-havo: ${weather.weather[0].description}
    `;

    // Mini App → Python botga yuborish
    tg.sendData(message);
});
