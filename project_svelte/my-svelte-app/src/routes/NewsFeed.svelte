<script>
	export let newsItems = []; // Получение новостей через пропсы
</script>

<style>

.news-feed {
    background-color: #f9f9f9; /* Фон для ленты новостей */
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    margin-top: 20px;
}

.news-item {
    border: 1px solid #e0e0e0;
    border-radius: 5px;
    padding: 15px;
    margin-bottom: 15px;
    background-color: white;
}

.news-title {
    font-size: 20px;
    color: #00796b;
    margin-bottom: 10px;
}

.news-date {
    color: #777;
    font-size: 14px;
    margin-bottom: 10px;
}
</style>

<div class="news-feed">
<h2>Лента новостей</h2>
{#if newsItems.length > 0}
    {#each newsItems as item}
        <div class="news-item">
            <h3 class="news-title">{item.title}</h3>
            <p class="news-date">{item.date}</p>
            <p>{item.content}</p>
        </div>
    {/each}
{:else}
    <p>Нет новостей для отображения.</p>
{/if}
</div>