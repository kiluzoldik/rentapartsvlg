document.addEventListener('DOMContentLoaded', function() {
    showErrorPopups();
});

function showErrorPopups() {
    const popups = document.querySelectorAll('.error-popup');
    popups.forEach(popup => {
        popup.classList.add('show');
        
        setTimeout(() => {
            popup.classList.remove('show');
        }, 5000);
    });
}

function closePopup(element) {
    const popup = element.parentElement;
    popup.classList.remove('show');
}