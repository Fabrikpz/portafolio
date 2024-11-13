// Obtener el botón de menú, el sidebar y el botón de cierre
const menuBtn = document.querySelector('.menu-btn');
const sidebar = document.querySelector('.sidebar');
const closeBtn = document.querySelector('.close-btn');

// Función para abrir el sidebar
menuBtn.addEventListener('click', () => {
    sidebar.classList.add('open');
    menuBtn.style.display = 'none';  // Ocultar el botón de menú al abrir el sidebar
});

// Función para cerrar el sidebar
closeBtn.addEventListener('click', () => {
    sidebar.classList.remove('open');
    menuBtn.style.display = 'block';  // Mostrar el botón de menú al cerrar el sidebar
});
