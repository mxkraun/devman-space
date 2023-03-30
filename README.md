# Космический Телеграм
Эти скрипты могут скачать "космические" фотографии и запостить их в телеграм канале.

## Окружение
### Зависимости
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```bash
pip install -r requirements.txt
```

### Переменные окружения
#### Для `fetch_nasa_apod.py` и `fetch_nasa_epic.py`
- NASA_TOKEN=DEMO_KEY
#### Для `telegram_poster.py`
- TELEGRAM_TOKEN
- CHAT_ID
- SLEEP_SEC=14400

1. Поместите файл `.env` рядом со скриптами.
2. `.env` содержит текстовые данные без кавычек.

Например, если вы распечатаете содержимое `.env`, то увидите:

```bash
$ cat .env
NASA_TOKEN=DEMO_KEY
TELEGRAM_TOKEN=1111111111:qweasdASCAEr235tgdfESFSFd
CHAT_ID=@channel_name
SLEEP_SEC=14400
```

#### Как получить `NASA_TOKEN`
Зарегистрироваться на [api.nasa.gov](https://api.nasa.gov/#signUp). Токен придет на e-mail.

#### Как получить `TELEGRAM_TOKEN`
Создать своего телеграм бота с помощью [@BotFather](https://telegram.me/BotFather). Он выдаст токен.

#### Как получить `CHAT_ID`
CHAT_ID это ссылка на телеграм канал, например: @telegram

#### Как получить `SLEEP_SEC`
Установите время ожидания в секундах между постами.

## Как запустить
Файл `images_downloader.py` должен быть рядом с запускаемым скриптом, кроме `telegram_poster.py`
### `fetch_nasa_apod.py`
Запуск на Linux(Python 3) или Windows:

```bash
$ python fetch_nasa_apod.py [-a AMOUNT] [-p PATH]
```
Вы увидите:

```
Подключаемся...
Подключились.
Скачиваем картинку № 0...
Картинка № 0 скачана.
Скачиваем картинку № 1...
Картинка № 1 скачана.
...
Все готово!
```
Используйте `--help`, чтобы узнать подробности.
```bash
$ python fetch_nasa_apod.py --help
```
### `fetch_nasa_epic.py`
Запуск на Linux(Python 3) или Windows:

```bash
$ python fetch_nasa_epic.py [-p PATH] date
```
Вы увидите:

```
Подключаемся...
Подключились.
Скачиваем картинку № 0...
Картинка № 0 скачана.
Скачиваем картинку № 1...
Картинка № 1 скачана.
...
Все готово!
```
Используйте `--help`, чтобы узнать подробности.
```bash
$ python fetch_nasa_epic.py --help
```
### `fetch_spacex_images.py`
Запуск на Linux(Python 3) или Windows:

```bash
$ python fetch_spacex_images.py [-id LAUNCH_ID] [-p PATH]
```
Вы увидите:

```
Подключаемся...
Подключились.
Скачиваем картинку № 0...
Картинка № 0 скачана.
Скачиваем картинку № 1...
Картинка № 1 скачана.
...
Все готово!
```
Используйте `--help`, чтобы узнать подробности.
```bash
$ python fetch_spacex_images.py --help
```
### `telegram_poster.py`
Запуск на Linux(Python 3) или Windows:

```bash
$ python telegram_poster.py {image,images} path 
```
Вы увидите:

```
Парсим директорию...
Спарсили.
Отправляем images\my_image_0.jpg...
Отправили. Ожидание 14400 секунд...
Отправляем images\my_image_1.jpg...
Отправили. Ожидание 14400 секунд...
...
Картинки закончились. Перемешиваем...
Перемешали.
Отправляем images\my_image_7.jpg...
Отправили. Ожидание 14400 секунд...
Отправляем images\my_image_1.jpg...
Отправили. Ожидание 14400 секунд...
...
```
или
```
Отправляем images\my_image_4.jpg...
Отправили.
```

Используйте `--help`, чтобы узнать подробности.
```bash
$ python fetch_spacex_images.py --help
```
## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).