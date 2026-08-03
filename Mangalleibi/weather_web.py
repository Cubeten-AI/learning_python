<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Weather App</title>

<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Arial, Helvetica, sans-serif;
}

body{
    background:linear-gradient(135deg,#4facfe,#00f2fe);
    display:flex;
    justify-content:center;
    align-items:center;
    height:100vh;
}

.container{
    background:white;
    width:380px;
    padding:25px;
    border-radius:15px;
    box-shadow:0 10px 20px rgba(0,0,0,0.3);
    text-align:center;
}

h1{
    color:#333;
    margin-bottom:20px;
}

input{
    width:75%;
    padding:10px;
    border:2px solid #4facfe;
    border-radius:8px;
    font-size:16px;
    outline:none;
}

button{
    padding:10px 15px;
    border:none;
    background:#4facfe;
    color:white;
    border-radius:8px;
    cursor:pointer;
    font-size:16px;
    margin-left:5px;
}

button:hover{
    background:#2196f3;
}

.weather{
    margin-top:25px;
    display:none;
}

.weather img{
    width:80px;
}

.weather h2{
    margin:10px 0;
    color:#333;
}

.data{
    text-align:left;
    margin-top:15px;
    font-size:18px;
}

.data p{
    margin:8px 0;
}

.error{
    color:red;
    margin-top:15px;
}
</style>

</head>
<body>

<div class="container">

<h1>🌤 Weather App</h1>

<input type="text" id="city" placeholder="Enter City Name">
<button onclick="getWeather()">Search</button>

<div class="error" id="error"></div>

<div class="weather" id="weather">

<img id="icon">

<h2 id="location"></h2>

<div class="data">
<p><b>Temperature:</b> <span id="temp"></span> °C</p>
<p><b>Condition:</b> <span id="condition"></span></p>
<p><b>Humidity:</b> <span id="humidity"></span>%</p>
<p><b>Wind:</b> <span id="wind"></span> km/h</p>
<p><b>Feels Like:</b> <span id="feels"></span> °C</p>
<p><b>Pressure:</b> <span id="pressure"></span> mb</p>
<p><b>UV Index:</b> <span id="uv"></span></p>
<p><b>Country:</b> <span id="country"></span></p>
</div>

</div>

</div>

<script>

const apiKey = "69b28e9ac1534b9681f70927262907";

async function getWeather(){

    let city = document.getElementById("city").value.trim();

    if(city==""){
        alert("Please enter a city name.");
        return;
    }

    let url=`https://api.weatherapi.com/v1/current.json?key=${apiKey}&q=${city}&aqi=yes`;

    try{

        let response=await fetch(url);
        let data=await response.json();

        if(data.error){
            document.getElementById("weather").style.display="none";
            document.getElementById("error").innerHTML=data.error.message;
            return;
        }

        document.getElementById("error").innerHTML="";

        document.getElementById("weather").style.display="block";

        document.getElementById("location").innerHTML=
        data.location.name+", "+data.location.region;

        document.getElementById("country").innerHTML=
        data.location.country;

        document.getElementById("temp").innerHTML=
        data.current.temp_c;

        document.getElementById("condition").innerHTML=
        data.current.condition.text;

        document.getElementById("humidity").innerHTML=
        data.current.humidity;

        document.getElementById("wind").innerHTML=
        data.current.wind_kph;

        document.getElementById("feels").innerHTML=
        data.current.feelslike_c;

        document.getElementById("pressure").innerHTML=
        data.current.pressure_mb;

        document.getElementById("uv").innerHTML=
        data.current.uv;

        document.getElementById("icon").src=
        "https:"+data.current.condition.icon;

    }

    catch(error){
        document.getElementById("error").innerHTML="Something went wrong!";
    }

}

document.getElementById("city").addEventListener("keypress",function(e){
    if(e.key==="Enter"){
        getWeather();
    }
});

</script>

</body>
</html>