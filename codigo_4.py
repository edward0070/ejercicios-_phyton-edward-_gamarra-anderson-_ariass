# calculo_imc.py
def main() -> None:
    """Solicita peso y altura, calcula el IMC y lo muestra."""
    try:
        peso = float(input("Ingrese su peso en kilogramos: "))
        altura = float(input("Ingrese su altura en metros: "))

        if altura <= 0:
            raise ValueError("La altura debe ser mayor que cero.")

        imc = peso / (altura ** 2)
        print(f"Su IMC es: {imc:.2f}")

    except ValueError as err:
        print(f"Entrada no válida: {err}")

if __name__ == "__main__":
    main()







