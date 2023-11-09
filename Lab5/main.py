import struct

from sympy import limit, Symbol, tan


class Expression:
    def __init__(self, value: float, decimal_path: str = "decimal.txt", binary_path: str = "binary.txt"):
        self._value_ = value

        self._x_ = Symbol("x")
        self._function_ = tan(self._x_) / (3 * self._x_)

        self._result_: float | None = None
        self._decimal_path_ = decimal_path
        self._binary_path_ = binary_path

    def solve(self) -> None:
        self._result_ = limit(self._function_, self._x_, self._value_).evalf()

    def write_decimal(self) -> None:
        with open(self._decimal_path_, "w") as file:
            file.write(str(self._result_))

    def read_decimal(self) -> float:
        with open(self._decimal_path_, "r") as file:
            return float(file.read())

    def write_binary(self) -> None:
        with open(self._binary_path_, "wb") as file:
            file.write(struct.pack("!f", self._result_))

    def read_binary(self) -> float:
        with open(self._binary_path_, "rb") as file:
            return struct.unpack("!f", file.read())[0]


def main():
    expression = Expression(0)

    expression.solve()
    expression.write_binary()
    expression.write_decimal()

    print(f"Result from binary file: {expression.read_binary()}")
    print(f"Result from txt file: {expression.read_decimal()}")


if __name__ == '__main__':
    main()
