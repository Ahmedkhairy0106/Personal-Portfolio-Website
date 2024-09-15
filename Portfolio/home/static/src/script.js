document.addEventListener('DOMContentLoaded', function() {
    const menuButton = document.getElementById('menu-button');
    const navbar = document.getElementById('navbar-cta');

    menuButton.addEventListener('click', () => {
        navbar.classList.toggle('hidden');
    });
});