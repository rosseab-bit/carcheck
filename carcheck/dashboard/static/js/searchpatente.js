document
  .getElementById("getlocation")
  .addEventListener("click", async (event) => {
    event.preventDefault();
    const form = document.getElementById("formSearchPatente");
    const formData = new FormData(form);
    var patente = formData.get("search-input");
    try {
      const response = await fetch(`/dashboard/searchvehiculo/${patente}`);

      if (!response.ok) {
        throw new Error("Error en la solicitud: " + response.statusText);
      }

      const data = await response.json();
      if (
        data.vehicle.longitud.length === 0 &&
        data.vehicle.latitud.length === 0
      ) {
        alert("No existen coordenadas para esa patente");
      }
      console.log(
        "Estos son los vehiculos: ",
        data.vehicle,
        data.vehicle.longitud.toString().length,
        data.vehicle.latitud.toString().length
      );
      /* actualizo mapa con las coordenadas que se condiguen */
      if (
        data.vehicle.longitud.toString().length > 0 &&
        data.vehicle.latitud.toString().length > 0
      ) {
        console.log("actualizo mapa");
        updateMarker(data.vehicle.latitud, data.vehicle.longitud, data.vehicle.patente);
      }
      /* actualizo mapa con las coordenadas que se condiguen */

      //const resultDiv = document.getElementById('result');
      if (data.error) {
        //resultDiv.textContent = 'Error: ' + data.error;
        let textContent = "Error: " + data.error;
        console.log(textContent);
      } else {
        //resultDiv.textContent = `Campo 1: ${data.campo1}, Campo 2: ${data.campo2}, Selección: ${data.seleccion}`;
      }
    } catch (error) {
      console.error("Error:", error);
      alert("No se encontro resultado para la pantente.");
    }
  });
