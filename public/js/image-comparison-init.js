// Wires up every .js-comparison-container on the page as an ImageComparison
// slider. Each container holds two img.comparison-image; their alt text is the label.
document.addEventListener('DOMContentLoaded', function () {
  var containers = document.querySelectorAll('.js-comparison-container');
  for (var i = 0; i < containers.length; i++) {
    var container = containers[i];
    var images = container.querySelectorAll('.comparison-image');
    new ImageComparison({
      container: container,
      startPosition: container.getAttribute('data-start-position'),
      data: [
        { image: images[0], label: images[0].alt },
        { image: images[1], label: images[1].alt }
      ]
    });
  }
});
