from multiplicacion import multiplicarNumeros

print("Ingrese Numero 1: ")
num1 = int(input())
print("Ingrese Numero 2: ") 
num2 = int(input())

print("Elige una operacion: ")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")

opcion = int(input())
match opcion:
    case 1:
        sumarNumeros(num1, num2)
    case 2:
        restarNumeros(num1, num2)
    case 3:
        multiplicarNumeros(num1, num2)
    case 4:
        dividirNumeros(num1, num2)
    case other:
        print("Opcion no valida")
