<script>
    import { fade, fly } from 'svelte/transition';
    import NewsFeed from '../routes/NewsFeed.svelte';
    import FlipImage from './FlipImage.svelte';


    // import './src/styles/global.css';
    // import './src/styles/header.css';
    // import './src/styles/chat.css';
    // import './src/styles/container.css';

    // Пример новостей
    let newsItems = [
        {
            title: "Потерянная кошка",
            date: "2024-10-07",
            content: "На улице нашли Дашу"
        },
    ];

    // Данные для блоков изображений и текста
    let blocks = [
        {
            imageUrl: 'heart_1.jpg',
            text: 'Возьмите друга домой. Откройте своё сердце и примите в свою жизнь преданную душу. Мы уверены, что вместе вы создадите историю любви.'
        },
        {
            imageUrl: 'heart_1.jpg',
            text: '2'
        },
        {
            imageUrl: 'heart_1.jpg',
            text: '3'
        }
    ];
</script>

<style>
    .gallery {
        display: flex;
        gap: 40px; /* Расстояние между картинками */
        justify-content: center;
        flex-wrap: wrap;
        margin-bottom: 30px;
    }

    /* .container {
        padding: 20px;
        max-width: 800px;
        margin: 0 auto;
        text-align: center;
    } */

    .content {
        margin-bottom: 50px;
    }

    .button {
        display: inline-block;
        padding: 10px 20px;
        background-color: #00796b;
        color: #fff;
        text-decoration: none;
        border-radius: 5px;
        font-size: 1.1em;
        transition: background-color 0.3s ease;
    }

    .button:hover {
        background-color: #004d40;
    }

    img {
        margin: 20px 0;
    }
</style>

<!-- Верхняя часть страницы -->
<div class="container">
    <div class="content">
        <h1 in:fly={{ x: 200, duration: 1000 }}>Спасаем сердца, дарим тепло</h1>
        <p in:fade={{ duration: 1500 }}>
            Каждый день мы стремимся спасти как можно больше жизней. Наша миссия — дать шанс на новую жизнь бездомным и нуждающимся животным. Вместе мы можем сделать этот мир лучше, помогая тем, кто оказался в беде.
        </p>
        <img src="paw_1.png" alt="Наши любимцы" style="width: 5%; height: auto;" in:fly={{ y: -100, duration: 1200 }} />
        <a href="/donate" class="button" in:fly={{ x: 200, duration: 1000 }}>Поддержать приют</a>
    </div>
</div>

<!-- Галерея изображений -->
<div class="gallery">
    <FlipImage frontImage="img_front_1.png" backImage="img_back_1.png" />
    <FlipImage frontImage="img_front_2.png" backImage="img_back_2.png" />
    <FlipImage frontImage="img_front_3.png" backImage="img_back_3.png" />
</div>

<!-- Нижняя часть страницы -->
<div class="container">
    <div class="content">
        <h1 in:fly={{ x: 200, duration: 1000 }}>Как помочь?</h1>
        <img src="heart_1.png" alt="Как помочь?" style="width: 5%; height: auto;" in:fly={{ y: -100, duration: 1200 }} />
        <p in:fade={{ duration: 1500 }}>
            Есть много способов помочь нашему приюту. Вы можете взять животное домой, стать волонтёром или сделать пожертвование. Каждый ваш вклад помогает нам заботиться о тех, кто этого действительно заслуживает.
        </p>
        <img src="paw_1.png" alt="Как помочь?" style="width: 5%; height: auto;" in:fly={{ y: -100, duration: 1200 }} />
        <a href="/donate" class="button" in:fly={{ x: 200, duration: 1000 }}>Поддержать приют</a>
    </div>
</div>

<!-- Лента новостей -->
<div class="container">
    <NewsFeed {newsItems} />
</div>
