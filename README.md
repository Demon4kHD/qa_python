# qa_python_4    

[Pull request можно посмотреть здесь](https://github.com/Demon4kHD/qa_python "Мамой клянусь - сам сделал")

#### В классе TestBooksCollector использованы следующие фикстуры:

* **collector** - (autouse=True) - фикстура создания объекта класса BooksCollector()
* **add_genre_in_collectors_of_books** - создает класс, наполнает его данными о книге и рейтинге из Таблицы*

#### В классе TestBooksCollector использованы следующие методы:

1. **test_add_valid_book_true** - возможность добавить книгу по названию
2. **test_add_books_with_valid_length_true** - возможность добавления нескольких книг с пустым значением жанра
3. **test_add_books_with_not_valid_length_false** - добавление книг с не валидными данными о книге из Таблицы*
4. **test_add_books_genre_valid_genre_true** - добавление книг с валиднымиданными о книге и рейтинге из Таблицы*
5. **test_get_books_with_specific_genre_true** - получение списка книг конкретного жанра
6. **test_number_books_for_children_true** - получение размера списка из книг без возрастного ценза.
7. **test_genre_books_for_children_in_collector_true** - получение списка из трех книг без возрастного ценза
8. **test_number_book_in_favorites_true** - добавление книги в избранное
9. **test_add_second_book_in_favorites_true** - добавление дубля книги и вывод списка
10. **test_delete_book_from_favorites_true** - удалени книги
11. **test_delete_book_which_not_in_favorites_true** - повторное удалени книги, уже удаленной.


### Таблица тестовых данных для проверки ГЗ:

| Название существующей книги | Кол-во символов |    Жанр     |
|:-:|:-:|:-----------:|
| t | 1 | Фантастика  |
| V. | 2 |  Детектив   | 
| Мастер и Маргарита | 18 | Мультфильм  |
| Преступление и наказание | 24 |    Ужасы    |
| Женщина с бумажными цветами | 27 |   Комедии   | 
| Рассказы о веселых людях и хорошей погоде | 41 | Мультфильмы |
|Иллюзия «Я», или Игры, в которые играет с нами мозг | 51 |    Ужасы    |


[А для хорошего настрения лови трек!](https://music.yandex.ru/album/25862435/track/113840603)
