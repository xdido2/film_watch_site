let headerBurger     = document.getElementById("header__burger");
let mainMenu         = document.getElementById("main__menu");
let isParentBtn      = document.getElementById("is__parent");
let mainDropDownMenu = document.querySelector('.main__dropdown');

headerBurger.onclick = function() {
    headerBurger.classList.toggle("active");
    mainMenu.classList.toggle('active');
}

isParentBtn.addEventListener('click', () => {
    isParentBtn.classList.toggle('active');
    mainDropDownMenu.classList.toggle('active');
});