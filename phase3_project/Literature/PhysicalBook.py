from Books import Books


class PhysicalBook(Books):
    def __init__(self, *,
                 name: str = '',
                 pages: int = 0,
                 ISBN: str = '',
                 genre: str = '',
                 publisher: str = '',
                 weight: float = 0.0,
                 cover: str = '') -> None:
        super().__init__(name = name,
                         pages = pages,
                         ISBN = ISBN,
                         genre = genre,
                         publisher = publisher)
        self.weight = weight
        self.cover = cover

    def get_full_info(self) -> dict:
        result = super().get_full_info()
        result.update({'weight': self.weight, 'cover': self.cover})
        return result

    def edit_info(self, **kwargs) -> None:
        super().edit_info(**kwargs)
        for key, value in kwargs.items():
            if key in ["weight", "cover"]:

                if key == "weight" and not isinstance(value, float):
                    print(f'{key} is not a float number')
                elif key in ["cover"] and not isinstance(value, str):
                    print(f'{key} is not a string')

                setattr(self, key, value)

    def show_info(self) -> None:
        super().show_info()
        print(f'Weight: {'Добавьте вес' if self.weight == 0.0 else self.weight}'
              f'\nCover: {'Добавьте тип обложки' if self.cover == '' else self.cover}')