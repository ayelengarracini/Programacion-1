# Resolución de problemas y algoritmos
# Desafíos 3 y 4
# Ejecuta este archivo directamente en Visual Studio Code.

# ============================================================
# DESAFÍO 3: SUMA DE LOS PRIMEROS N NÚMEROS NATURALES
# ============================================================

def sumar_naturales(n):
    """Devuelve la suma de los números naturales desde 1 hasta n."""
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        return "Error: n debe ser un entero positivo."

    suma = 0
    for numero in range(1, n + 1):
        suma += numero

    return suma


# Ejemplo de uso del desafío 3
n = 5
resultado = sumar_naturales(n)

print("DESAFÍO 3: SUMA DE LOS PRIMEROS N NÚMEROS NATURALES")
print("Número ingresado:", n)
print("La suma de los primeros", n, "números es:", resultado)


# ============================================================
# DESAFÍO 4: CONTAR LOS NÚMEROS PARES DE UNA LISTA
# ============================================================

def contar_pares(lista):
    """Devuelve cuántos números pares contiene la lista."""
    cantidad_pares = 0

    for numero in lista:
        if numero % 2 == 0:
            cantidad_pares += 1

    return cantidad_pares


# Ejemplo de uso del desafío 4
numeros = [4, 7, 2, 9, 10, 13, 8, 5]
resultado_pares = contar_pares(numeros)

print("\nDESAFÍO 4: CANTIDAD DE NÚMEROS PARES")
print("Lista de números:", numeros)
print("Cantidad de números pares:", resultado_pares)


# ============================================================
# PRUEBAS ADICIONALES PARA EXPERIMENTAR
# ============================================================

print("\nPRUEBAS ADICIONALES")
print("Suma de los primeros 10 números:", sumar_naturales(10))
print("Pares en [1, 3, 5, 7]:", contar_pares([1, 3, 5, 7]))
print("Pares en una lista vacía:", contar_pares([]))
