import requests
import images_downloader
import argparse
from environs import Env


def main():
    env = Env()
    env.read_env()

    parser = argparse.ArgumentParser(description='Скрипт скачивает нужное количество случайных фотографий NASA APOD (Astronomy Picture of the Day).')
    parser.add_argument('-a', '--amount', help='количество картинок для случайной генерации', default=1)
    parser.add_argument('-p', '--path', help='путь для сохранения картинок', default='images')
    args = parser.parse_args()

    NASA_TOKEN = env('NASA_TOKEN', default='DEMO_KEY')
    params = {
        'api_key': NASA_TOKEN,
        'thumbs': 'True',
        'count': args.amount
    }

    try:
        print('Подключаемся...')
        response = requests.get('https://api.nasa.gov/planetary/apod', params=params)
        response.raise_for_status()
        response_data = response.json()
        print('Подключились.')
        for index, data in enumerate(response_data):
            print(f'Скачиваем картинку № {index}...')
            if data['media_type'] == 'image':
                images_downloader.download_image(data['url'], args.path, f'nasa_apod_{index}')
            elif data['media_type'] == 'video':
                images_downloader.download_image(data['thumbnail_url'], args.path, f'nasa_apod_{index}')
            print(f'Картинка № {index} скачана.')
    except requests.exceptions.HTTPError:
        print('Неверное количество.')
    else:
        print('Все готово!')
    

if __name__ == '__main__':
    main()
    