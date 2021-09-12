
window.onload = function(){
    var element = document.getElementsByTagName('span')[0], i = 0;
    (function(){
        element.style.left = (++i<200) ? i+'px' : i = 0;
        setTimeout(arguments.callee, 10);
    })();
};
