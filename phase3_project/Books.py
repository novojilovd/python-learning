from Literature import Literature


class Books(Literature):
    def __init__(self, *,
                 name: str = '',
                 pages: int = 0,
                 author: str = '',
                 ISBN: str = '',
                 genre: str = '',
                 publisher: str = '') -> None:
        super().__init__(name = name,
                         pages = pages,
                         author = author,
                         ISBN = ISBN,
                         genre = genre,
                         publisher = publisher)

    def get_full_info(self) -> dict:
        return dict(ISBN = self.ISBN,
                    name = self.name,
                    author = self.author,
                    pages = self.pages,
                    genre = self.genre,
                    publisher = self.publisher)

    def edit_info(self, **kwargs) -> None:
        for key, value in kwargs.items():
            if key in ["ISBN", "name", "author", "pages", "genre", "publisher"]:

                if key == "pages" and not isinstance(value, int):
                    print(f'{key} is not a int number')
                elif key in ["ISBN", "name", "author", "genre", "publisher"] and not isinstance(value, str):
                    print(f'{key} is not a string')

                setattr(self, key, value)


    def show_info(self) -> None:
        print(f'ISBN: {'Добавьте ISBN' if self.ISBN == '' else self.ISBN}'
              f'\nName: {'Добавьте название' if self.name == '' else self.name}'
              f'\nAuthor: {'Добавьте автора' if self.author == '' else self.author}'
              f'\nPages: {'Добавьте количество страниц' if self.pages == 0 else self.pages}'
              f'\nGenre: {'Добавьте жанр' if self.genre == '' else self.genre}'
              f'\nPublisher: {'Добавьте издателя' if self.publisher == '' else self.publisher}'
                )