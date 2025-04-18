# qa_python
add_new_book				    test_add_new_book_name_too_long							        #Проверяет, что книги с именем длиннее 40 символов не добавляются
set_book_genre				    test_set_book_genre_valid_genre							        #Проверяет установку жанра у добавленной книги
get_book_genre				    test_get_book_genre_returns_none_if_book_not_added				#Проверяет, что жанр несуществующей книги — None
get_books_with_specific_genre		test_get_books_with_specific_genre_returns_correct_books		#Проверяет список книг определённого жанра
get_books_for_children			test_get_books_for_children_excludes_age_restricted				#Проверяет, что книги с возрастным ограничением не возвращаются
add_book_in_favorites			test_add_book_in_favorites_adds_only_once						#Проверяет, что книга не добавляется в избранное повторно
delete_book_from_favorites		test_delete_book_from_favorites_removes_if_exists				#Проверяет удаление книги из избранного
get_books_genre				    test_get_books_genre_returns_actual_genre_dict					#Проверяет, что словарь книг возвращается корректно
get_list_of_favorites_books		test_get_list_of_favorites_books_returns_correct_list			#Проверяет список избранных книг