"""
Este programa sirve para calcular la nota final de los alumnos 
a través del cálculo de su nota media.

Escrito por Francisco Ródenas Micol
01/03/2026
"""
def calcular_media(nota1, nota2, nota3):
    """Calcula la media aritmética de las tres notas"""
    return (nota1 + nota2 + nota3) / 3

def obtener_calificacion(media):
    """Se calcula la calificación final"""
    if media >= 9:
        return "Sobresaliente"
    elif media >= 7:
        return "Notable"
    elif media >= 5:
        return "Aprobado"
    else:
        return "Suspenso"

def mostrar_informe(nombre, n1, n2, n3):
    """Muestra las notas, nota media y nota final de cada alumno"""
    media = calcular_media(n1, n2, n3)
    calificacion = obtener_calificacion(media)
    
    print(f"Alumno: {nombre}")
    print(f"Nota 1: {n1}")
    print(f"Nota 2: {n2}")
    print(f"Nota 3: {n3}")
    
    print(f"Media: {media:.2f}") #Con "f" limitamos a 2 decimales
    print(calificacion)
    print("-" * 22)

def main():
    """MAIN"""
    mostrar_informe("Ana García", 8, 7, 9)
    mostrar_informe("Luis Pérez", 4, 5, 3)
    mostrar_informe("Marta Gómez", 6, 7, 5)

if __name__ == "__main__":
    main()