from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class MultiFunctionDevice(Printer, Scanner):
    def print(self, document):
        print(f"Printing: {document}")

    def scan(self, document):
        print(f"Scanning: {document}")

class SimplePrinter(Printer):
    def print(self, document):
        print(f"Printing: {document}")

# Хорошая практика:
# Классы, которые должны только печатать или сканировать, могут реализовывать конкретные интерфейсы.
