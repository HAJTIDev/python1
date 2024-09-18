class Note:
    __counter=0
    def __init__(self,title,content):
        Note.__counter+=1
        self.__id=Note.__counter
        self._title=title
        self._content=content
    def display(self):
        print(f'title: {self._title}\nContent: {self._content}')
    def diagnose(self):
        print(f'{self.__id};{self._title};{self._content}')
notka=Note("meow","meow")
notka.display()
notka.diagnose()