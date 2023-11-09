class Display:
    def __init__(self, symbol: str, size: int):
        self._symbol_ = symbol + "  " if symbol else "#  "
        self._size_ = size if size else 10

        self._array_ = ""

    def display(self) -> None:
        for length in range(self._size_, 0, -1):
            line = self._symbol_ * length + "\n"
            print(line, end="")

            self._array_ += line

    def to_file(self) -> None:
        with open("file.txt", "w") as file:
            file.write(self._array_)


def main():
    symbol = input("Enter the symbol: ")
    size = int(input("Enter the size: "))

    display = Display(symbol, size)

    display.display()
    display.to_file()


if __name__ == '__main__':
    main()
