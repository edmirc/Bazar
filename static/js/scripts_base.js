function menuShow() {
    const divMobile = document.querySelector('.div-mobile');
    const searchMobile = document.querySelector('.mobile-search');
    const icon = document.querySelector('.icon');
    const iconSearch = document.querySelector('.icon-search');

    // Fecha a barra de busca se estiver aberta
    if (searchMobile.classList.contains('open')) {
        searchMobile.classList.remove('open');
        if (iconSearch.src.includes('fechar.svg')) {
            iconSearch.src = '../static/imag/search.svg';
        }
    }

    // Alterna o menu
    if (divMobile.classList.contains('open')) {
        divMobile.classList.remove('open');
        if (icon.src.includes('icon_close.svg')) {
            icon.src = '../static/imag/menu.svg';
        }
    } else {
        divMobile.classList.add('open');
        if (icon.src.includes('menu.svg')) {
            icon.src = '../static/imag/icon_close.svg';
        }
    }
}

function showSearch() {
    const divSearch = document.querySelector('.mobile-search');
    const divMobile = document.querySelector('.div-mobile');
    const icon = document.querySelector('.icon');
    const iconSearch = document.querySelector('.icon-search');

    // Fecha o menu se estiver aberto
    if (divMobile.classList.contains('open')) {
        divMobile.classList.remove('open');
        if (icon.src.includes('icon_close.svg')) {
            icon.src = '../static/imag/menu.svg';
        }
    }

    // Alterna a barra de busca
    if (divSearch.classList.contains('open')) {
        divSearch.classList.remove('open');
        if (iconSearch.src.includes('icon_close.svg')) {
            iconSearch.src = '../static/imag/search.svg';
        }
    } else {
        divSearch.classList.add('open');
        if (iconSearch.src.includes('search.svg')) {
            iconSearch.src = '../static/imag/icon_close.svg';
        }
    }
}




/*
function menuShow(){
    let divMobile = document.querySelector('.div-mobile');
    let searchmobile = document.querySelector('.mobile-search');
    if (searchmobile.classList.contains('open')){
        searchmobile.classList.remove('open')
        document.querySelector('.icon-search').src = '../static/imag/search.svg'
    }
    if (divMobile.classList.contains('open')){
        divMobile.classList.remove('open');
        document.querySelector('.icon').src = '../static/imag/menu.svg'
    }else{
        divMobile.classList.add('open');
        document.querySelector('.icon').src = '../static/imag/icon_close.svg'
    }
}

function showSearch(){
    let divSearch = document.querySelector('.mobile-search');
    let divMobile = document.querySelector('.div-mobile');
    if (divMobile.classList.contains('open')){
        divMobile.classList.remove('open')
        document.querySelector('.icon').src = '../static/imag/menu.svg'
    }
    if (divSearch.classList.contains('open')){
        divSearch.classList.remove('open');
        document.querySelector('.icon-search').src = '../static/imag/search.svg'
    }else{
        divSearch.classList.add('open');
        document.querySelector('.icon').src = '../static/imag/icon_close.svg'
    }
}*/