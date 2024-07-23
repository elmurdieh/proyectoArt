document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM completamente cargado y parseado');

    // Código para manejar la activación de botones Sí/No en preguntas
    const preguntas = document.querySelectorAll('.pregunta-row');
    console.log('Preguntas encontradas:', preguntas);

    preguntas.forEach(pregunta => {
        pregunta.addEventListener('click', event => {
            console.log('Botón clicado:', event.target);

            if (event.target.classList.contains('btn-outline-success') || event.target.classList.contains('btn-outline-danger')) {
                // Obtén todos los botones en esta fila
                const botones = pregunta.querySelectorAll('.btn');
                console.log('Botones en la fila:', botones);
                
                // Elimina la clase 'active' de todos los botones en esta fila
                botones.forEach(boton => boton.classList.remove('active'));
                
                // Añade la clase 'active' al botón clicado
                event.target.classList.add('active');
            }
        });
    });

    // Código para manejar la visibilidad de botones adicionales en tablas
    const tables = document.querySelectorAll('.table');
    
    tables.forEach(table => {
        const buttons = table.querySelectorAll('.btn-group button');
    
        buttons.forEach(button => {
            button.addEventListener('click', (event) => {
                // Obtén el contenedor de los botones
                const btnGroup = event.target.closest('.btn-group');
                
                // Obtén todos los botones en el grupo
                const btns = btnGroup.querySelectorAll('button');
                
                // Elimina la clase 'active' de todos los botones en el grupo
                btns.forEach(btn => btn.classList.remove('active'));
                
                // Añade la clase 'active' al botón clicado
                event.target.classList.add('active');
            });
        });
    });
});

function limpiarFormulario() {
    // Restablecer todos los campos del formulario
    document.querySelectorAll('input[type="text"], input[type="number"], textarea').forEach(input => input.value = '');
    // Eliminar la clase 'active' de todos los botones
    document.querySelectorAll('.btn-group .btn').forEach(btn => btn.classList.remove('active'));
}
