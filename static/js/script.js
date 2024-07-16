document.addEventListener('DOMContentLoaded', function() {
    const toggleDescription = document.querySelector('.toggle-description');
    const description = document.getElementById('apartment-description');

    toggleDescription.addEventListener('click', function() {
        if (description.style.display === 'none') {
            description.style.display = 'block';
        } else {
            description.style.display = 'none';
        }
    });
});
