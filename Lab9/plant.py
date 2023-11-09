from abc import ABC, abstractmethod


class Plant(ABC):
    def __init__(self, name: str, kind: str, age: float):
        self._name_ = name
        self._kind_ = kind
        self._age_ = age
        self._alive_ = True

    @property
    def name(self) -> str: return self._name_

    @property
    def kind(self) -> str: return self._kind_

    @property
    def age(self) -> float: return self._age_

    @property
    def alive(self) -> bool: return self._alive_

    @abstractmethod
    def __repr__(self) -> str: ...

    @abstractmethod
    def growth(self, value: float = 0.083) -> None: ...

    @abstractmethod
    def decay(self) -> None: ...

    @abstractmethod
    def water(self) -> None: ...


class Tree(Plant, ABC):
    def __init__(self, name: str, kind: str, age: float):
        super().__init__(name, kind, age)

        self._water_ = 1

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
