document.addEventListener("DOMContentLoaded", function () {
  //let latitud = parseFloat("{{latitud}}");
  //let longitud = parseFloat("{{longitud}}");
  var mymap = L.map("mapid").setView([latitud, longitud], 15);
  const path = window.location.pathname;
  console.log('file js', path);
  // Añadir la capa de mapa base de OpenStreetMap
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution:
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(mymap);

  // Añadir marcador
  L.marker([latitud, longitud])
    .addTo(mymap)
    .bindPopup("¡Hola! Este es el obelisco.")
    .openPopup();
});
