import json
from livereload import Server
from jinja2 import Environment, FileSystemLoader, select_autoescape


def on_reload(books):
    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader, autoescape=select_autoescape(['html', 'xml']))
    template = env.get_template('template.html')
    rendered_page = template.render(books=books)
    with open('index.html', 'w', encoding="UTF-8") as file:
        file.write(rendered_page)


def rebuild():
    with open('book.json', 'r', encoding='UTF-8') as file:
        book_json = file.read()
    books = json.loads(book_json)
    on_reload(books)
    print("Site rebuilt")


def main():
    rebuild()
    server = Server()
    server.watch('template.html', rebuild)
    server.serve(root='.')


if __name__ == '__main__':
    main()
