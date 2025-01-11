document.addEventListener("DOMContentLoaded", function() {
    const videoItems = document.querySelectorAll('.video-item');
    const videoFrame = document.querySelector('.videos_frame');

    // Функция для проверки, виден ли элемент
    function isElementInViewport(el) {
        const rect = el.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }

    // Функция для добавления класса 'visible' к элементам
    function showVideos() {
        videoItems.forEach((item, index) => {
            if (isElementInViewport(videoFrame)) {
                setTimeout(() => {
                    item.classList.add('visible');
                }, index * 100); // Задержка для каждого элемента
            }
        });
    }

    // Запускаем анимацию при прокрутке
    window.addEventListener('scroll', showVideos);
});