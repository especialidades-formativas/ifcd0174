# IFCD0174 · Machine Learning e Inteligencia Artificial · Recursos del libro

Material complementario del libro *Machine Learning e Inteligencia Artificial*, que desarrolla la
especialidad formativa IFCD0174. Cada código QR del libro lleva a uno de estos recursos:

| Tipo | Qué es |
|---|---|
| **Ejecuta** | Notebook de Python que se ejecuta en el navegador (JupyterLite), sin instalar nada |
| **Explora** | Herramienta interactiva para experimentar con un concepto |
| **Compruébalo** | Test de autoevaluación con explicación de cada respuesta |
| **Actualizado** | Página que se mantiene al día (normativa, versiones, cambios) |

Web publicada: <https://especialidades-formativas.github.io/ifcd0174/>

Este repositorio no es un sitio oficial del SEPE ni de FUNDAE. «Especialidad formativa» es el
nombre genérico del catálogo público en el que se basa el programa del libro.

## Cómo funciona

`recursos.csv` es la **fuente única**: cada fila es un QR del libro (código, tipo, título y destino).

```bash
pip install -r requirements.txt
python herramientas/construir.py                         # construye la web en site/
python herramientas/construir.py --sin-lab --libro RUTA  # además actualiza el bloque de recursos de libro.tex
```

El script genera:

- `site/<código>/`: redirección estable de cada QR. El QR impreso no cambia nunca; si un recurso
  se mueve, solo se cambia su destino en `recursos.csv`.
- `site/lab/`: JupyterLite con los notebooks de `contenido/notebooks/`.
- `site/recursos/`: páginas HTML de `contenido/recursos/`.

GitHub Actions (`.github/workflows/pages.yml`) ejecuta todos los notebooks, construye la web y la
publica en GitHub Pages en cada cambio y el día 1 de cada mes, para detectar a tiempo si una
actualización rompe algún ejemplo. Las versiones de las librerías están fijadas en
`requirements.txt`.

## Privacidad

Ninguna página pide registro, usa cookies ni envía datos de quien la visita.
