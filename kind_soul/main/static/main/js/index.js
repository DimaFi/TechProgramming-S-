document.addEventListener('DOMContentLoaded', () => {
    const carousel = document.querySelector('.carousel');
    const images = document.querySelectorAll('.carousel-image');
    let visibleImages = getVisibleImages(); // Количество видимых изображений зависит от разрешения
    let currentIndex = visibleImages;

    function getVisibleImages() {
        return window.innerWidth < 768 ? 1 : 3; // 1 изображение на маленьких экранах, 3 на больших
    }

    function updateImageDimensions() {
        visibleImages = getVisibleImages(); // Обновляем количество видимых изображений
        const imageWidth = carousel.clientWidth / visibleImages; // Ширина одного изображения
        images.forEach(image => {
            image.style.width = `${imageWidth}px`;
        });
    }

    // Клонируем изображения для бесконечной прокрутки
    const prependImages = Array.from(images).slice(-visibleImages).map(img => img.cloneNode(true));
    const appendImages = Array.from(images).slice(0, visibleImages).map(img => img.cloneNode(true));

    prependImages.forEach(img => carousel.prepend(img));
    appendImages.forEach(img => carousel.append(img));

    function updateCarousel() {
        carousel.style.transition = 'transform 0.5s ease-in-out';
        carousel.style.transform = `translateX(-${currentIndex * (carousel.clientWidth / visibleImages)}px)`;
    }

    function showNextImage() {
        currentIndex++;
        updateCarousel();

        setTimeout(() => {
            if (currentIndex >= images.length + visibleImages) {
                currentIndex = visibleImages;
                carousel.style.transition = 'none';
                carousel.style.transform = `translateX(-${currentIndex * (carousel.clientWidth / visibleImages)}px)`;
            }
        }, 500);
    }

    // Интервал автоматической прокрутки
    setInterval(showNextImage, 3000);

    // Обновляем размеры при изменении размера окна
    window.addEventListener('resize', () => {
        updateImageDimensions();
        updateCarousel();
    });

    // Инициализация
    updateImageDimensions();
});

document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.getElementById('menu-toggle');
    const menu = document.getElementById('menu');
  
    menuToggle.addEventListener('click', () => {
      menu.classList.toggle('active');
    });
  });
  