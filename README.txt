Это описание и документация будущего проекта. 


# Проект Django

## Установка

1. Установите Python версии 3.12.
2. Создайте виртуальное окружение, если нет:

python -m venv venv

3. Активируйте окружение:
- Windows:
  ```
  .\venv\Scripts\activate
  ```
- Linux/MacOS:
  ```
  source venv/bin/activate
  ```
4. Установите зависимости:

pip install -r requirements.txt

5. Запустите сервер:

cd .\kind_soul\

python manage.py runserver


Обновление и добавление зависимостей в проект:

pip freeze > requirements.txt