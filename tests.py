from main import BooksCollector
import pytest

class TestBooksCollector:

    @pytest.fixture(autouse=True)
    def collector(self):
        self.collector = BooksCollector()
        return self.collector

    def test_add_valid_book_true(self):
        self.collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(self.collector.get_books_genre()) == 1

    positive_name_list = ['t', 'V.', 'Женщина с бумажными цветами', 'Рассказы о веселых людях,хорошей погоде', 'Рассказы о веселых людях, хорошей погоде']

    @pytest.mark.parametrize('name', positive_name_list)
    def test_add_books_with_valid_length_true(self, name):
        self.collector.add_new_book(name)
        assert self.collector.get_book_genre(name) is ''
        assert len(self.collector.get_books_genre()) in range(1, 6)

    negative_name_list = ['', 'Рассказы о веселых людях и хорошей погоде', 'Рассказы о веселых людях и хорошей погоде', 'Иллюзия «Я», или Игры, в которые играет с нами мозг']

    @pytest.mark.parametrize('name', negative_name_list)
    def test_add_books_with_not_valid_length_false(self, name):
        self.collector.add_new_book(name)
        assert len(self.collector.get_books_genre()) == 0

    def test_add_books_genre_valid_genre_true(self, add_genre_in_collectors_of_books):
        self.new_collector = add_genre_in_collectors_of_books
        books_genre = self.new_collector.get_books_genre()
        books_list = {'t': 'Фантастика', 'V.': 'Детективы', 'Мастер и Маргарита': 'Мультфильмы', 'Преступление и наказание': 'Ужасы', 'Женщина с бумажными цветами': 'Комедии'}
        for name in books_genre:
            assert books_genre[name] == books_list[name]

    def test_get_books_with_specific_genre_true(self, add_genre_in_collectors_of_books):
        self.new_collector = add_genre_in_collectors_of_books
        books_genre = self.new_collector.get_books_genre()
        for name in books_genre:
            genre = books_genre[name]
            lst_genre = self.new_collector.get_books_with_specific_genre(genre)
            assert name in lst_genre

    def test_number_books_for_children_true(self, add_genre_in_collectors_of_books):
        self.new_collector = add_genre_in_collectors_of_books
        assert len(self.new_collector.get_books_for_children()) == 3

    genre_not_age_rating = ['t', 'Мастер и Маргарита', 'Женщина с бумажными цветами']

    def test_genre_books_for_children_in_collector_true(self, add_genre_in_collectors_of_books):
        self.new_collector = add_genre_in_collectors_of_books
        list_for_comparison = self.new_collector.get_books_for_children()
        for i in range(len(list_for_comparison)):
            assert self.genre_not_age_rating[i] == list_for_comparison[i]

    def test_number_book_in_favorites_true(self, add_genre_in_collectors_of_books):
        self.new_collector = add_genre_in_collectors_of_books
        for name in self.new_collector.get_books_genre():
            self.new_collector.add_book_in_favorites(name)
        assert len(self.new_collector.get_list_of_favorites_books()) == len(self.new_collector.get_books_genre())

    def test_add_second_book_in_favorites_true(self, add_genre_in_collectors_of_books):
        self.new_collector = add_genre_in_collectors_of_books
        for name in self.new_collector.get_books_genre():
            self.new_collector.add_book_in_favorites(name)
        self.new_collector.add_book_in_favorites('Мастер и Маргарита')
        assert len(self.new_collector.get_list_of_favorites_books()) == len(self.new_collector.get_books_genre())

    def test_delete_book_from_favorites_true(self, add_genre_in_collectors_of_books):
        self.new_collector = add_genre_in_collectors_of_books
        for name in self.new_collector.get_books_genre():
            self.new_collector.add_book_in_favorites(name)
        self.new_collector.delete_book_from_favorites('Мастер и Маргарита')
        assert 'Мастер и Маргарита' not in self.new_collector.get_list_of_favorites_books()

    def test_delete_book_which_not_in_favorites_true(self, add_genre_in_collectors_of_books):
        self.new_collector = add_genre_in_collectors_of_books
        for name in self.new_collector.get_books_genre():
            self.new_collector.add_book_in_favorites(name)
        self.new_collector.delete_book_from_favorites('Мастер и Маргарита')
        self.new_collector.delete_book_from_favorites('Мастер и Маргарита')
        assert 'Мастер и Маргарита' not in self.new_collector.get_list_of_favorites_books()