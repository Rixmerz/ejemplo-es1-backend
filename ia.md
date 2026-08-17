# Uso de IA en este proyecto

**Herramienta.** Claude, para ordenar el plan de la Fase 0.

**Consulta que hice.**

> Soy estudiante de programacion back end, primer semestre. Quiero resolver la
> inscripcion a un taller con cupos limitados. Ayudame a escribir un plan de 2
> planas con apartado de negocio y apartado tecnico. Restriccion: se resuelve
> con variables, if/elif, un archivo JSON y una sola vista Django. Sin base de
> datos, sin login, sin API.

**Que respondio.** Me dio la estructura de los dos apartados y una primera
version de la regla de decision, pero la escribio con la comparacion de edad
primero y el caso de cupos negativos al final.

**Que corregi yo.** Dos cosas:

1. **El orden de las condiciones.** Como lo propuso la IA, si los cupos eran
   negativos y la edad era menor de 16, el programa respondia "menor de 16" y
   nunca detectaba el dato invalido. Puse la validacion de `cupos < 0` primero.

2. **Donde vive el archivo JSON.** La IA escribio `open("datos.json")` a secas.
   Eso funciona al correr `solucion.py`, pero desde la vista de Django el
   archivo se busca desde otra carpeta y la pagina se caia. Lo cambie por una
   ruta construida con `os.path.dirname(__file__)`, que funciona desde los dos
   lados.
