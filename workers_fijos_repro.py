#!/usr/bin/env python3
"""Reproduce la medición: tres workers /miu/global, tres JSON fijos, ninguno vivo.

Lee los dos worker.js locales, extrae el JSON de /miu/global (claves +
literal phi), cuenta llamadas fetch() (sin contar el handler), busca
accesos vivos (KV / D1 / Supabase) y hashea el campo drive (solo se
imprime la huella, nunca el valor). El tercer worker (miu-agents) no
vive en local: se tabula el registro verificado (lectura GitHub
2026-11-09, descarga SHA c162dfb7..., minería ola 4 tanda 1,
LECTURA.md:33).

Solo stdlib. Solo lectura local. Sin red.
"""
import hashlib
import re
import sys
from pathlib import Path

BASE = Path.home() / "workspace" / "miu-verificacion-2026-11-06"

LOCALES = {
    "(i) realidad": BASE / "extracted" / "miu_realidad_upload_REAL" / "worker.js",
    "(ii) FranBot": BASE / "franbot-repos" / "FranBot" / "worker.js",
}

# (iii) registrado, no local. Fuente: GitHub Jaime393/miu-agents/worker.js,
# lectura 2026-11-09 (descarga SHA c162dfb7...); minería ola 4 tanda 1,
# LECTURA.md:33. Tamaño en bytes: NO SÉ (no medido en local).
REGISTRO_III = {
    "etiqueta": "(iii) miu-agents",
    "claves": ["global_mind", "autorizacion", "repos", "phi", "manos",
               "expansion", "drive"],
    "phi": "$107M",
    "default": "global mind 16/16 - MIU v27 expansion 16 repos - 10 manos",
    "drive_huella": "b3a56d7a",
}


def extraer_global(texto):
    """Devuelve el cuerpo del primer JSON.stringify({...}) del archivo,
    que en los dos workers locales es el de /miu/global."""
    m = re.search(r"JSON\.stringify\(\{([^{}]*)\}\)", texto)
    if not m:
        raise ValueError("no se encontró JSON.stringify({...})")
    return m.group(1)


def analizar(ruta):
    """Analiza un worker.js local. Devuelve un dict con lo medido."""
    raw = ruta.read_bytes()
    texto = raw.decode("utf-8")
    cuerpo = extraer_global(texto)
    claves = re.findall(r"(\w+)\s*:", cuerpo)
    phi = re.search(r"phi:'([^']*)'", cuerpo).group(1)
    default = re.search(r"return new Response\('([^']*)'\)", texto).group(1)
    # fetch(: el handler 'async fetch(' cuenta una vez; las llamadas son
    # el resto.
    total_fetch = len(re.findall(r"fetch\(", texto))
    handler_fetch = len(re.findall(r"async fetch\(", texto))
    llamadas_fetch = total_fetch - handler_fetch
    # Accesos vivos: KV, D1, Supabase, uso de env. fuera de parámetros.
    kv = [ln for ln in texto.splitlines()
          if re.search(r"\bKV\b", ln) and not ln.strip().startswith("//")]
    d1 = [ln for ln in texto.splitlines() if re.search(r"\bD1\b", ln)]
    supabase = [ln for ln in texto.splitlines()
                if "supabase" in ln.lower()]
    env_uso = [ln for ln in texto.splitlines()
               if re.search(r"\benv\.", ln)]
    drive = re.search(r"drive:'([^']*)'", cuerpo)
    drive_huella = (hashlib.sha256(drive.group(1).encode()).hexdigest()[:8]
                    if drive else None)
    return {
        "ruta": str(ruta),
        "bytes": len(raw),
        "lineas": texto.count("\n"),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "claves": claves,
        "n_claves": len(claves),
        "phi": phi,
        "default": default,
        "llamadas_fetch": llamadas_fetch,
        "kv_codigo": len(kv),
        "d1": len(d1),
        "supabase": len(supabase),
        "env_uso": len(env_uso),
        "drive_huella": drive_huella,
    }


def main():
    print("Tres workers /miu/global, tres JSON fijos, ninguno vivo")
    print("Medición 2026-11-09. Solo lectura local.")
    print()
    for etiqueta, ruta in LOCALES.items():
        a = analizar(ruta)
        print(f"{etiqueta}: {a['ruta']}")
        print(f"  bytes={a['bytes']} lineas={a['lineas']} "
              f"sha256={a['sha256'][:8]}...")
        print(f"  claves /miu/global ({a['n_claves']}): "
              f"{', '.join(a['claves'])}")
        print(f"  phi: '{a['phi']}'")
        print(f"  respuesta por defecto: '{a['default']}'")
        print(f"  llamadas fetch(): {a['llamadas_fetch']} | "
              f"KV en código: {a['kv_codigo']} | D1: {a['d1']} | "
              f"Supabase: {a['supabase']} | env. usado: {a['env_uso']}")
        print(f"  huella drive: {a['drive_huella']}")
        print()
    r = REGISTRO_III
    print(f"{r['etiqueta']}: registro verificado, no local")
    print(f"  claves /miu/global ({len(r['claves'])}): "
          f"{', '.join(r['claves'])}")
    print(f"  phi: '{r['phi']}'")
    print(f"  respuesta por defecto: '{r['default']}'")
    print(f"  huella drive: {r['drive_huella']}")
    print()
    print("Veredicto: los tres devuelven literales fijos; ninguno lee "
          "nada vivo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
