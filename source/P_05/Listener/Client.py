from source.P_05.Listener.FileReader import FileReader
from source.P_05.Listener.Listener import Listener


class FilePrinter(Listener):
    """ Реалізація інтерфейсу Listener
        Виводить отримані рядки на екран """

    def onDataReceive(self, line):
        print(line)


class WordCounter(Listener):
    """ Реалізація інтерфейсу Listener
        Підраховує кількість слів у текстовому файлі """

    def onDataReceive(self, line):
        global words_number
        words = line.split()
        words_number += len(words)


if __name__ == "__main__":
    filereader = FileReader("input.txt")

    filereader.registerListener(FilePrinter())
    filereader.registerListener(WordCounter())

    words_number = 0
    filereader.read()
    print(words_number)
