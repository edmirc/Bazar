document.addEventListener('DOMContentLoaded', function() {
    const mainImage = document.querySelector('.product-gallery-img');
    const thumbnails = document.querySelectorAll('.thumbnails');

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

function menuShow(){
    let divMobile = document.querySelector('.div-mobile');
    if (divMobile.classList.contains('open')){
        divMobile.classList.remove('open');
    }else{
        divMobile.classList.add('open');
        
    }
}

function showSearch(){
    let divSearch = document.querySelector('.mobile-search');
    if (divSearch.classList.contains('open')){
        divSearch.classList.remove('open');
    }else{
        divSearch.classList.add('open');
    }
}