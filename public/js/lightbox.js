document.onkeydown = function(e) {
    e = e || window.event;
    var isEscape = false;
    if ("key" in e) {
        isEscape = (e.key === "Escape" || e.key === "Esc");
    } else {
        isEscape = (e.keyCode === 27);
    }
    if (isEscape) {
        var lightbox = document.querySelector('.lightbox:target');
        if(lightbox) {
           window.location.href = '#_';
        }
    }
};
