//onload = function(){alert('Olá, seja bem vindo'); }

let slid = document.querySelector('.slider');
//let propriedadeAreaSlidersx = slidersArea.getBoundingClientRect();
//let propriedadeXW = propriedadeAreaSlidersx.width
let propriedadeX = slid.getBoundingClientRect();
let larguraSlid = propriedadeX.width


let totalSlides = document.querySelectorAll('.slider').length;
let currentSlide = 0;

const target = document.querySelectorAll('[data-animate]');
const animationClass = 'show'

function mostrar(){
    //console.log('estou funcionando')
    //console.log(windowTop)
    const windowTop = window.pageYOffset;
    target.forEach(function(element){
        if((windowTop) == 700){
            element.classList.add("show")
        }
    })
}

window.addEventListener('scroll', function(){
    mostrar();
});

function goNext(){
    currentSlide++;
    if (currentSlide > (totalSlides - 1)){
        currentSlide = 0;
    }
    updateMargin();

}

function goBack(){
    currentSlide--;
    if(currentSlide < 0) {
        currentSlide = totalSlides - 1;
    }
    updateMargin();
}

function updateMargin(){
    let newMargin = (currentSlide * larguraSlid);
    document.querySelector('.slider').style.marginLeft = `-${newMargin}px`
}



