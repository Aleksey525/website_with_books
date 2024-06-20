import json
import os
from livereload import Server
from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked


def on_reload(books):
    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader, autoescape=select_autoescape(['html', 'xml']))
    folder = 'pages/'
    os.makedirs(folder, exist_ok=True)
    divide_pages = list(chunked(books, 10))
    for page_number, books in enumerate(divide_pages):
        template = env.get_template('template.html')
        rendered_page = template.render(books=books, page_number=page_number, number_of_pages=len(divide_pages))
        complete_path = os.path.join(folder, f'{page_number + 1}index.html')
        with open(complete_path, 'w', encoding="UTF-8") as file:
            file.write(rendered_page)


def rebuild():
    with open('book.json', 'r', encoding='UTF-8') as file:
        book_json = file.read()
    books = json.loads(book_json)
    on_reload(books)
    print("Site rebuilt")
    return books


def main():
    rebuild()
    server = Server()
    server.watch('template.html', rebuild)
    server.serve(root='.')


if __name__ == '__main__':
    main()
