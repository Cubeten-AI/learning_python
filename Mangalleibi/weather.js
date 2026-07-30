const readline = require("readline");

const apiKey = "69b28e9ac1534b9681f70927262907";

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

async function getWeather(city) {
    const url = `https://api.weatherapi.com/v1/current.json?key=${apiKey}&q=${city}&aqi=yes`;

    try {
        const response = await fetch(url);
        const data = await response.json();

        if (data.error) {
            console.log("\n❌ " + data.error.message);
            askAgain();
            return;
        }

        console.log("\n========== WEATHER REPORT ==========");
        console.log("City       :", data.location.name);
        console.log("Region     :", data.location.region);
        console.log("Country    :", data.location.country);
        console.log("Temperature:", data.current.temp_c + " °C");
        console.log("Condition  :", data.current.condition.text);
        console.log("Humidity   :", data.current.humidity + "%");
        console.log("Wind Speed :", data.current.wind_kph + " km/h");
        console.log("Feels Like :", data.current.feelslike_c + " °C");
        console.log("Pressure   :", data.current.pressure_mb + " mb");
        console.log("UV Index   :", data.current.uv);
        console.log("====================================");

        askAgain();

    } catch (err) {
        console.log("Error:", err.message);
        askAgain();
    }
}

function askAgain() {
    rl.question("\nDo you want to search another city? (yes/no): ", (answer) => {
        if (answer.toLowerCase() === "yes") {
            askCity();
        } else {
            console.log("\nThank you for using the Weather App!");
            rl.close();
        }
    });
}

function askCity() {
    rl.question("\nEnter city name: ", (city) => {
        getWeather(city);
    });
}

console.log("========== WEATHER APP ==========");
askCity();