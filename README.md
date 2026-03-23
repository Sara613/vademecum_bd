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
