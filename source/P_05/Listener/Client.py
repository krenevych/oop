from source.P_05.Listener.FileReader import FileReader
from source.P_05.Listener.Listener import Listener


class FilePrinter(Listener):
    """ Реалізація інтерфейсу Listener
        Виводить отримані рядки на екран """
    def onReadLine(self, line):
        print(line)


class WordCounter(Listener):
    def onReadLine(self, line):
        global words_number
        words = line.split()
        words_number += len(words)


if __name__ == "__main__":
    filereader = FileReader("input.txt")

    filereader.addListener(FilePrinter())
    filereader.addListener(WordCounter())

    words_number = 0
    filereader.read()
    print(words_number)
