import json
import os

from django.shortcuts import redirect, render

# solucion.py vive junto a manage.py, un nivel mas arriba que esta carpeta.
from solucion import ARCHIVO, cargar, cupos_libres, decidir, guardar


def resumen(request):
    """Muestra la lista y, si llegan datos por el formulario, decide y guarda.

    La regla de decision NO se reescribe aqui: se importa de solucion.py.
    """
    registros = cargar()

    nombre = request.GET.get("nombre", "").strip()
    edad = request.GET.get("edad", "").strip()

    if nombre and edad.isdigit():
        estado = decidir(int(edad), cupos_libres(registros))
        registros.append({"nombre": nombre, "edad": int(edad), "estado": estado})
        guardar(registros)
        # Redirige para que recargar la pagina no reenvie el formulario.
        return redirect("resumen")

    return render(request, "resumen.html", {
        "registros": registros,
        "cupos_libres": max(cupos_libres(registros), 0),
        "archivo_existe": os.path.exists(ARCHIVO),
    })
