# menu.py

def mostrar_menu():
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

def operaciones():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la operación: ")

        if opcion == '1':
            a, b = map(float, input("Ingrese dos números separados por un espacio: ").split())
            print(f"Resultado: {a + b}")
        elif opcion == '2':
            a, b = map(float, input("Ingrese dos números separados por un espacio: ").split())
            print(f"Resultado: {a - b}")
        elif opcion == '3':
            a, b = map(float, input("Ingrese dos números separados por un espacio: ").split())
            print(f"Resultado: {a * b}")
        elif opcion == '4':
            a, b = map(float, input("Ingrese dos números separados por un espacio: ").split())
            if b != 0:
                print(f"Resultado: {a / b}")
            else:
                print("Error: División por cero.")
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    operaciones()
