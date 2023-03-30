import telegram
from environs import Env
import os
import time
import random
import argparse


def main():
    env = Env()
    env.read_env()

    parser = argparse.ArgumentParser(description='Скрипт постит картинки в телеграм канал с нужным интервалом.')
    parser.add_argument('mode', choices=['image', 'images'], help='введите "image" чтобы запостить 1 картинку или "images" чтобы запостить все картинки из директории.')
    parser.add_argument('path', help='путь до картинок')
    args = parser.parse_args()

    TELEGRAM_TOKEN = env('TELEGRAM_TOKEN')
    SLEEP_SEC = env.int('SLEEP_SEC', default=14400)
    CHAT_ID=env('CHAT_ID')

    try:
        bot = telegram.Bot(token=TELEGRAM_TOKEN)
        if args.mode == 'images' and os.path.isdir(args.path):
            print('Парсим директорию...')
            images_paths = [os.path.join(path, name) for path, _, names in os.walk(args.path) for name in names]
            print('Спарсили.')
            while True:
                for image_path in images_paths:
                    print(f'Отправляем {image_path}...')
                    with open(image_path, 'rb') as photo:
                        bot.sendPhoto(chat_id=CHAT_ID, photo=photo)
                    print(f'Отправили. Ожидание {SLEEP_SEC} секунд...')
                    time.sleep(SLEEP_SEC)
                print('Картинки закончились. Перемешиваем...')    
                random.shuffle(images_paths)
                print('Перемешали.')
        elif args.mode == 'image' and os.path.isfile(args.path):
            print(f'Отправляем {args.path}...')
            with open(args.path, 'rb') as photo:
                bot.sendPhoto(chat_id=CHAT_ID, photo=photo)
            print('Отправили.')
        else:
            print('Неверный ввод.')
    except telegram.error.TelegramError:
        print('Что-то пошло не так.')
    

if __name__ == '__main__':
    main()