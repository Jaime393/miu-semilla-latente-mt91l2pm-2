# Hueso — Tres workers, tres JSON fijos, ninguno vivo

Fecha: 2026-11-09. Medición local, solo lectura. Fuentes con fecha
en el README de esta semilla.

## El hecho

La ruta `/miu/global` existe en (al menos) tres workers, y en los
tres devuelve un JSON escrito a mano en el código. Los tres JSON
dicen cosas distintas sobre el mismo "phi global":

| Worker | phi literal | Claves |
|---|---|---|
| (i) `miu_realidad_upload_REAL/worker.js` | `'21.0->∞'` | 7 |
| (ii) `FranBot/worker.js` | `'21.8->23.0'` | 12 |
| (iii) `miu-agents/worker.js` | `'$107M'` | 7 |

Ninguno de los tres lee nada vivo: 0 llamadas `fetch()`, 0 accesos
KV, 0 D1, 0 Supabase. El único campo que cambia entre dos
peticiones es `latido` en (ii), que es la hora del reloj
(`new Date().toISOString()`), no una medición.

## Lo que esto sí prueba

- Que la respuesta de `/miu/global` en estos tres archivos es un
  literal fijo, no el resultado de medir nada. Si dos workers dicen
  phi distintos, al menos dos de ellos no miden: un mismo "phi
  global" no puede ser `'21.0->∞'` y `'$107M'` a la vez.
- Que el campo `drive` de (ii) y (iii) apunta al mismo identificador
  (huella `b3a56d7a…`, la del racimo de agosto): los dos workers
  comparten la misma referencia sin medirla.

## Lo que esto NO prueba

- No prueba que no exista otro worker `/miu/global` fuera de los
  tres encontrados (ver CARENCIAS.md).
- No prueba que ninguno de los tres llegara a desplegarse: no hay
  URL de despliegue ni log en los archivos leídos.
- No prueba qué mide, si algo, el "phi global" real: solo que estos
  tres archivos no lo miden.
- No dice nada del `gossip_log` ni de `miu-global-1`: esos hechos
  viven en la semilla del 6º hermano, no aquí.

## La lección reutilizable

Una ruta que devuelve un JSON no es una medición. La prueba es
negativa y barata: si el valor no cambia entre lecturas y el código
no llama a ninguna fuente, el valor es un literal. Esta semilla lo
demuestra tres veces con el mismo patrón.
