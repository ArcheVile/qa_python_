import pytest
from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize("name", ["А" * 41, "Б" * 100])
    def test_add_new_book_name_too_long(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    @pytest.mark.parametrize("book, genre", [("1984", "Фантастика"), ("Шутка", "Комедии")])
    def test_set_book_genre_valid_genre(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == genre

    @pytest.mark.parametrize("book_name", ["Неизвестная книга", "", "123"])
    def test_get_book_genre_returns_none_if_book_not_added(self, book_name):
        collector = BooksCollector()
        assert collector.get_book_genre(book_name) is None

    def test_get_book_genre_returns_correct_genre_after_setting(self):
        collector = BooksCollector()
        book_name = "Гарри Поттер"
        genre = "Фантастика"

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        assert collector.books_genre[book_name] == genre
        assert collector.get_book_genre(book_name) == genre

    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1', 'Комедии')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 2', 'Фантастика')
        assert collector.get_books_with_specific_genre('Комедии') == ['Книга 1']

    def test_get_books_for_children_excludes_age_restricted(self):
        collector = BooksCollector()
        collector.add_new_book('Хоррор')
        collector.set_book_genre('Хоррор', 'Ужасы')
        collector.add_new_book('Комедия')
        collector.set_book_genre('Комедия', 'Комедии')
        assert collector.get_books_for_children() == ['Комедия']

    def test_add_book_in_favorites_adds_only_once(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        collector.add_book_in_favorites('1984')  # повторно
        assert collector.get_list_of_favorites_books() == ['1984']

    def test_delete_book_from_favorites_removes_if_exists(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        collector.delete_book_from_favorites('1984')
        assert collector.get_list_of_favorites_books() == []

    def test_get_books_genre_returns_actual_genre_dict(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        expected = {'1984': ''}
        assert collector.get_books_genre() == expected

    def test_get_list_of_favorites_books_returns_correct_list(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        assert collector.get_list_of_favorites_books() == ['1984']
