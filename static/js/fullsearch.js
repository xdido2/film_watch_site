// Открыть и закрыт окно поиска
let getFullWindowSearch = document.getElementById('header__mobile-search');
let fullSearchWindow    = document.getElementById("full__search");
let btnCloseWindow      = document.getElementById('search__window-close');
let body                = document.querySelector('body');

getFullWindowSearch.addEventListener('click', function() {
    fullSearchWindow.classList.add('open');
    body.classList.add('lock');
});

btnCloseWindow.onclick = function() {
    fullSearchWindow.classList.remove('open');
    body.classList.remove('lock');
}
// Конец

// Работа поиска
window.onload = function() {
    const search   = document.getElementById("full-search__input");
    const products = document.querySelectorAll('.search__products div');
    const clearBtn = document.querySelector('.btn-clear');
    
    search.addEventListener('input', () => {
        let searchValue = search.value.toLowerCase();

        products.forEach(elem => elem.classList.remove('hide'));

        if(searchValue.length) {
            products.forEach((elem) => {
                const productLowerText = elem.innerText.toLowerCase();

                if(productLowerText.search(searchValue) == -1) {
                    elem.classList.add('hide');
                }
            });
        } 
    });

    clearBtn.addEventListener('click', () => {
        search.value =  '';
        products.forEach(elem => elem.classList.remove('hide'));
    })
}