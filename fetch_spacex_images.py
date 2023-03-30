import requests
import images_downloader
import argparse


def main():
    parser = argparse.ArgumentParser(description='Скрипт скачивает фотографии с зауска spaceX за нужную дату.')
    parser.add_argument('-id', '--launch_id', help='ID запуска spaceX', default='latest')
    parser.add_argument('-p', '--path', help='путь для сохранения картинок', default='images')
    args = parser.parse_args()

    try:
        print('Подключаемся...')
        response = requests.get(f'https://api.spacexdata.com/v5/launches/{args.launch_id}')
        response.raise_for_status()
        urls = response.json()['links']['flickr']['original']
        print('Подключились.') 
        for index, url in enumerate(urls):
            print(f'Скачиваем картинку № {index}...')
            images_downloader.download_image(url, args.path, f'spacex_{index}')
            print(f'Картинка № {index} скачана.')
        if not urls:
            print(f'Нет картинок с ID "{args.launch_id}"') 
    except requests.exceptions.HTTPError:
        print('Неверный ID.')
    else:
        print('Все готово!')
    

if __name__ == '__main__':
    main()   
    