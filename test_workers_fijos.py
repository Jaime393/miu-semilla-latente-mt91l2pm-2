#!/usr/bin/env python3
"""Tests de la medición: tres workers /miu/global, tres JSON fijos.

Solo stdlib. Solo lectura local. Sin red. Sin valores de claves:
el campo drive solo se comprueba por su huella (primeros 8 hex
del sha256), nunca se imprime ni se compara el valor.
"""
import hashlib
import unittest
from pathlib import Path

import workers_fijos_repro as repro


class TestWorkersFijos(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = {k: repro.analizar(p) for k, p in repro.LOCALES.items()}

    def test_phi_literales(self):
        self.assertEqual(self.a["(i) realidad"]["phi"], "21.0->\u221e")
        self.assertEqual(self.a["(ii) FranBot"]["phi"], "21.8->23.0")
        self.assertEqual(repro.REGISTRO_III["phi"], "$107M")

    def test_n_claves(self):
        self.assertEqual(self.a["(i) realidad"]["n_claves"], 7)
        self.assertEqual(self.a["(ii) FranBot"]["n_claves"], 12)
        self.assertEqual(len(repro.REGISTRO_III["claves"]), 7)

    def test_claves_exactas(self):
        self.assertEqual(
            self.a["(i) realidad"]["claves"],
            ["global_mind", "autorizacion", "github", "vive", "phi",
             "panteon", "biblia"])
        self.assertEqual(
            self.a["(ii) FranBot"]["claves"],
            ["vive", "phi", "esporas", "genoma", "manos", "autorizacion",
             "github", "drive", "funding", "biblia", "panteon", "latido"])
        self.assertEqual(
            repro.REGISTRO_III["claves"],
            ["global_mind", "autorizacion", "repos", "phi", "manos",
             "expansion", "drive"])

    def test_cero_llamadas_fetch(self):
        # Solo el handler 'async fetch(' existe; llamadas: 0.
        for a in self.a.values():
            self.assertEqual(a["llamadas_fetch"], 0)

    def test_cero_accesos_vivos(self):
        for a in self.a.values():
            self.assertEqual(a["kv_codigo"], 0)
            self.assertEqual(a["d1"], 0)
            self.assertEqual(a["supabase"], 0)
            self.assertEqual(a["env_uso"], 0)

    def test_unico_campo_dinamico_es_latido(self):
        # En (ii) el único campo que no es literal es latido (hora del
        # reloj). Se comprueba que existe y que el resto de claves son
        # las ya listadas: ningún otro campo usa Date ni Math.random.
        texto = Path(repro.LOCALES["(ii) FranBot"]).read_text()
        self.assertIn("new Date().toISOString()", texto)
        self.assertEqual(texto.count("new Date()"), 1)
        self.assertNotIn("Math.random", texto)

    def test_huella_drive(self):
        # Misma huella en los dos workers locales que llevan el campo.
        self.assertEqual(self.a["(i) realidad"]["drive_huella"], None)
        self.assertEqual(self.a["(ii) FranBot"]["drive_huella"], "b3a56d7a")
        self.assertEqual(repro.REGISTRO_III["drive_huella"], "b3a56d7a")

    def test_relectura_byte_identica(self):
        for ruta in repro.LOCALES.values():
            h1 = hashlib.sha256(ruta.read_bytes()).hexdigest()
            h2 = hashlib.sha256(ruta.read_bytes()).hexdigest()
            self.assertEqual(h1, h2)

    def test_tamanos(self):
        self.assertEqual(self.a["(i) realidad"]["bytes"], 826)
        self.assertEqual(self.a["(i) realidad"]["lineas"], 11)
        self.assertEqual(self.a["(ii) FranBot"]["bytes"], 508)
        self.assertEqual(self.a["(ii) FranBot"]["lineas"], 0)


if __name__ == "__main__":
    unittest.main()
