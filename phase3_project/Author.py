class Author:
        def __init__(self,
                     name: str = '',
                     works: list[str] = []):
            self.name = name
            self.works = works

        def show_works(self):
            for work in self.works:
                print(work)