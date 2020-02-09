const COORDS = 'coords';

function handleGeoSuceces(position){
    console.log(position);
}

function handleGeoError(){
    console.log("Cant access geo location");
}

function askForCoords(){
    navigator.geolocation.getCurrentPosition(handleGeoSuceces, handleGeoError)
}

function loadCoords(){
    const loadedCoords = localStorage.getItem(COORDS);
    if(loadedCoords === null){
        askForCoords;
    } else{
        // getWeather
    }
}

function init(){
    loadCoords();
}

init();