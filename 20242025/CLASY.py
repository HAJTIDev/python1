class Note:
    __counter = 0

    def __init__(self, title, content):
        Note.__counter += 1
        self.__id = Note.__counter
        self._title = title
        self._content = content

    def display(self):
        print(f"Title: {self._title}\nContent: {self._content}")

    def diagnose(self):
        print(f"{self.__id};{self._title};{self._content}")


# Test działania aplikacji
note1 = Note("Title1", "Content1")
note1.display()
note1.diagnose()

note2 = Note("Title2", "Content2")
note2.display()
note2.diagnose()