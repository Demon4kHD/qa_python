import pytest

from main import BooksCollector


@pytest.fixture
def add_genre_in_collectors_of_books():
    collector = BooksCollector()
    book_list = ['t', 'V.', 'Мастер и Маргарита', 'Преступление и наказание', 'Женщина с бумажными цветами']
    for name in book_list:
        collector.add_new_book(name)
    positive_genres_list = [['t', 'Фантастика'], ['V.', 'Детективы'], ['Мастер и Маргарита', 'Мультфильмы'],
                            ['Преступление и наказание', 'Ужасы'], ['Женщина с бумажными цветами', 'Комедии']]
    for i in range(len(positive_genres_list)):
        collector.set_book_genre(positive_genres_list[i][0], positive_genres_list[i][1])
    return collector
