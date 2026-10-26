# Plan de pruebas: SauceDemo

## 1. Objetivo
Verificar que las funciones principales de la tienda de demostración
(login, catálogo, carrito y checkout) funcionan correctamente, y que la API
pública de JSONPlaceholder responde según lo esperado.

## 2. Alcance

**Dentro del alcance**
- Login: caso exitoso y casos de rechazo
- Catálogo: ordenamiento por nombre y precio
- Carrito: agregar productos y ver su contenido
- Checkout: compra completa y validación de campos obligatorios
- API de posts y comentarios: lectura, creación, edición y borrado

**Fuera del alcance**
- Pruebas de rendimiento y carga
- Pruebas de seguridad
- Compatibilidad con navegadores distintos de Chromium
- Pruebas en dispositivos móviles

## 3. Estrategia

| Nivel | Herramienta | Qué cubre |

| UI automatizada | Playwright + pytest | Flujos críticos del usuario |
| API automatizada | requests + pytest | Contratos y códigos de respuesta |
| Exploratoria manual | Navegador | Defectos que la automatización no detecta |

Se automatizan los flujos que se repiten en cada cambio (regresión).
Se prueba manualmente lo que cambia mucho o requiere criterio humano.

## 4. Entorno
- Sistema: Windows 11, Python 3.14, Chromium (Playwright)
- Aplicación bajo prueba: https://www.saucedemo.com
- API bajo prueba: https://jsonplaceholder.typicode.com
- CI: GitHub Actions (ubuntu-latest)

## 5. Criterios
- **Entrada:** entorno accesible y datos de prueba disponibles.
- **Salida:** el 100 % de los casos críticos pasa y no hay defectos
  abiertos de severidad alta.

## 6. Riesgos
- Los sitios de práctica pueden cambiar selectores o estar caídos.
- JSONPlaceholder simula las escrituras: no se puede verificar persistencia.
- Dependencia de internet para ejecutar las pruebas.

## 7. Entregables
- Código de pruebas automatizadas
- Casos de prueba documentados
- Reportes de defectos
- Resultado de ejecución en GitHub Actions