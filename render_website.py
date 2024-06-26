import argparse
import json
import os
import urllib.parse

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked


NUMBER_OF_BOOKS = 10


def on_reload(books):
    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader, autoescape=select_autoescape(['html', 'xml']))
    folder = 'pages/'
    os.makedirs(folder, exist_ok=True)
    divide_pages = list(chunked(books, NUMBER_OF_BOOKS))
    for page_number, books in enumerate(divide_pages):
        encode_path(books)
        template = env.get_template('template.html')
        rendered_page = template.render(books=books, page_number=page_number, number_of_pages=len(divide_pages))
        complete_path = os.path.join(folder, f'index{page_number + 1}.html')
        with open(complete_path, 'w', encoding="UTF-8") as file:
            file.write(rendered_page)


def encode_path(books):
    folder = '../media/'
    for book in books:
        image_path = os.path.join(folder, book['img_src'])
        text_path = os.path.join(folder, book['book_path'])
        book['img_src'] = urllib.parse.quote(image_path)
        book['book_path'] = urllib.parse.quote(text_path)


def rebuild(path):
    with open(path, 'r', encoding='UTF-8') as file:
        books = json.load(file)
    on_reload(books)
    return books


def main():
    parser = argparse.ArgumentParser(
        description='Онлайн библиотека'
    )
    parser.add_argument('--path', default='book.json', type=str, help='Путь к кофигурационному файлу')
    args = parser.parse_args()
    path = args.path
    books = rebuild(path)
    server = Server()
    server.watch('template.html', lambda: on_reload(books))
    server.serve(root='.', default_filename='pages/index1.html')


if __name__ == '__main__':
    main()
