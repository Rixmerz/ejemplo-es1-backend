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
cp .env.example .env             # en Windows: copy .env.example .env
```

**El paso del `.env` no es opcional.** Si lo saltas, Django corta con
`UndefinedValueError: SECRET_KEY not found`. Las claves no se escriben dentro
del código: se leen del `.env`, que está en `.gitignore` y no se sube a GitHub.
El `.env.example` sí se sube, para que quien clone el repo sepa qué variables
necesita.

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

Abre <http://127.0.0.1:8000/resumen/>. Desde ahí puedes inscribir con el
formulario, sin volver a la consola.

## La vista NO reescribe la regla: la importa

Esto es lo que pide el Paso 2 de la Fase 3. En `core/views.py`:

```python
from solucion import ARCHIVO, CUPOS, cargar, decidir, guardar
```

La regla de decisión vive en un solo lugar, `solucion.py`. Si la copiaras
dentro de la vista tendrías la misma lógica en dos archivos, y al corregir un
caso tendrías que acordarte de arreglarlo dos veces.

## Los 4 resultados

| # | Condición | Resultado |
| --- | --- | --- |
| 1 | `cupos < 0` | Error: cantidad de cupos inválida |
| 2 | `edad < 16` | Rechazado: es menor de 16 años |
| 3 | `cupos == 0` | Rechazado: no quedan cupos |
| 4 | resto | Aceptado |

El caso 1 va **primero**. Si lo dejas al final nunca se alcanza a revisar.

**Un rechazo no consume cupo.** `cupos_libres()` cuenta solo los registros con
estado `Aceptado`. Si contaras todos los registros, un menor de edad rechazado
te dejaría sin cupos — es un error fácil de cometer y difícil de notar.

## Dónde va cada archivo

```
ejemplo-es1/
├── manage.py
├── solucion.py                    <- junto a manage.py
├── datos.json                     <- lo crea solucion.py, aquí mismo
├── plan.md, ia.md, requirements.txt
├── .env                           <- tus claves, NO se sube
├── .env.example                   <- la plantilla, sí se sube
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

## Las claves van en `.env`, no en el código

`settings.py` lee `SECRET_KEY` y `DEBUG` con `python-decouple`:

```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
```

El `.env` está en `.gitignore` y no se sube. El `.env.example` sí se sube: es
la plantilla que dice qué variables hacen falta. Es la seguridad mínima de
cualquier proyecto Django.

## Sobre los paquetes externos

`requirements.txt` trae tres:

| Paquete | Para qué | ¿Se evalúa en 1.1.3? |
| --- | --- | --- |
| `tabulate` | Mostrar el resumen como tabla en consola | **Sí, este es el del criterio** |
| `django` | La página web | No, es del criterio 1.1.4 |
| `python-decouple` | Leer las claves desde `.env` | No, es buena práctica |

`json` **no** cuenta como paquete externo: viene incluido con Python y no se
instala con pip.

## Sin base de datos

Esta versión guarda en un archivo JSON. No hay modelos ni migraciones: las
bases de datos se ven en la Unidad 2.
