<script>
  import Home from './routes/Home.svelte';
  import About from './routes/About.svelte';
  import Contacts from './routes/Contacts.svelte';
  import Donate from './routes/Donate.svelte';
  import News from './routes/NewsFeed.svelte';
  import FlipImage from './routes/FlipImage.svelte';

  // Путь сейчас к странице
  let currentRoute = '/';

  // Видимость меню
  let showMenu = false;

  // Текущее значение темы (изначлально light)
  let theme = 'light';

  // Переключение темы
  function toggleTheme() {
    theme = theme === 'light' ? 'dark' : 'light';
    document.body.setAttribute('data-theme', theme); // Установка темы на body
  }

  // переключение страниц
  function navigate(route) {
    currentRoute = route;
    showMenu = false;
  }

  // Видимость чата
  let showChat = false;

  function toggleChat() {
    showChat = !showChat;
  }

  // новости, но тут они не нужны скорее всего
  let newsItems = [
    {
      title: "",
      date: "",
      content: ""
    },
  ];
</script>

<style>
  body {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
    color: #333;
    transition: background-color 0.8s, color 0.8s;
  }

  body[data-theme='light'] {
    background-color: #f0f0f0;
    color: #333333;
  }

  body[data-theme='dark'] {
    background-color: #2b2b2b;
    color: #f0f0f0;
  }

  .app-container {
    display: flex;
    min-height: 100vh;
  }

  .container_text {
  background: linear-gradient(135deg, #e0f7fa, #00796b); /* Градиентный фон */
  padding: 20px;
  border-radius: 15px; /* Закругленные углы */
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15); /* Тень для объема */
  margin-top: 20px;
  animation: fadeIn 0.8s ease-out; /* Плавное появление */
  color: white; /* Белый цвет текста для контраста */
  font-size: 1.1em;
  line-height: 1.5; /* Улучшает читаемость текста */
  max-width: 800px;
  margin: 20px auto; /* Центрирование блока */
}

  /* Текстовые элементы внутри контейнера */
.container_text h1 {
  font-size: 2em;
  margin-bottom: 15px;
  color: #ffffff; /* Белый цвет заголовка */
  text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.4); /* Тень для заголовка */
}

.container_text p {
  margin-bottom: 10px;
  color: #e0f7fa; /* Светлый оттенок для текста */
}

.container_text a {
  color: #ffeb3b; /* Жёлтые ссылки */
  text-decoration: underline;
  transition: color 0.3s ease;
}

.container_text a:hover {
  color: #ffca28; /* Изменение цвета при наведении */
}

.menu {
  position: fixed; /* Закрепляем меню относительно окна браузера */
  top: 90px;
  left: -370px; /* Скрываем меню за пределами экрана */
  width: 200px; /* Фиксированная ширина меню */
  height: 100%; /* Меню занимает всю высоту экрана */
  overflow: hidden;
  background-color: #004d40;
  color: white;
  transition: left 0.3s ease; /* Анимация появления меню */
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.5); /* Добавляем тень */
  z-index: 9; /* Меню находится поверх контента */
}

