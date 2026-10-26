# Casos de prueba

| Campo | Detalle |
| ID | TC-001 |
| Título | Login exitoso con usuario estándar |
| Prioridad | Alta |
| Tipo | Funcional / Humo |
| Precondiciones | El usuario `standard_user` existe y está activo |
| Datos | Usuario: `standard_user` · Contraseña: `secret_sauce` |
| Pasos | 1. Abrir https://www.saucedemo.com<br>2. Escribir el usuario y la contraseña<br>3. Pulsar **Login** |
| Resultado esperado | Se muestra la página de productos y el título "Products" |
| Automatizado en | `tests/ui/test_login.py::test_login_exitoso` |

| Campo | Detalle |

| ID | TC-002 |
| Título | Login rechazado para usuario bloqueado |
| Prioridad | Alta |
| Tipo | Funcional / Negativa |
| Precondiciones | El usuario `locked_out_user` está bloqueado |
| Datos | Usuario: `locked_out_user` · Contraseña: `secret_sauce` |
| Pasos | 1. Abrir https://www.saucedemo.com<br>2. Escribir el usuario y la contraseña<br>3. Pulsar **Login** |
| Resultado esperado | No se inicia sesión y aparece un mensaje que indica que el usuario está bloqueado |
| Automatizado en | `tests/ui/test_login.py::test_login_usuario_bloqueado` |

| Campo | Detalle |
| ID | TC-003 |
| Título | Compra completa de un producto |
| Prioridad | Alta |
| Tipo | Funcional / Regresión |
| Precondiciones | Sesión iniciada con `standard_user`, carrito vacío |
| Datos | Nombre: Ana · Apellido: Pérez · Código postal: 130001 |
| Pasos | 1. Agregar "Sauce Labs Backpack" al carrito<br>2. Abrir el carrito y pulsar **Checkout**<br>3. Completar los datos y pulsar **Continue**<br>4. Pulsar **Finish** |
| Resultado esperado | Se muestra "Thank you for your order!" |
| Automatizado en | `tests/ui/test_checkout.py::test_compra_completa` |

| ID | Titulo | Tipo |
| TC-004 | Login rechazado con contraseña incorrecta | Negativa |
| TC-005 | Agregar un producto actualiza el contador del carrito | Funcional |
| TC-006 | El producto agregado aparece en el carrito | Funcional |
| TC-007 | Checkout rechazado sin nombre | Negativa |
| TC-008 | Ordenar productos por precio de menor a mayor | Funcional |
| TC-009 | Ordenar productos por nombre de la Z a la A | Funcional |
| TC-010 | Obtener un post inexistente devuelve 404 | API / Negativa |
