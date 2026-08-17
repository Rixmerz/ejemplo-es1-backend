# Plan — Inscripcion al taller de robotica

## Apartado de negocio

**Problema.** El taller de robotica tiene 3 cupos y las inscripciones se toman
en un cuaderno. Se anota gente que no cumple la edad minima, se pasan de cupo,
y nadie sabe cuantos van hasta que alguien cuenta a mano.

**Solucion.** Un programa que pide nombre y edad, decide en el momento si la
persona queda inscrita, y deja el registro escrito para poder revisarlo despues.

**Alcance.** Entra: pedir los datos, decidir, avisar el motivo, guardar y
mostrar la lista. No entra: editar registros, borrar, ni cuentas de usuario.

**MoSCoW.**

| Prioridad | Funcion |
| --- | --- |
| Must | Pedir nombre y edad |
| Must | Decidir con los 4 resultados |
| Must | Guardar en datos.json |
| Must | Mostrar la lista en una pagina web |
| Should | Corregir un registro mal ingresado |
| Could | Exportar la lista a Excel |
| Won't | Cuentas de usuario con contrasena |

**MVP** = los cuatro Must. Es lo unico que esta programado.

## Apartado tecnico

**Datos de entrada.** `nombre` (texto), `edad` (entero, convertida con `int()`).
`cupos` se calcula como 3 menos los ya inscritos.

**Regla de decision.** Los 4 resultados, en este orden:

| # | Condicion | Resultado |
| --- | --- | --- |
| 1 | cupos < 0 | Error: cantidad de cupos invalida |
| 2 | edad < 16 | Rechazado: es menor de 16 anios |
| 3 | cupos == 0 | Rechazado: no quedan cupos |
| 4 | resto | Aceptado |

El caso 1 va primero. Si se deja al final nunca se alcanza a revisar.

**Paquete externo.** `tabulate`, para mostrar el resumen en consola como tabla
alineada. Se instala con pip. `json` no cuenta: viene con Python.

**Pantalla Django.** `/resumen/` muestra la tabla de inscritos. Si todavia no
hay ninguno, muestra un mensaje en vez de una tabla vacia.
