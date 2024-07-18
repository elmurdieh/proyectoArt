function saludo(){
    alert("HOLA MUNDO")
}
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