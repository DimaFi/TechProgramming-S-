<script>
    export let frontImage;
    export let backImage;
  </script>
  
  <style>
    .flip-container {
      perspective: 1000px; /* перспективу для 3D-эффекта */

      /* размер контейнера */
      width: 300px;
      height: 300px;
    }
  
    .flipper {
      position: relative;
      width: 100%;
      height: 100%;
      transition: transform 0.6s;
      transform-style: preserve-3d;
    }
  
    .flip-container:hover .flipper {
      transform: rotateY(180deg); /* Переворот на 180 */
    }
  
    .front, .back {
      position: absolute;
      width: 100%;
      height: 100%;
      backface-visibility: hidden; /* Скрыть обратную сторону */
    }
  
    .front {
      z-index: 2; /* Передняя сторона */
      transform: rotateY(0deg);
    }
  
    .back {
      transform: rotateY(180deg); /* Задняя сторона */
    }
  
    img {
      width: 100%;
      height: 100%;
      object-fit: cover; /* масштаб изображения под контейнер */
      border-radius: 10px;
    }
  </style>
  
  <div class="flip-container">
    <div class="flipper">
      <div class="front">
        <img src={frontImage} alt="" />
      </div>
      <div class="back">
        <img src={backImage} alt="" />
      </div>
    </div>
  </div>
  