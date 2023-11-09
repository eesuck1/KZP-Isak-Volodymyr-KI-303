from sympy import limit, Symbol, tan


def main():
    x = Symbol("x")
    function = tan(x) / (3 * x)

    with open("result.txt", "w") as file:
        value = float(input("Enter the x value: "))
        result = limit(function, x, value).evalf()

        print(f"Result: {result} was successfully written into result.txt")

        file.write(str(result))


if __name__ == '__main__':
    main()
