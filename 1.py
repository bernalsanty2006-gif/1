num1_str = input("Ingresa el primer número: ")

num2_str = input("Ingresa el segundo número: ")

try:
    num1 = float(num1_str)
    num2 = float(num2_str)
except ValueError:
    print("Error: Ingresa solo números válidos.")
else:
    suma = num1 + num2

    print(f"La suma de {num1} y {num2} es: {suma}")