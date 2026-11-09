# Carencias — miu-semilla-latente-mt91l2pm-2

Lo que NO se sabe va aquí, nunca en la semilla. Cada ítem lleva
dónde se buscó (o que no se buscó) y fecha.

- **NO SÉ — si existe otro worker `/miu/global` fuera de los tres
  encontrados.** Se buscaron tres rutas locales y el repo
  `miu-agents` (plan §3, 2026-11-09). No se hizo una búsqueda
  exhaustiva por todo el workspace ni por todos los repos.
- **NO SÉ — si alguno de los tres workers llegó a desplegarse.**
  No hay URL de despliegue ni log en los archivos leídos
  (2026-11-09). La medición es del código, no del despliegue.
- **NO SÉ — el tamaño en bytes de (iii) `miu-agents/worker.js`.**
  Se leyó por GitHub (descarga SHA `c162dfb7…`, 2026-11-09); el
  tamaño no se midió en local.
- **NO SÉ — a qué apunta el campo `drive` de (ii) y (iii).** El
  valor nunca se abrió ni se reproduce aquí; solo se registra su
  huella (`b3a56d7a…`, la del racimo de agosto). Abrirlo es otra
  tarea, no esta medición.
- **NO SÉ — si el `scheduled()` de (i) corrió alguna vez.** Su
  cuerpo es solo un comentario (poda KV TTL 10/ciclo): no hay
  código que pode ni log de ejecución (2026-11-09).
- **NO SÉ — si alguien leyó alguna vez el `latido` de (ii).** Es
  la hora del reloj, no una medición; nadie la consume en los
  archivos leídos (2026-11-09).
- **NO SÉ — qué era el PAT real detrás del marcador redactado en
  el campo `github` de (i).** El archivo mismo lo redacta ("PAT
  seguro en Properties..."); buscarlo queda fuera de esta
  medición y fuera de esta semilla.
- **NO SÉ — qué responde la ruta `/franbot` de (i) en vivo.**
  Es otro JSON fijo en el mismo archivo; esta semilla mide solo
  `/miu/global` (2026-11-09).
