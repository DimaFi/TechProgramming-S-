<script>
    import { fade, fly } from 'svelte/transition';
    import './styles/global.css';

    // Images for the gallery
    let images = [
        'img_back_1.png', 'img_back_2.png', 'img_back_3.png', 'img_back_4.png',
        'img_front_1.png', 'img_front_2.png', 'img_front_3.png'
    ];
</script>

<style>
    /* Общие стили */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        font-family: Arial, sans-serif;
        background-color: #e8f4f8;
        color: #333;
    }

    /* Основной контейнер */
    .main-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 50px 20px;
        max-width: 1200px;
        margin: 0 auto;
    }

    /* Текстовый блок */
    .container {
        max-width: 600px;
        text-align: center;
        margin-bottom: 40px;
    }

    /* .container h1 {
        font-size: 2.5rem;
        margin-bottom: 20px;
    }

    .container p {
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 20px;
    } */

    .hero-buttons {
        display: flex;
        gap: 10px;
        justify-content: center;
        margin-bottom: 40px;
    }

    .details-btn, .donate-btn {
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 20px;
        cursor: pointer;
    }

    .details-btn {
        background-color: #5ec1e6;
        color: #fff;
    }

    .donate-btn {
        background-color: #00b5ad;
        color: #fff;
    }

    /* Галерея в стиле мозаики */
    .gallery {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        grid-auto-rows: 150px;
        gap: 10px;
        width: 100%;
        max-width: 1000px;
    }

    /* Асимметричная структура изображений */
    .gallery img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 10px;
        transition: transform 0.3s ease;
    }

    /* Настраиваем размеры изображений в сетке */
    .gallery img:nth-child(1) {
        grid-column: span 2;
        grid-row: span 2;
    }

    .gallery img:nth-child(3) {
        grid-column: span 2;
        grid-row: span 1;
    }

    .gallery img:nth-child(5) {
        grid-column: span 1;
        grid-row: span 2;
    }

    .gallery img:nth-child(7) {
        grid-column: span 2;
        grid-row: span 1;
    }

    .gallery img:hover {
        transform: scale(1.05);
    }

    /* Секция "Как помочь" */
    .how-to-help {
        padding: 40px 20px;
        text-align: center;
        max-width: 800px;
        margin: 50px auto 0;
    }

    .how-to-help h2 {
        font-size: 2rem;
        margin-bottom: 20px;
    }

    .how-to-help ul {
        list-style: none;
    }

    .how-to-help li {
        font-size: 1.1rem;
        margin-bottom: 15px;
        color: #555;
    }
</style>

<div class="main-content">
    <!-- Блок с текстом и кнопками -->
    <div class="container">
        <h1 in:fade={{ duration: 1000 }}>Спасаем сердца, дарим тепло</h1>
        <p in:fade={{ duration: 1500 }}>
            Мы верим, что каждая жизнь цена и достойна любви. Наш фонд помогает брошенным и нуждающимся животным найти новый дом, вернуть веру в людей и подарить надежду на счастливую жизнь...
        </p>
        <div class="hero-buttons">
            <button class="details-btn" in:fly={{ y: 20, duration: 800 }}>Подробнее</button>
            <button class="donate-btn" in:fly={{ y: 20, duration: 800, delay: 200 }}>Пожертвовать</button>
        </div>
    </div>

    <!-- Блок с галереей -->
    <div class="gallery">
        {#each images as image, i}
            <img src={image} alt="Изображение животного" in:fly={{ y: 30, duration: 800, delay: i * 150 }} />
        {/each}
    </div>
</div>

<div class="how-to-help">
    <h2 in:fade={{ duration: 1000 }}>Как помочь?</h2>
    <ul>
        <li in:fade={{ duration: 1000, delay: 200 }}>🤍 Возьмите друга домой...</li>
        <li in:fade={{ duration: 1000, delay: 400 }}>🤍 Станьте временным куратором...</li>
        <li in:fade={{ duration: 1000, delay: 600 }}>🤍 Поддержите нас...</li>
        <li in:fade={{ duration: 1000, delay: 800 }}>🤍 Расскажите о нас...</li>
    </ul>
</div>
