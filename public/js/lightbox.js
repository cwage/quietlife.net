document.addEventListener('keydown', function(e) {
    if (e.key === "Escape" || e.key === "Esc") {
        var lightbox = document.querySelector('.lightbox:target');
        if (lightbox) {
            window.history.replaceState(null, document.title, window.location.pathname + window.location.search + '#_');
            lightbox.style.display = 'none';
        }
    }
});
