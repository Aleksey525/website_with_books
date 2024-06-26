# Скрипт для верстки онлайн-библиотеки

Скрипт для формирования и верстки сайта с онлайн - библиотекой из книг скачанных с [tululu.org](https://tululu.org/)

![screenshot](https://github.com/Aleksey525/static_site/blob/main/image.jpg/)
### Как установить

Python3 должен быть уже установлен. Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

```

pip install -r requirements.txt

```

### Сценарии использования

* Скачать готовый сайт с онлайн - библиотекой:  
Чтобы начать пользоваться локальной версией сайта, нужно скачать файлы репозитория на свой компьютер. Затем перейти
в папку `pages` и открыть в браузере любой `html` файл.   
  Ссылка на опубликованный сайт - 
[website_with_books](https://aleksey525.github.io/website_with_books/pages/index1.html)
#####
* Запустить скрипт и развернуть сайт:
  ```
  python main.py render_website.py
  ```
  ```
  [I 240621 06:21:19 server:335] Serving on http://127.0.0.1:5500
  [I 240621 06:21:19 handlers:62] Start watching changes
  [I 240621 06:21:19 handlers:64] Start detecting changes
  ```
  Cкрипт создает 10 `html` файлов в директории `pages`. Данные о книгах берутся из `book.json`, который находится в корневой директории. 
  Изображения книг с расширением `.jpg` из директории `images`, текстовые файлы книг с расширением `.txt` из директории `books`.
  В скрипт интегрирован свой `live server`, который отслеживает все изменения в `template.html`. После запуска сайт доступен по 
  адресу http://127.0.0.1:5500/pages/index1.html.
#####
* Пример запуска скрипта с указанием пути до файла с данными:
  ```
  python main.py render_website.py --path ../name.json
  ```
### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).



  

 


