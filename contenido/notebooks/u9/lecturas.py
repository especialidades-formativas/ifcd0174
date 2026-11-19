import numpy as np
import pandas as pd

def generar_lecturas(maquinas=200, horas=24 * 365, semilla=0):
    """Lecturas horarias simuladas de una flota durante un año."""
    rng = np.random.default_rng(semilla)
    ritmo = rng.uniform(0.5, 1.5, maquinas)      # desgaste por hora
    desgaste = rng.uniform(0, 300, maquinas)     # desde la revisión
    filas = []
    for h in range(horas):
        desgaste += ritmo
        temp = 60 + 0.01 * desgaste + rng.normal(0, 2, maquinas)
        if h >= 24 * 273:              # desde octubre, media flota
            temp[: maquinas // 2] += 3  # con sensor descalibrado
        vib = 2 + 0.004 * desgaste + rng.normal(0, 0.5, maquinas)
        kw = 40 + 0.5 * (temp - 60) + rng.normal(0, 3, maquinas)
        z = -9 + 0.006 * desgaste + 0.8 * (vib - 2)
        averia = rng.random(maquinas) < 1 / (1 + np.exp(-z))
        filas.append((np.full(maquinas, h), np.arange(maquinas),
                      temp, vib, kw, desgaste.copy(), averia))
        desgaste[averia] = 0                      # se repara
    h, m, t, v, k, d, a = map(np.concatenate, zip(*filas))
    df = pd.DataFrame({
        "fecha": pd.Timestamp("2025-01-01") + pd.to_timedelta(h, "h"),
        "maquina": m, "temperatura": t, "vibracion": v,
        "consumo_kw": k, "horas_desde_revision": d, "averia": a})
    # objetivo: ¿se averiará la máquina en las próximas 24 horas?
    df = df.sort_values(["maquina", "fecha"], ignore_index=True)
    def en_24h(s):                               # ¿avería en las 24 h
        futuro = s[::-1].rolling(24, 1).max()[::-1]   # siguientes?
        return futuro.shift(-1, fill_value=0)
    proxima = df.groupby("maquina")["averia"].transform(en_24h)
    df["averia_24h"] = proxima.astype(bool)
    return df
