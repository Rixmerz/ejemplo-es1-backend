# Ejemplo de referencia — Evaluación ES1

**TI3V41 · Programación Back End · Unidad 1 · INACAP**

Este es el ejemplo resuelto que acompaña a las instrucciones del ES1.
Muestra la estructura completa que se espera de tu entrega.

> **Tu problema va a ser otro.** No copies este caso: copia la estructura.

## Qué resuelve

La inscripción a un taller de robótica con 3 cupos. El programa pide nombre y
edad, decide si la persona queda inscrita, guarda el registro en `datos.json` y
lo muestra en una página web.

## Cómo correrlo

```bash
python -m venv .venv
source .venv/bin/activate        # en Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

**Comprobar los 4 resultados:**

```bash
python solucion.py --demo
```

**Agregar una inscripción:**

```bash
python solucion.py
```

**Ver la página web:**

```bash
python manage.py runserver
```

Abre <http://127.0.0.1:8000/resumen/>.

## Los 4 resultados

| # | Condición | Resultado |
| --- | --- | --- |
| 1 | `cupos < 0` | Error: cantidad de cupos inválida |
| 2 | `edad < 16` | Rechazado: es menor de 16 años |
| 3 | `cupos == 0` | Rechazado: no quedan cupos |
| 4 | resto | Aceptado |

El caso 1 va **primero**. Si lo dejas al final nunca se alcanza a revisar.

## Dónde va cada archivo

```
ejemplo-es1/
├── manage.py
├── solucion.py                    <- junto a manage.py
├── datos.json                     <- lo crea solucion.py, aquí mismo
├── plan.md, ia.md, requirements.txt
├── core/views.py
├── core/templates/resumen.html    <- Django solo lo busca aquí
└── miproyecto/settings.py, urls.py
```

## Qué criterio cubre cada archivo

| Archivo | Criterio | Puntos |
| --- | --- | --- |
| `solucion.py` — variables y `int()` | 1.1.1 | 6 |
| `solucion.py` — `if`/`elif` y operadores | 1.1.2 | 6 |
| `solucion.py` + `requirements.txt` — `tabulate` | 1.1.3 | 6 |
| `core/` + `miproyecto/` + `ia.md` | 1.1.4 | 12 |
| `plan.md` | requisito, sin puntaje | — |

## Sin base de datos

Esta versión guarda en un archivo JSON. No hay modelos ni migraciones: las
bases de datos se ven en la Unidad 2.
