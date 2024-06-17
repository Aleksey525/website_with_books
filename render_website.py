import json

from jinja2 import Environment, FileSystemLoader, select_autoescape


def main():
    with open('book.json', 'r', encoding='UTF-8') as file:
        book_json = file.read()
    books = json.loads(book_json)

    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)

    template = env.get_template('template.html')
    rendered_page = template.render(books=books)

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

if __name__ == '__main__':
    main()





