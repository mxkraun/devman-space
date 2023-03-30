import requests
import images_downloader
import argparse
from datetime import datetime
from environs import Env


def main():
    env = Env()
    env.read_env()

    parser = argparse.ArgumentParser(description='Скрипт скачивает фотографии NASA EPIC (Earth Polychromatic Imaging Camera) за нужную дату.')
    parser.add_argument('date', help='дата в формате d-m-Y')
    parser.add_argument('-p', '--path', help='путь для сохранения картинок', default='images')
    args = parser.parse_args()

    NASA_TOKEN = env('NASA_TOKEN', default='DEMO_KEY')
    params = {
        'api_key': NASA_TOKEN,
    } 

    mydate = datetime.strptime(args.date, '%d-%m-%Y')
    day, month, year = mydate.day, mydate.month, mydate.year

    try:
        print('Подключаемся...')
        response = requests.get(f'https://epic.gsfc.nasa.gov/api/natural/date/{year}-{month:02}-{day:02}', params=params)
        response.raise_for_status()
        response_data = response.json()
        print('Подключились.')
        if not response_data:
            print('Нет картинок за этот день.')
        for index, data in enumerate(response_data):
            print(f'Скачиваем картинку № {index}...')
            image_name = data['image']
            url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month:02}/{day:02}/png/{image_name}.png'
            images_downloader.download_image(url, args.path, f'nasa_epic_{index}', params)
            print(f'Картинка № {index} скачана.')
    except requests.exceptions.HTTPError:
        print('Ошибка подключения.')
    else:
        print('Все готово!')
    

if __name__ == '__main__':
    main()
    