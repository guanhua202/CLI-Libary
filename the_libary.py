# Beta v0.1

from time import sleep

print()
print("         📚 Моя Библиотека")
print()
print("1. Информация о книгах (> 1)")
print("2. Добавить книгу")
print("3. Удалить книгу (> 1)")
print("0. Выйти из Библиотеки")
print("-------------------------------------")
print()
print("Примечание: (> 1) означает что есть под-варианты для выполнения точного действия")
print()

select_action = int(input("Выберите действие: "))

books = [{"title" : "Bushido",
	"author" : "Yudzan Daydodzi/Yamamoto Zunetomo",
	"year" : "1998",
	"read" : False},
]

while select_action != 0:

	if select_action == 1:

		print()
		for i in range(0, len(books)):
			print()
			print(f"📔 Информация о книге №{i + 1}:")
			print()
			print(f"Название: {books[i]['title']}")
			print(f"Автор: {books[i]['author']}")
			print(f"Год: {books[i]['year']}")
			print(f"Прочитано: {books[i]['read']}")
		print()

	elif select_action == 2:
		new_book_name = str(input("Введите название новой книги: "))
		new_book_author = str(input("Кто написал эту книгу: "))
		new_book_year = str(input("В каком году вышла книга: "))
		new_book_read = int(input("Вы читали её?(Да - 1, Нет - 2): "))

		if new_book_read == 1:
			new_book_read = True
		else:
			new_book_read = False

		new_book = {"title" : new_book_name, "author" : new_book_author, "year" : new_book_year, "read" : new_book_read}

		books.append(new_book)
		print("Книга успешно добавлена!")

	elif select_action == 3:
		del_book_num = int(input("Введите № книги для удаления: "))

		for book in range(0, len(books)):
			if del_book_num - 1 == book:

				print("Будет удалена следующая книга: ")
				print()
				print(f"📔 Информация о книге №{book + 1}:")
				print()
				sleep(1)
				print(f"Название: {books[book]['title']}")
				print(f"Автор: {books[book]['author']}")
				print(f"Год: {books[book]['year']}")
				print(f"Прочитано: {books[book]['read']}")
				sleep(1)
				print()

				confirm = str(input("Удалить?(Y/N): ")).lower()

				if confirm == 'y':
					del books[book]
					print("Книга была удалена.")
				elif confirm == 'n':
					print("Операция прервана.")
				else:
					print("Вводите только Y или N.")

	print()
	print("         📚 Моя Библиотека")
	print()
	print("1. Информация о книгах (> 1)")
	print("2. Добавить книгу")
	print("3. Удалить книгу (> 1)")
	print("0. Выйти из Библиотеки")
	print("-------------------------------------")
	print()

	select_action = int(input("Выберите действие: "))
