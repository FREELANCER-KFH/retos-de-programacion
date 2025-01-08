'''
En este proyecto, desarrollo una calculadora funcional con las operaciones aritméticas básicas, 
implementando conceptos básicos como funciones, variables, operaciones
aritméticas, estructuras de control y de repetición (bucles), obtener datos del teclado y mostrar resultados en pantalla.

Este proyecto es parte de una serie de aplicaciones que estaré desarrollando en diferentes lenguajes de programación para mejorar la lógica y extender mis habilidades como programador y hacker.

Att: Kevin Feliz Henríquez.
'''

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División entre cero no permitida."
    return a / b

def calculadora():
    print("Bienvenido a la Calculadora")
    while True:
        print("\nSeleccione una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        try:
            opcion = int(input("Ingrese su opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if opcion == 5:
            print("Saliendo de la calculadora. ¡Adiós!")
            break

        if opcion not in [1, 2, 3, 4]:
            print("Opción no válida. Inténtelo de nuevo.")
            continue

        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Por favor, ingrese números válidos.")
            continue

        if opcion == 1:
            print(f"Resultado: {suma(num1, num2)}")
        elif opcion == 2:
            print(f"Resultado: {resta(num1, num2)}")
        elif opcion == 3:
            print(f"Resultado: {multiplicacion(num1, num2)}")
        elif opcion == 4:
            print(f"Resultado: {division(num1, num2)}")

if __name__ == "__main__":
    calculadora()
