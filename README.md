### Normalización del Vademécum Optometría

El archivo Excel original tenía toda la información de cada medicamento en una sola fila, lo que generaba **redundancia** (mismo laboratorio repetido 30 veces, misma posología repetida, etc.).
La normalización consiste en separar esos datos en tablas independientes y conectarlas con llaves foráneas.

### Diagrama de relaciones

```
therapeutic_groups
    id (PK)
    name
        │
        │ 1:N (un grupo tiene muchas familias)
        ▼
    family
        id (PK)
        name
        description
        id_therapeutic_group (FK → therapeutic_groups.id)
            │
            │ 1:N (una familia tiene muchos productos)
            ▼
        product_details
            id (PK)
            commercial_name
            generic_name
            action_mechanism
            concentration
            notes
            is_active
            id_family              (FK → family.id)
            id_laboratory          (FK → laboratory.id)
            id_pharmaceutical_form (FK → pharmaceutical_form.id)
            id_posology            (FK → posology.id)

laboratory             pharmaceutical_form       posology
    id (PK)                id (PK)                id (PK)
    name                   name                   name
    │                      │                      │
    └──────────────────────┴──────────────────────┘
                            ↑ todas apuntan a product_details
```

### ¿Por qué estas tablas?

| Tabla | Propósito |
|-------|-----------|
| `therapeutic_groups` | Evita repetir el nombre del grupo (Antibióticos, Antialérgicos...) |
| `family` | Agrupa medicamentos por mecanismo similar; hereda el grupo terapéutico |
| `laboratory` | Catálogo de laboratorios farmacéuticos (no repetir "Tecnoquímicas S.A" 20 veces) |
| `pharmaceutical_form` | Catálogo: Solución oftálmica, Ungüento, etc. |
| `posology` | Catálogo de instrucciones de dosificación |
| `product_details` | Tabla principal — cada fila es un medicamento único |

---

## Estructura del proyecto

```
vademecumDB/
├── app.py                              ← Servidor Flask + registro de rutas
├── requirements.txt                    ← Librerías necesarias
├── .env                                ← Credenciales de BD 
├── .gitignore                          ← Archivos que Git debe ignorar
├── README.md                           ← Descripcion
│
├── db/
│   ├── __init__.py
│   ├── db.py                           ← Conexión a PostgreSQL Session
│   └── models.py                       ← definición de tablas
│
├── common/
│   ├── __init__.py
│   └── http.py                         ← Respuestas HTTP estandarizadas
│
└── routes/
    ├── __init__.py
    │
    │--family/
    │.  │--__init__.py
    │   │--family_service.py
    │   │--family_controller.py
    │   │--family_routes.py← CRUD completo para tabla family
    │--laboratory/
    │.  │--__init__.py
    │   │--laboratory_service.py
    │   │--laboratory_controller.py
    │   │--laboratory_routes.py ← CRUD completo para tabla laboratory
    │--therapeutic_groups/
    │.  │--__init__.py
    │   │--therapeutic_service.py
    │   │--therapeutic_controller.py
    │   │--therapeutic_routes.py ← CRUD completo para tabla laboratory
    └── products/
        ├── __init__.py
        └── products_routes.py ← CRUD completo para tabla product_details
```

---

## Paso a paso para ejecutar el proyecto

### Paso 1 — Instalar PostgreSQL
Descárgalo de https://www.postgresql.org/download/  
Durante la instalación anota bien tu usuario y contraseña.

### Paso 2 — Crear la base de datos en DBeaver 

**Opción A — En DBeaver:**
1. Abre DBeaver → Nueva conexión → PostgreSQL
2. Rellena: Host `localhost`, Puerto `5432`, User `postgres`, Password (todo dependiendo de ti)
3. Conéctate, clic derecho en Databases → Create Database
4. Nombre: `vademecumDB` → OK

**Opción B — En la terminal (psql):**
```sql
psql -U postgres
CREATE DATABASE "vademecumDB";
\q
```

### Paso 3 — Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/vademecumDB.git
cd vademecumDB
```

### Paso 4 — Crear el entorno virtual
```bash
# Crear el entorno virtual (solo la primera vez)
python -m venv .venv

# Activarlo:
# En Windows:
.venv\Scripts\activate

# En macOS / Linux:
source .venv/bin/activate

# Sabes que está activo porque aparece (.venv) al inicio de la terminal
```

### Paso 5 — Instalar las dependencias
```bash
pip install -r requirements.txt
```

### Paso 6 — Configurar el archivo .env
Crea un archivo llamado `.env` en la raíz del proyecto con este contenido:
```env
DATABASE_URL=postgresql://postgres:TU_CONTRASEÑA@localhost:tupuerto/vademecumDB
HOST=127.0.0.1
PORT=5000
```

### Paso 7 — Ejecutar el servidor
```bash
python app.py
```

Deberías ver en la terminal:
```Tablas verificadas / creadas en vademecumDB
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Paso 8 — Verificar en DBeaver
Actualiza la conexión en DBeaver y deberías ver las 6 tablas creadas:
`therapeutic_groups`, `laboratory`, `pharmaceutical_form`, `posology`, `family`, `product_details`


