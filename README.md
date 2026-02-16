# ACADEMIX BACKEND

Backend desarrollado con FastAPI (fastapi-mike) para el proyecto Academix.

## Tecnologías utilizadas

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- MySQL (XAMPP)

## Requisitos previos

Antes de ejecutar el proyecto asegúrate de tener instalado:

- Python 3.10+
- Git
- XAMPP (con MySQL activado)
- pip

Verifica que Python esté instalado:
```bash
python --version
```

## Instalación del proyecto

### 1. Clonar el repositorio
```bash
git clone https://github.com/academix10A/academix-backend.git
```

### 2. Entrar al directorio
```bash
cd academix-backend
```

### 3. Crear entorno virtual (recomendado)
```bash
python -m venv venv
```

**Activar entorno virtual:**

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```

## Configuración de la Base de Datos

Este proyecto utiliza MySQL mediante XAMPP.

### PASOS IMPORTANTES (EN ESTE ORDEN)

1. Iniciar XAMPP y asegurarse de que MySQL esté activo.
2. Crear manualmente una base de datos llamada:
```
   academix
```
   Puedes hacerlo desde phpMyAdmin.
3. Ejecutar el backend para que las tablas se creen automáticamente.
4. Una vez creadas las tablas, ejecutar los inserts del archivo:
```
   inserts_prueba.sql
```

## Ejecución del proyecto

El backend se inicia con:
```bash
uvicorn app.main:app --reload
```

Si todo está correcto, el servidor se ejecutará en:
```
http://127.0.0.1:8000
```

## Documentación (Swagger)

FastAPI genera documentación automática.
Puedes verla en:
```
http://127.0.0.1:8000/docs
```

Aquí podrás:

- Probar endpoints
- Ver modelos de datos
- Revisar respuestas
- Probar autenticación si está configurada

## Estructura importante del proyecto

- `app/` → Código principal del backend
- `app/main.py` → Punto de entrada del servidor
- `inserts_prueba.sql` → Datos de prueba para la base de datos
- `requirements.txt` → Dependencias del proyecto

## Flujo de trabajo con Git (IMPORTANTE)

**No trabajar directamente sobre `main`. El trabajo se integra en la rama `develop`.**

### 1. Cambiar a develop y actualizar
```bash
git checkout develop
git pull origin develop
```

### 2. Crear una nueva rama
```bash
git checkout -b feature/nombre-descriptivo
```

**Ejemplo:**
```bash
git checkout -b feature/auth-endpoints
```

### 3. Agregar cambios
```bash
git add .
```

### 4. Crear commit
```bash
git commit -m "Descripción clara del cambio realizado"
```

**Ejemplo:**
```bash
git commit -m "Agrega endpoint de registro de usuario"
```

### 5. Hacer push
```bash
git push origin feature/nombre-descriptivo
```

### 6. Merge a develop

**El merge NO se hace a `main`, se hace a `develop`.**

**Opción A: Desde GitHub**
1. Crear Pull Request hacia `develop`
2. Esperar revisión
3. Hacer merge

**Opción B: Desde consola (si el equipo lo permite)**
```bash
git checkout develop
git pull origin develop
git merge feature/nombre-descriptivo
git push origin develop
```

## Buenas prácticas

- No subir el entorno virtual (`venv/`)
- No subir archivos compilados
- No modificar directamente `main`
- Commits pequeños y claros
- Probar que el backend levante antes de hacer push
- Mantener `develop` siempre funcional
- Siempre hacer pull antes de comenzar a trabajar

## Limpieza del entorno (si hay errores)

Si algo falla con dependencias:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Si la base de datos tiene problemas:

- Verificar que exista la base `academix`
- Verificar credenciales en el archivo de configuración
- Reiniciar XAMPP

## Notas finales

- **El orden correcto es:**
  1. Crear base de datos
  2. Ejecutar backend (crea tablas)
  3. Ejecutar inserts

- **Si el backend no inicia:**
  - Verificar conexión a la base de datos
  - Revisar que MySQL esté activo
  - Revisar errores en consola

---

Backend del proyecto Academix.