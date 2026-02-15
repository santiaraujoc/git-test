def dividirNumeros(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    print(f"División: {a / b}")