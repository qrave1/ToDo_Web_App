# ToDo - Время дороже всего

## ToDo менеджер, реализованный на фреймворке FastAPI

## Развёртывание приложения на Windows
Создаём и активируем виртуальное окружение
```sh
python -m venv venv
. venv/Scripts/activate
```
Устанавливаем необходимые пакеты
```sh
pip install -r requirements.txt
```
Создаем файл окружения .env и записываем туда NAME_APP и SQLALCHEMY_DATABASE_URL
Запускаем приложение через веб-сервер uvicorn
```sh
uvicorn main:app --reload --port 5000
```