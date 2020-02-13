from source.P_05.L11_FileReader import FileReader
from source.P_05.L12_Observer import Observer


class FilePrinter(Observer):
    """ Реалізація інтерфейсу Observer
        Виводить отримані рядки на екран """

    def onDataReceive(self, line):
        print(line)


class WordCounter(Observer):
    """ Реалізація інтерфейсу Observer
        Підраховує кількість слів у текстовому файлі
        Тут під словом будемо розуміти послідовність літер, що відокремлена одним або кількома символами пропуску.
    """

    def onDataReceive(self, line):
        global words_number
        words = line.split()
        words_number += len(words)


if __name__ == "__main__":
    filereader = FileReader("input.txt")

    filereader.register_observers(FilePrinter())
    filereader.register_observers(WordCounter())

    words_number = 0
    filereader.read()
    print(words_number)
