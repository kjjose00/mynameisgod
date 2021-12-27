const navbar = document.querySelector('.navbar');

const container = document.querySelector('.container');

window.onscroll = function(){
    if(window.pageYOffset > navbar.offsetTop){
        navbar.classList.add('sticky')
    }
    else{
        navbar.classList.remove('sticky');
    }
}