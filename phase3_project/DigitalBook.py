from Books import Books


class DigitalBook(Books):
    def __init__(self, *,
                 name: str = '',
                 pages: int = 0,
                 author: str = '',
                 ISBN: str = '',
                 genre: str = '',
                 publisher: str = '',
                 size: float = 0.0,
                 file_path: str = ''):
        super().__init__(name = name,
                         pages = pages,
                         author = author,
                         ISBN = ISBN,
                         genre = genre,
                         publisher = publisher)
        self.size = size
        self.file_path = file_path

    def get_full_info(self) -> dict:
        result = super().get_full_info()
        result.update({'size': self.size, 'file_path': self.file_path})
        return result

    def edit_info(self, **kwargs) -> None:
        super().edit_info(**kwargs)
        for key, value in kwargs.items():
            if key in ["size", "file_path"]:

                if key == "size" and not isinstance(value, float):
                    print(f'{key} is not a float number')
                elif key in ["file_path"] and not isinstance(value, str):
                    print(f'{key} is not a string')

                setattr(self, key, value)

    def show_info(self) -> str:
        super().show_info()
        print(f'Size: {'Добавьте размер файла' if self.size == 0.0 else self.size}'
              f'\nfile_path: {'Добавьте путь к файлу' if self.file_path == '' else self.file_path}')
