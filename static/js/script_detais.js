// filepath: /product-display/product-display/js/script.js
document.addEventListener('DOMContentLoaded', function() {
    const mainImage = document.getElementById('main-image');
    const thumbnails = document.querySelectorAll('.thumbnail');

    thumbnails.forEach(thumbnail => {
        thumbnail.addEventListener('click', function() {
            mainImage.src = this.src;
            mainImage.classList.add('enlarged');
        });
    });

    mainImage.addEventListener('click', function() {
        if (this.classList.contains('enlarged')) {
            this.classList.remove('enlarged');
        } else {
            this.classList.add('enlarged');
        }
    });
});