var mymap;
var marker;
var latitud;
var longitud;
const postUpdatePosition =  async(latitud, longitud) => {
  const csrfToken = window.myAppConfig.csrfToken;
  const response = await fetch('/dashboard/updateposition', {
    method: 'POST',
    body: JSON.stringify({'Latidud': latitud, 'Longitud': longitud}),
    headers:{
      'Content-Type': 'aplication/json',
      'X-Requested-With': 'XMLHttpRequest',
      'X-CSRFToken': csrfToken 
    }
  })
};
const initializeMap = (latitud, longitud, tagmarker) => {
  //let latitud = parseFloat("{{latitud}}");
  //let longitud = parseFloat("{{longitud}}");
  if (mymap !== undefined) {
    mymap.remove();
  }
  mymap = L.map("mapid").setView([latitud, longitud], 14);
  const path = window.location.pathname;
  console.log("file js", path);
  // Añadir la capa de mapa base de OpenStreetMap
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution:
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(mymap);

  // Añadir marcador
  let markerdescription = tagmarker;
  marker = L.marker([latitud, longitud])
    .addTo(mymap)
    .bindPopup(
      `${markerdescription ? markerdescription : "¡Usted se encuentra aqui!."}`
    )
    .openPopup();
};
//initializeMap(latitud, longitud);

/*const updateMarker = (lat, longi, tagmarker) => {
  console.log("entro a marker add :", lat, longi);
  if (marker) {
    marker.setLatLng([lat, longi]);
    mymap.setView([lat, longi], 15);
    marker.setPopupContent(tagmarker);
  } else {
    initializeMap(lat, longi, tagmarker);
  }
};*/

/* obtener localizacion del nvegador */
const getLocation = () => {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition, showError, {
            enableHighAccuracy: true,
            timeout: 5000,
            maximumAge: 0
        });
  }
};
const showPosition = (position) => {
  latitud = position.coords.latitude;
  longitud = position.coords.longitude;
  postUpdatePosition(latitud, longitud);
  initializeMap(latitud, longitud);
  console.log("Latitud local: ", latitud, " Longitud local: ", longitud);
};
const showError = (error) => {
  switch (error.code) {
    case error.PERMISSION_DENIED:
      console.error("El usuario ha denegado la solicitud de geolocalización.");
      break;
    case error.POSITION_UNAVAILABLE:
      console.error("La información de la ubicación no está disponible.");
      break;
    case error.TIMEOUT:
      console.error("La solicitud de geolocalización ha caducado.");
      break;
    case error.UNKNOWN_ERROR:
      console.error("Ha ocurrido un error desconocido.");
      break;
  }
};

  getLocation();
//initializeMap(latitud, longitud);

const updateMarker = (lat, longi, tagmarker) => {
  console.log("entro a marker add :", lat, longi);
  if (marker) {
    marker.setLatLng([lat, longi]);
    mymap.setView([lat, longi], 15);
    marker.setPopupContent(tagmarker);
  } else {
    initializeMap(lat, longi, tagmarker);
  }
};

