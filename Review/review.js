// Make API call the listed site and return the current weather conditions for Cocoa Beach, FL
// https://weatherstack.com

    const apicall = async() => {
    fetch('http://api.weatherstack.com/current?access_key=c4088c285aac67a81e0e96caa950ce09&query=Cocoa Beach')
    .then((response) => response.json())
    .then((data)=>{
        console.log(data)
        weatherInfo = {
            temperature: data.current.temperature,
            windspeed: data.current.wind_speed,
            description: data.current.weather_descriptions
        }
    })
console.log(weatherInfo)    
}

apicall()