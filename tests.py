from main import BooksCollector
import pytest

class TestBooksCollector:

    @pytest.fixture(autouse=True)
    def collector(self):
        self.collector = BooksCollector()
        return self.collector

    def test_add_valid_book_true(self):
        # Создание пустого списка и добавление книги с валидным названием в созданный список
        self.collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(self.collector.get_books_genre()) == 1

    positive_name_list = ['t', 'V.', 'Женщина с бумажными цветами', 'Рассказы о веселых людях,хорошей погоде', 'Рассказы о веселых людях, хорошей погоде']

    @pytest.mark.parametrize('name', positive_name_list)
    def test_add_books_with_valid_length(self, name):
        # Добавление книг с валидной длиной имени
        self.collector.add_new_book(name)
        assert self.collector.get_book_genre(name) is ''
        assert len(self.collector.get_books_genre()) in range(1, 6)

    negative_name_list = ['', 'Рассказы о веселых людях и хорошей погоде', 'Рассказы о веселых людях и хорошей погоде', 'Иллюзия «Я», или Игры, в которые играет с нами мозг']

    @pytest.mark.parametrize('name', negative_name_list)
    def test_add_books_with_not_valid_length(self, name):
        # Добавление книг с невалидной длиной имени
        self.collector.add_new_book(name)
        assert len(self.collector.get_books_genre()) == 0

    def test_add_books_genre_valid_genre(self, add_genre_in_collectors_of_books):
        self.new_collector = add_genre_in_collectors_of_books
        books_genre = self.new_collector.get_books_genre()
        books_list = {'t': 'Фантастика', 'V.': 'Детективы', 'Мастер и Маргарита': 'Мультфильмы', 'Преступление и наказание': 'Ужасы', 'Женщина с бумажными цветами': 'Комедии'}
        for name in books_genre:
            assert books_genre[name] == books_list[name]

    def test_get_books_with_specific_genre(self, add_genre_in_collectors_of_books):
        self.new_collector = add_genre_in_collectors_of_books
        books_genre = self.new_collector.get_books_genre()
        for name in books_genre:
            genre = books_genre[name]
            lst_genre = self.new_collector.get_books_with_specific_genre(genre)
            assert name in lst_genre





