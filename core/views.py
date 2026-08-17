import json
import os

from django.shortcuts import render

ARCHIVO = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "datos.json")


def resumen(request):
    registros = []
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, encoding="utf-8") as f:
            registros = json.load(f)
    return render(request, "resumen.html", {"registros": registros})
