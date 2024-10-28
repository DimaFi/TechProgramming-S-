<script>
    import { fade } from 'svelte/transition';

    // Галерея изображений
    let images = [
        'img_back_1.png', 'img_back_2.png', 'img_back_3.png', 'img_back_4.png', 
        'img_front_1.png', 'img_front_2.png', 'img_front_3.png', 'img_front_1.png'
    ];

    // Функция для перемешивания массива
    function shuffleArray(array) {
        return array.sort(() => Math.random() - 0.5);
    }

    // Перемешанный массив изображений
    let randomizedImages = shuffleArray(images);
</script>

<style>
    .buttons {
        display: flex;
        gap: 20px;
        justify-content: center;
    }

    .button {
        padding: 10px 20px;
        background-color: #00796b;
        color: #fff;
        text-decoration: none;
        border-radius: 5px;
        font-size: 1em;
        transition: background-color 0.3s ease;
    }

    .button:hover {
        background-color: #004d40;
    }

    .gallery {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -1;
    }

    .gallery img {
        position: absolute;
        width: 150px;
        height: auto;
        border-radius: 10px;
        transition: transform 0.3s ease, opacity 0.3s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        opacity: 0;
    }

    .left {
        left: 0;
        animation: slide-left 10s infinite;
    }

    .right {
        right: 0;
        animation: slide-right 10s infinite;
    }

    @keyframes slide-left {
        0% {
            transform: translateX(-150%);
            opacity: 0;
        }
        10% {
            opacity: 1;
        }
        90% {
            opacity: 1;
        }
        100% {
            transform: translateX(0);
            opacity: 0;
        }
    }

    @keyframes slide-right {
        0% {
            transform: translateX(150%);
            opacity: 0;
        }
        10% {
            opacity: 1;
        }
        90% {
            opacity: 1;
        }
        100% {
            transform: translateX(0);
            opacity: 0;
        }
    }
</style>

<div class="container">
    <h1 in:fade={{ duration: 1000 }}>Спасаем сердца, дарим тепло</h1>
    <p in:fade={{ duration: 1500 }}>
        Мы верим, что каждая жизнь ценна и достойна любви. Наш фонд помогает брошенным и нуждающимся животным найти новый дом, вернуть веру в людей и подарить надежду на счастливую жизнь.
    </p>
    <div class="buttons">
        <a href="/more" class="button" in:fade={{ duration: 1000 }}>Подробнее</a>
        <a href="/donate" class="button" in:fade={{ duration: 1000 }}>Пожертвовать</a>
    </div>
</div>

<div class="gallery">
    {#each randomizedImages as image, i}
        <img src={image} alt="Наш любимец" class={i % 2 === 0 ? 'left' : 'right'} />
    {/each}
</div>

<div class="container_text">
    <!-- Нижняя часть страницы: Как помочь -->
    <div class="help-section">
        <h2>Как помочь?</h2>
        <p>Возьмите друга домой. Откройте своё сердце и примите в свою жизнь преданную душу. Мы уверены, что вместе вы создадите историю любви.</p>
        <p>Станьте временным куратором. Если вы пока не можете взять животное навсегда, но готовы предоставить временное жильё, это тоже огромная помощь.</p>
        <p>Поддержите нас. Ваше пожертвование поможет нам обеспечить медицинскую помощь, питание и уход для тех, кто в этом остро нуждается.</p>
        <p>Расскажите о нас. Делая репосты и рассказывая о нашей деятельности, вы даёте шанс каждому подопечному найти дом.</p>
    </div>
</div>
