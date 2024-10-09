<!-- ImageTextBlock.svelte -->
<script>
    export let imageUrl; // URL изображения
    export let text; // Текст для блока
  </script>
  
  <style>
    .image-text-block {
      display: flex;
      align-items: center; /* Выравнивание по вертикали */
      margin: 10px 0;
    }
  
    .image-text-block img {
      width: 50px; /* Ширина изображения */
      height: auto; /* Авто-высота для поддержания пропорций */
      margin-right: 10px; /* Отступ справа от изображения */
    }
  
    .image-text-block p {
      margin: 0; /* Убираем отступы у параграфа */
    }
  </style>
  
  <div class="image-text-block">
    <img src={imageUrl} alt={text} />
    <p>{text}</p>
  </div>
  