.menu.open {
  left: 0; /* При открытии меню появляется на экране */
}

  /* .menu.open {
    width: 740px;
  } */

  .menu ul {
    list-style: none;
    padding: 20px;
    margin: 0;
  }

  .menu ul li {
    margin: 20px 0;
  }

  .menu ul li a {
    color: #e0f7fa;
    font-size: 18px;
    text-decoration: none;
    display: block;
    padding: 10px;
    transition: background-color 0.3s;
    border-radius: 4px;
  }

  .menu ul li a:hover {
    background-color: #00796b;
  }

  .content {
    flex-grow: 1;
    padding: 20px;
    transition: margin-left 0.3s ease;
  }


  /* при открытии меню сдвигать content вправо */

  /*
  .content.menu-open {
    margin-left: 250px;
  }
  */ 


  .header {
    background-color: #e0f7fa;
    padding: 10px 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    border-bottom: 2px solid #00796b;
  }

  .logo {
    width: 50px;
    height: auto;
    margin-right: 15px;
  }

  .title {
    font-size: 24px;
    color: #333;
  }

  .theme-toggle {
    position: absolute;
    right: 20px;
    top: 20px;
    background-color: #00796b;
    color: white;
    border: none;
    padding: 10px;
    cursor: pointer;
    border-radius: 4px;
    transition: background-color 0.3s;
  }

  .theme-toggle:hover {
    background-color: #004d40;
  }

  button {
    transition: background-color 0.3s;
    background-color: #f4f4f4;
    border: 1px solid #ccc;
    padding: 10px 15px;
    border-radius: 4px;
    cursor: pointer;
  }

  button:hover {
    background-color: #ddd;
  }

  .menu-button {
    position: absolute;
    top: 30px;
    left: 20px;
    padding: 10px 20px;
    background-color: #00796b;
    color: white;
    font-size: 16px;
    border: none;
    cursor: pointer;
    border-radius: 4px;
    transition: background-color 0.3s;
    z-index: 10;
  }

  .menu-button:hover {
    background-color: #004d40;
  }

  .container {
    padding: 20px;
    flex-grow: 1;
  }

  .chat-button {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #00796b;
    color: white;
    border: none;
    border-radius: 50%;
    width: 60px;
    height: 60px;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;  
    transition: background-color 0.3s;
    z-index: 10;
  }

  .chat-button:hover {
    background-color: #004d40;
  }

  .chat-window {
    position: fixed;
    bottom: 100px;
    right: 20px;
    width: 300px;
    height: 400px;
    background-color: #e0f7fa;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    display: none;
    z-index: 20;
    padding: 20px;
    color: #333;
  }

  .chat-window.open {
    display: block;
  }

  .chat-header {
    font-size: 18px;
    color: #00796b;
    margin-bottom: 10px;
  }

  .chat-options {
    display: flex;
    flex-direction: column;
  }

  .chat-options button {
    background-color: #00796b;
    border: none;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 10px;
    cursor: pointer;
    color: white;
    transition: background-color 0.3s;
  }

  .chat-options button:hover {
    background-color: #004d40;
  }

  @keyframes fadeIn {
    from {
      opacity: 0;
      transform: translateY(10px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

</style>

<div class="header">
  <img class="logo" src="logo_1.png" alt="Logo" />
  <h1 class="title">Преданные Души</h1>
  <button class="theme-toggle" on:click={toggleTheme}>
    {theme === 'light' ? 'Dark Mode' : 'Light Mode'}
  </button>
</div>

<button class="menu-button" on:click={() => (showMenu = !showMenu)}>
  {showMenu ? 'Close' : 'Menu'}
</button>

<div class="app-container">
  <nav class={`menu ${showMenu ? 'open' : ''}`}>
    <ul>
      <li><a href="javascript:void(0);" on:click={() => navigate('/')}>Главная страница</a></li>
      <li><a href="javascript:void(0);" on:click={() => navigate('/about')}>О нас</a></li>
      <li><a href="javascript:void(0);" on:click={() => navigate('/contacts')}>Контакты</a></li>
      <li><a href="javascript:void(0);" on:click={() => navigate('/donate')}>Пожертвования</a></li>
      <li><a href="javascript:void(0);" on:click={() => navigate('/news')}>Новости</a></li>
      <li><a href="javascript:void(0);" on:click={() => navigate('/gallery')}>Фотографии</a></li>
    </ul>
  </nav>

  <div class={`content ${showMenu ? 'menu-open' : ''}`}>
    {#if currentRoute === '/'}
      <Home />
    {:else if currentRoute === '/about'}
      <About />
    {:else if currentRoute === '/contacts'}
      <Contacts />
    {:else if currentRoute === '/donate'}
      <Donate />
    {:else if currentRoute === '/news'}
      <News {newsItems} />
    {:else if currentRoute === '/gallery'}
      <FlipImage />
    {/if}
  </div>
</div>

<!-- <div class="image-button-block">
  <a href="/donate" class="support-button">Support Us</a>
</div> -->

<div class="chat-window {showChat ? 'open' : ''}">
  <div class="chat-header">Мы на связи!</div>
  <div class="chat-options">
    <button on:click={() => alert('Есть вопрос? Напиши нам в чат!')}>Чат</button>
    <button on:click={() => alert('Есть впорос? Напиши нам на почту!')}>Почта</button>
  </div>
</div>

<button class="chat-button" on:click={toggleChat}>Chat</button>
