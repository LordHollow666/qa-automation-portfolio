# QA Automation Portfolio

![Tests](https://github.com/TU_USUARIO/qa-automation-portfolio/actions/workflows/tests.yml/badge.svg)

Suite de pruebas automatizadas de interfaz y de API, con documentación de QA
(plan de pruebas, casos y reportes de defectos) y ejecución continua en GitHub Actions.

## Qué contiene

- **11 pruebas de UI** con Playwright sobre una tienda de demostración
  ([SauceDemo](https://www.saucedemo.com)): login, carrito, checkout y ordenamiento.
- **10 pruebas de API** con requests sobre
  [JSONPlaceholder](https://jsonplaceholder.typicode.com): lectura, creación,
  edición, borrado y filtros.
- **Patrón Page Object** para mantener los selectores en un solo lugar.
- **CI con GitHub Actions**: las pruebas corren en cada push y Pull Request, y se
  guardan el reporte HTML y la evidencia de fallos.
- **Documentación de QA** en [`docs/`](docs/).


## Tecnologías

Python · pytest · Playwright · requests · pytest-html · GitHub Actions

## Estructura

```
.
├── .github/workflows/   # Pipeline de CI
├── docs/                # Plan de pruebas, casos y defectos
├── pages/               # Page Objects (login, inventario, carrito, checkout)
├── tests/
│   ├── ui/              # Pruebas de interfaz
│   └── api/             # Pruebas de API
├── pytest.ini
└── requirements.txt
```

## Cómo ejecutarlo

```bash
git clone https://github.com/LordHollow666/qa-automation-portfolio.git
cd qa-automation-portfolio

python -m venv .venv
.venv\Scripts\Activate.ps1        # Windows PowerShell
# source .venv/bin/activate       # Mac / Linux

pip install -r requirements.txt
playwright install chromium
```

```bash
pytest                    # todas las pruebas
pytest -m ui              # solo interfaz
pytest -m api             # solo API
pytest --headed --slowmo 700    # ver el navegador trabajando
pytest --html=reports/report.html --self-contained-html   # con reporte HTML
```

## Documentación de QA

- [Plan de pruebas](docs/plan-de-pruebas.md)
- [Casos de prueba](docs/casos-de-prueba.md)
- [Reportes de defectos](docs/reportes-de-defectos.md)

## Decisiones técnicas

- **Page Object:** si un selector cambia, se corrige en un solo archivo y no en
  cada test.
- **Fixtures en `conftest.py`:** el login se prepara una vez y los tests lo reutilizan.
- **`parametrize`:** un mismo test cubre varios datos (ordenamientos, comentarios por post).
- **Marcadores `ui` / `api`:** permiten ejecutar por grupos y correr rápido solo lo necesario.
- **Timeout en todas las peticiones de API:** evita que un servidor que no responde
  deje colgada la ejecución.

## Limitaciones conocidas

- JSONPlaceholder simula las escrituras (POST, PUT, DELETE) pero no las guarda, así
  que no se verifica persistencia.
- Solo se prueba en Chromium.
- Los sitios de práctica pueden cambiar sus selectores.

## Cómo usé IA en este proyecto

Usé asistentes de IA para aprender los conceptos (Page Object, fixtures, CI) y
acelerar la escritura de código. Diseñé la estructura, revisé y ejecuté cada prueba,
escribí los casos de prueba y reporté los defectos a partir de mi propia exploración manual.

## Próximos pasos

- Pruebas con otros navegadores (Firefox, WebKit)
- Publicar el reporte HTML en GitHub Pages
- Ampliar la cobertura de casos negativos