"""Taller de robotica: decide si una persona queda inscrita.

Este es el ejemplo de referencia del ES1. Tu problema sera otro,
pero la estructura es exactamente esta.
"""

import json
import os

from tabulate import tabulate

ARCHIVO = os.path.join(os.path.dirname(__file__), "datos.json")
CUPOS = 3


def decidir(edad, cupos):
    """Devuelve uno de los 4 resultados posibles. El dato invalido va primero."""
    if cupos < 0:
        return "Error: cantidad de cupos invalida"
    elif edad < 16:
        return "Rechazado: es menor de 16 anios"
    elif cupos == 0:
        return "Rechazado: no quedan cupos"
    else:
        return "Aceptado"


def cupos_libres(registros):
    """Solo los aceptados ocupan cupo. Un rechazo no consume nada."""
    aceptados = [r for r in registros if r["estado"] == "Aceptado"]
    return CUPOS - len(aceptados)


def cargar():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, encoding="utf-8") as f:
            return json.load(f)
    return []


def guardar(registros):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(registros, f, indent=2, ensure_ascii=False)


def main():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))

    registros = cargar()
    estado = decidir(edad, cupos_libres(registros))
    print(estado)

    registros.append({"nombre": nombre, "edad": edad, "estado": estado})
    guardar(registros)
    print()
    print(tabulate(registros, headers="keys"))


def demo():
    """Comprueba que los 4 resultados son distintos entre si."""
    casos = [(17, 3), (14, 3), (20, 0), (20, -1)]
    salidas = [decidir(e, c) for e, c in casos]
    for (e, c), s in zip(casos, salidas):
        print(f"edad={e} cupos={c} -> {s}")
    assert len(set(salidas)) == 4, "los 4 casos deben dar mensajes distintos"
    print("\nOK: los 4 resultados son distintos.")


if __name__ == "__main__":
    import sys
    demo() if "--demo" in sys.argv else main()
