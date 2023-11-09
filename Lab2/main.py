class Plant:
    def __init__(self, name: str, kind: str, age: float):
        self._name_ = name
        self._kind_ = kind
        self._age_ = age

        self._water_ = 1
        self._alive_ = True

    @property
    def name(self) -> str: return self._name_

    @property
    def kind(self) -> str: return self._kind_

    @property
    def age(self) -> float: return self._age_

    @property
    def alive(self) -> bool: return self._alive_

    def __repr__(self) -> str: return f"Name: {self._name_}\nKind: {self._kind_}\nAge: {self._age_}\n"

    def growth(self, value: float = 0.083) -> None:
        """
        Increase age by given value if plant is alive
        Standard value is one month or 1 / 12 of the year
        """
        if self._alive_:
            self._age_ += value

    def decay(self) -> None:
        """
        Changes the alive flag to False
        """
        self._alive_ = False

    def water(self) -> None:
        """
        Increase plant water amount
        """
        self._water_ += 0.1


def main():
    plant = Plant("Павуча Лілія", "Квітка", 1)

    plant.growth()
    print(plant)


if __name__ == '__main__':
    main()
