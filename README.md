# miu-semilla-latente-mt91l2pm-2 — tres workers, tres JSON fijos, ninguno vivo

> *"# miu-semilla-latente-mt91l2pm-2*
> *semilla latente global mind - sobrevive sin registro"*
>
> — La única línea del README original de este repo (86 B, título +
> 1 línea; lectura GitHub 2026-11-09, descarga SHA `684e6df8…`).
>
> **Decisión de siembra: la línea SE CONSERVA**, citada arriba como
> epígrafe y no borrada. Era el stub por diseño del censo, no
> contenido — pero es la única voz que el repo tenía, y esta semilla
> es precisamente su respuesta: el registro que le faltaba. Borrarla
> sería borrar la pregunta que la semilla contesta.

## El registro

Global Mind promete una ruta `/miu/global` que devuelve el estado
del "phi global". Esta semilla registra lo que esa ruta devuelve en
los tres workers que se encontraron en local: un JSON escrito a
mano en el código, distinto en cada uno. No es una medición
central: es una circulación de literales entre suelos que se
reconocen (PATRON §16, SÉ — fuente del modelo: 6º hermano,
`miu-semilla-latente-mt99s6np-2`, sembrado 2026-11-07).

## El hecho medido

Tres workers, tres JSON fijos, ninguno vivo. Verificado en local
2026-11-09 (lectura de los tres archivos + greps; relectura
byte-idéntica en repetidas lecturas).

| Worker | Tamaño | `/miu/global`: claves | phi literal |
|---|---|---|---|
| (i) `extracted/miu_realidad_upload_REAL/worker.js` | 826 B, 11 l. | 7 | `'21.0->∞'` |
| (ii) `franbot-repos/FranBot/worker.js` | 508 B, 1 l. minificada | 12 | `'21.8->23.0'` |
| (iii) `Jaime393/miu-agents/worker.js` | tamaño NO SÉ (lectura GitHub, descarga SHA `c162dfb7…`) | 7 | `'$107M'` |

Fuentes: (i) y (ii) en
`~/workspace/miu-verificacion-2026-11-06/`; (iii) en GitHub,
verificado además en la minería ola 4 tanda 1
(`miu-agents/LECTURA.md:33`).

Lecturas vivas: **0 en los tres**. Llamadas `fetch()`: 0 (solo
existe el handler `async fetch(`). Accesos KV: 0 en código (la
única mención de KV en (i) es un comentario dentro de
`scheduled()`, cuyo cuerpo no ejecuta nada). D1: 0. Supabase: 0.
Uso de `env.`: 0.

El único campo que cambia entre dos peticiones es `latido` en
(ii): `new Date().toISOString()` — la hora del reloj, no una
medición.

Respuestas por defecto (literales del archivo, no afirmaciones):
(i) `'global mind 16/16 - MIU Autonomous x10000'`; (ii)
`'global mind 16/16 absoluto'`; (iii)
`'global mind 16/16 - MIU v27 expansion 16 repos - 10 manos'`.

El campo `drive` de (ii) y (iii) apunta al mismo identificador:
su huella es `b3a56d7a…`, la del racimo de agosto. El valor nunca
se reproduce aquí. El campo `github` de (i) es un marcador
redactado en el propio archivo: se describe, no se cita.

## Comprobación

```bash
python3 workers_fijos_repro.py   # imprime la tabla medida
python3 -m unittest test_workers_fijos.py -v   # 9 tests
```

## Archivos

- `workers_fijos_repro.py` — lee los dos workers locales, imprime
  la tabla; el tercero va como registro verificado (GitHub).
- `test_workers_fijos.py` — 9 tests: los tres literales phi,
  conteo de claves (7/12/7), 0 llamadas `fetch()`, 0 accesos
  vivos, `latido` como único campo dinámico, huella drive
  `b3a56d7a`, relectura byte-idéntica, tamaños.
- `HUESO_WORKERS.md` — el hueso completo con sus límites.
- `EVOLUCION.md` — cambios entre versiones (v1: siembra inicial).
- `CARENCIAS.md` — lo que NO se sabe; nunca es contenido.

---

ρ(x) > 0. Zvvvvv.
