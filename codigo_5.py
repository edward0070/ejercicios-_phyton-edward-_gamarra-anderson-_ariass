# conversor_temperatura.py
def celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte grados Celsius a Fahrenheit."""
    return celsius * 1.8 + 32


def fahrenheit_a_celsius(fahrenheit: float) -> float:
    """Convierte grados Fahrenheit a Celsius."""
    return (fahrenheit - 32) / 1.8


def main() -> None:
    """Menú principal: pide la opción y la temperatura, y muestra la conversión."""
    print("Conversor de temperaturas")
    print("1) Celsius → Fahrenheit")
    print("2) Fahrenheit → Celsius")

    try:
        opcion = int(input("Elija una opción (1 o 2): ").strip())
        if opcion not in (1, 2):
            raise ValueError("La opción debe ser 1 o 2.")

        temp = float(input("Ingrese la temperatura a convertir: ").strip())

        if opcion == 1:
            resultado = celsius_a_fahrenheit(temp)
            print(f"{temp:.2f} °C equivalen a {resultado:.2f} °F")
        else:
            resultado = fahrenheit_a_celsius(temp)
            print(f"{temp:.2f} °F equivalen a {resultado:.2f} °C")

    except ValueError as err:
        print(f"Entrada no válida: {err}")


if __name__ == "__main__":
    main()


