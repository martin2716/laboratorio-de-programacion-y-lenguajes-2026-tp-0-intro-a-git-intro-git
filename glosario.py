"""
IF009 - Laboratorio de Programación y Lenguajes (UNTDF)
TP 0: Git & GitHub Flow
Script base para el Glosario Colaborativo
"""


def mostrar_bienvenida():
    print("=" * 40)
    print("  GLOSARIO COLABORATIVO - LPyL")
    print("=" * 40)
    print("Semanas 1-2: Introducción a Git, HTML, CSS y Python")
    print("-" * 40)


def glosario_inicial():
    """
    Diccionario con términos base.
    Los alumnos deben agregar nuevas funciones para extender este glosario.
    """
    terminos = {
        "HTML": "Lenguaje de marcado para la creación de páginas web.",
        "CSS": "Lenguaje de hojas de estilo para describir la presentación de un documento HTML.",
        "Python": "Lenguaje de programación de alto nivel, interpretado y multiparadigma.",
        "Git": "Sistema de control de versiones distribuido, diseñado para manejar proyectos pequeños a muy grandes con rapidez y eficiencia.",
        "GitHub": "Plataforma de alojamiento para proyectos de desarrollo de software que utiliza Git.",
    }

    for termino, definicion in terminos.items():
        print(f"-> {termino}: {definicion}")


# --- TAREA PARA EL ALUMNO ---
# Instrucciones:
# 1. Crea una rama 'feature-tu-termino'
# 2. Crea una función nueva siguiendo el ejemplo de abajo
# 3. Llámala dentro del bloque 'if __name__ == "__main__":'


def definicion_django():
    """
    Ejemplo implementado: definición para el término 'Django'.
    El alumno debe renombrar/editar esta función para su propio término.
    """
    termino = "Django"  # Reemplazar con el término asignado o elegido
    definicion = (
        "Framework web de alto nivel para desarrollar aplicaciones con Python "
        "siguiendo el patrón MVT (Model-View-Template)."
    )
    print(f"[NUEVO] {termino}: {definicion}")


if __name__ == "__main__":
    mostrar_bienvenida()
    glosario_inicial()

    # El alumno debe agregar la llamada a su función aquí:
    definicion_django()
