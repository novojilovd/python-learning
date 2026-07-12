from abc import ABC, abstractmethod


class Literature(ABC):
    @abstractmethod
    def __init__(self, *,
                 name: str = '',
                 pages: int = 0,
                 ISBN: str = '',
                 genre: str = '',
                 publisher: str = '') -> None:
        self.name = name
        self.ISBN = ISBN
        self.pages = pages
        self.genre = genre
        self.publisher = publisher


    @abstractmethod
    def get_full_info(self) -> dict:
        pass

    @abstractmethod
    def edit_info(self, **kwargs) -> None:
        pass

    @abstractmethod
    def show_info(self) -> None:
        pass