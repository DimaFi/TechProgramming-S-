<script>
import { fade, fly } from 'svelte/transition';
import NewsFeed from '../routes/NewsFeed.svelte';
import FlipImage from './FlipImage.svelte';

// import './src/styles/global.css';
// import './src/styles/header.css';
// import './src/styles/chat.css';
// import './src/styles/container.css';


</script>

<style>

</style>

<!-- Верхняя часть страницы -->
<div class="container">
    <div class="content">
        <h1 in:fly={{ x: 200, duration: 1000 }}>Контакты</h1>
        <p in:fade={{ duration: 1500 }}>
            Вы можете связаться с нами по телефону: ДАШИ или по email: СЛАВЫ
        </p>
        <img src="paw_1.png" alt="Наши любимцы" style="width: 5%; height: auto;" in:fly={{ y: -100, duration: 1200 }} />
    </div>
</div>