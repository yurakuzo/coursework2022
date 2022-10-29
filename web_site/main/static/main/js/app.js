const header = document.querySelector('#header');

document.addEventListener('scroll', () => {
    var scroll_position = window.scrollY;

    if(scroll_position >= 1){
        header.style.backgroundColor = "#0c0c0dcc";
    }
    else{
        header.style.backgroundColor = "transparent";
    }
});