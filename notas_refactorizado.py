def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def obtener_calificacion(media):
    """Nos indica la nota obtenida tras la media"""
    if media >= 9:
        return "Sobresaliente"
    elif media >= 7:
        return "Notable"
    elif media >= 5:
        return "Aprobado"
    else:
        return "Suspenso"

def mostrar_resultado(nombre, n1, n2, n3):
    """Muestra el informe final del alumno"""
    media = calcular_media(n1, n2, n3)
    calificacion = obtener_calificacion(media)
    
    print(f"Alumno: {nombre}")
    print(f"Notas: {n1}, {n2}, {n3}")
    print(f"Media: {media:.2f}")
    print(f"Resultado: {calificacion}")
    print("-" * 25)

# --- Ejecución del programa ---
mostrar_resultado("Pedro", 5, 6, 7)
mostrar_resultado("Juan", 4, 4, 3)
mostrar_resultado("Maria", 9, 10, 9)