## Guía completa de Postman

### Configuración base
- **Base URL:** `http://127.0.0.1:5000`
- En solicitudes POST y PUT agrega el header: `Content-Type: application/json`


### Families

####INSERT 1 — Primero necesitas crear un TherapeuticGroup directamente en DBeaver
> Como no creamos rutas para therapeutic_groups, inserta manualmente en DBeaver:
```sql
INSERT INTO therapeutic_groups (name) VALUES ('Antibióticos');
INSERT INTO therapeutic_groups (name) VALUES ('Antialérgicos');
```
####  INSERT — Crear familia 1
```
POST http://127.0.0.1:5000/families/

Body (raw JSON):
{
  "name": "Inhibidores de Pared",
  "description": "Infecciones oculares bacterianas como conjuntivitis y blefaritis",
  "id_therapeutic_group": 1
}
```
**Respuesta esperada (201):**
```json
{
  "status": "success",
  "message": "Familia creada exitosamente",
  "data": {
    "id": 1,
    "name": "Inhibidores de Pared",
    "description": "Infecciones oculares bacterianas como conjuntivitis y blefaritis",
    "id_therapeutic_group": 1
  }
}
```
#### GET ONE — Obtener familia por ID
```
GET http://127.0.0.1:5000/families/1
```

#### UPDATE — Actualizar familia 1
```
PUT http://127.0.0.1:5000/families/1

Body:
{
  "description": "Descripción actualizada: tratan infecciones oculares externas"
}
```

#### DELETE — Eliminar familia 2
```
DELETE http://127.0.0.1:5000/families/2
```

```sql
-- Laboratorios
INSERT INTO laboratory (name) VALUES ('Oftalmoquímica S.A');
INSERT INTO laboratory (name) VALUES ('Tecnoquímicas S.A');

-- Formas farmacéuticas
INSERT INTO pharmaceutical_form (name) VALUES ('Solución oftálmica');
INSERT INTO pharmaceutical_form (name) VALUES ('Ungüento oftálmico');

-- Posologías
INSERT INTO posology (name) VALUES ('Aplicar 1 gota en cada ojo cada 6 horas por 7 días');
INSERT INTO posology (name) VALUES ('Aplicar 1 gota en cada ojo cada 12 horas por 7 días');
```

## Formato estándar de respuestas

Todas las respuestas del servidor tienen este formato:

```json
{
  "status":  "success" | "error",
  "message": "Descripción del resultado",
  "data":    { objeto } | [ lista ] | null
}
```

| Código | Cuándo se usa |
|--------|--------------|
| 200 | GET exitoso, PUT exitoso, DELETE exitoso |
| 201 | POST exitoso (recurso creado) |
| 400 | Falta un campo obligatorio en el body |
| 404 | El ID que buscas no existe |
| 500 | Error inesperado del servidor |

# abajo estan las 8 respectivas imagenes 
# Vademecum API

API para el manejo de información farmacéutica (vademécum) desarrollada con Python, Flask, SQLAlchemy y Blueprints.

## Requisitos

- Python 3.8+
- PostgreSQL (u otro motor compatible con SQLAlchemy)

## Instalación

1. Clonar el repositorio.
2. Crear un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Configurar las variables de entorno en el archivo `.env`:
   - `DATABASE_URL`: URL de conexión a la base de datos PostgreSQL.

## Ejecución

Para iniciar el servidor de desarrollo:
```bash
python app.py
```

La API estará disponible en `http://localhost:5001/`.

## Endpoints

### Grupos Terapéuticos
- `GET /api/therapeutic-groups`: Listar todos.
- `GET /api/therapeutic-groups/<id>`: Obtener uno.
- `POST /api/therapeutic-groups`: Crear uno.
- `PUT /api/therapeutic-groups/<id>`: Actualizar uno.
- `DELETE /api/therapeutic-groups/<id>`: Eliminar uno.

### Familias
- `GET /api/families`: Listar todas.
- `GET /api/families/<id>`: Obtener una.
- `POST /api/families`: Crear una.
- `PUT /api/families/<id>`: Actualizar una.
- `DELETE /api/families/<id>`: Eliminar una.

### Laboratorios
- `GET /api/laboratories`: Listar todos.
- `GET /api/laboratories/<id>`: Obtener uno.
- `POST /api/laboratories`: Crear uno.
- `PUT /api/laboratories/<id>`: Actualizar uno.
- `DELETE /api/laboratories/<id>`: Eliminar uno.

### Productos
- `GET /api/products`: Listar todos.
- `GET /api/products/<id>`: Obtener uno.
- `POST /api/products`: Crear uno.
- `PUT /api/products/<id>`: Actualizar uno.
- `DELETE /api/products/<id>`: Eliminar uno.

## Estructura del Proyecto

```text
db/             # Configuración de BD y modelos
common/         # Utilidades comunes (respuestas HTTP)
routes/         # Controladores, servicios y rutas (Blueprints)
app.py          # Punto de entrada de la aplicación
requirements.txt # Dependencias
.env            # Variables de entorno
```
