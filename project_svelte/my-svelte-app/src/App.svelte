  <script>
    import Home from './routes/Home.svelte';
    import About from './routes/About.svelte';
    import Contacts from './routes/Contacts.svelte';
    import Donate from './routes/Donate.svelte';
    import News from './routes/NewsFeed.svelte';
    import FlipImage from './routes/FlipImage.svelte';


    import './styles/global.css';
    import './styles/header.css';
    import './styles/chat.css';
    import './styles/container.css';

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

  .container_text h1 {
    font-size: 2em;
    margin-bottom: 15px;
    color: #ffffff;
    text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.4);
  }

  .container_text a {
    color: #ffeb3b;
    text-decoration: underline;
    transition: color 0.3s ease;
  }

  .container_text a:hover {
    color: #ffca28;
  }

  .menu {
    position: fixed;
    top: 90px;
    left: -370px;
    width: 200px;
    height: 100%;
    overflow: hidden;
    background-color: #004d40;
    color: white;
    transition: left 0.3s ease;
    box-shadow: 2px 0 5px rgba(0, 0, 0, 0.5);
    z-index: 9;
  }

  .menu.open {
    left: 0;
  }

  .menu ul {
    list-style: none;
    padding: 20px;
    margin: 0;
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

  .header {
    padding: 10px 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
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

  button {
    transition: background-color 0.3s;
    background-color: #f4f4f4;
    border: 1px solid #ccc;
    padding: 10px 15px;
    border-radius: 4px;
    cursor: pointer;
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

  .content {
    padding-top: 150px;
    flex-grow: 1;
    padding: 20px;
  }

/* 
  nav {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 6а 0px;
    background-color: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(10px);
    z-index: 1000;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    padding: 10px 15px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  nav .header {
    display: flex;
    align-items: center;
  }

  nav ul {
    list-style: none;
    display: flex;
    gap: 20px;
    margin: 0;
    padding: 0;
    justify-content: center;
    flex: 1;
  }

  nav a {
    text-decoration: none;
    color: #000;
    font-size: 18px;
    padding: 10px 15px;
    border-radius: 5px;
    transition: background-color 0.3s ease;
  }

  nav a:hover,
  nav a.active {
    background-color: #00bfa6;
    color: #fff;
  } */

  .theme-toggle {
    background-color: #00796b;
    color: white;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
    border-radius: 4px;
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


    <nav>
      <div class="header">
        <img class="logo" src="logo_1.png" alt="Logo" />
        <h1 class="title">Преданные Души</h1>
      </div>


      <ul>
        <li><a href="javascript:void(0);" on:click={() => navigate('/')} class={currentRoute === '/' ? 'active' : ''}>Главная</a></li>
        <li><a href="javascript:void(0);" on:click={() => navigate('/gallery')} class={currentRoute === '/gallery' ? 'active' : ''}>Наши животные</a></li>
        <li><a href="javascript:void(0);" on:click={() => navigate('/contacts')} class={currentRoute === '/contacts' ? 'active' : ''}>Контакты</a></li>
        <li><a href="javascript:void(0);" on:click={() => navigate('/news')} class={currentRoute === '/news' ? 'active' : ''}>Новости</a></li>
      </ul>


      <div class="theme-toggle-container">
        <button class="theme-toggle" on:click={toggleTheme}>
          {theme === 'light' ? 'Тёмная' : 'Светлая  '}
        </button>
      </div> 
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

    
  <div class="chat-window {showChat ? 'open' : ''}">
    <div class="chat-header">Мы на связи!</div>
    <div class="chat-options">
      <button on:click={() => alert('Есть вопрос? Напиши нам в чат!')}>Чат</button>
      <button on:click={() => alert('Есть впорос? Напиши нам на почту!')}>Почта</button>
    </div>
  </div>

  <button class="chat-button" on:click={toggleChat}>Chat</button>
