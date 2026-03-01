def calcular_media(nota1, nota2, nota3):
    """Calcula el promedio de tres notas numéricas."""
    return (nota1 + nota2 + nota3) / 3

def obtener_calificacion(media):
    """Determina la etiqueta de calificación según la nota media."""
    if media >= 9:
        return "Sobresaliente"
    elif media >= 7:
        # Aquí ya no hace falta poner 'and media < 9' porque el elif 
        # anterior ya descartó los que son 9 o más.
        return "Notable"
    elif media >= 5:
        return "Aprobado"
    else:
        return "Suspenso"

def mostrar_informe(nombre, n1, n2, n3):
    """Imprime el desglose de notas y resultado final de un alumno."""
    media = calcular_media(n1, n2, n3)
    calificacion = obtener_calificacion(media)
    
    print(f"Alumno: {nombre}")
    print(f"Nota 1: {n1}")
    print(f"Nota 2: {n2}")
    print(f"Nota 3: {n3}")
    # El :.2f sirve para mostrar solo 2 decimales si la media es periódica
    print(f"Media: {media:.2f}")
    print(calificacion)
    print("-" * 22)

def main():
    """Función principal que ejecuta el programa con los datos originales."""
    mostrar_informe("Ana García", 8, 7, 9)
    mostrar_informe("Luis Pérez", 4, 5, 3)
    mostrar_informe("Marta Gómez", 6, 7, 5)

if __name__ == "__main__":
    main()