document.getElementById('submitnewcar').addEventListener('click', async () => {
            const form = document.getElementById('miFormulario');
            const formData = new FormData(form);

            try {
	      const response = await fetch('/dashboard/loadnewcar', {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                    }
                });

                if (!response.ok) {
                    throw new Error('Error en la solicitud: ' + response.statusText);
                }

	      const data = await response.json();
	      console.log(data)

	      //const resultDiv = document.getElementById('result');
                if (data.error) {
		  //resultDiv.textContent = 'Error: ' + data.error;
		  let textContent = 'Error: ' + data.error;
		  console.log(textContent);
		  alert("Todos los campos son obligatorios!")
                } else {
		  //resultDiv.textContent = `Campo 1: ${data.campo1}, Campo 2: ${data.campo2}, Selección: ${data.seleccion}`;
		  let textContent = `Campo 1: ${data.campo1}, Campo 2: ${data.campo2}, Selección: ${data.seleccion}`;
		  console.log(textContent);
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Error al enviar el formulario');
            }
});

