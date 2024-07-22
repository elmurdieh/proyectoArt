

function openModal() {
    document.getElementById("myModal").style.display = "block";
}

// Función para cerrar el modal
function closeModal(event) {
    var modal = document.getElementById("myModal");
    if (event.target == modal || event.target.className == "close") {
        modal.style.display = "none";
    }
}
document.addEventListener('DOMContentLoaded', () => {
    const loadWorkers = async () => {
      const response = await fetch('/get_workers');
      if (!response.ok) {
        console.error('Error fetching data:', response.statusText);
        return;
      }
      const trabajadores = await response.json();
      const tbody = document.getElementById('workerTableBody');
      tbody.innerHTML = '';
      trabajadores.forEach(trabajador => {
        const row = `
          <tr>
            <td class="p-2 border-b">${trabajador.Nombre}</td>
            <td class="p-2 border-b">${trabajador.Rut}</td>
            <td class="p-2 border-b">
              <button onclick="guardarUsuarios('${trabajador.Rut}')" class="bg-green-500 text-white py-1 px-2 rounded hover:bg-green-600">
                Asignar
              </button>
            </td>
          </tr>
        `;
        tbody.innerHTML += row;
      });
    };
    loadWorkers();
  });
var trabajadores = []
function guardarUsuarios(valor){
    trabajadores.push(valor)
}
function verTrabajadores(){
    alert(trabajadores)
}
async function enviarTrabajadores() {
    const response = await fetch('/guardar_trabajadores', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ trabajadores })
    });

    if (response.ok) {
        alert('Trabajadores enviados exitosamente');
    } else {
        alert('Error al enviar los trabajadores');
    }
}