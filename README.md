# EntrevistaQuoDigital

Este proyecto es una API de Flask para gestionar usuarios, con una base de datos PostgreSQL que se puede levantar con Docker.

-----

## Cómo instalar dependencias

Las dependencias del proyecto se gestionan con `uv`. Para instalarlas, ejecuta el siguiente comando en el directorio `api`:

```bash
uv sync
```

Las dependencias son:

* flask\>=3.1.2
* flask-sqlalchemy\>=3.1.1
* httpie\>=3.2.4
* python-dotenv\>=1.1.1

-----

## Cómo levantar la app localmente

Para levantar la aplicación localmente, necesitas tener Docker y Docker Compose instalados.

1. **Crea un archivo `.env`** en el directorio raíz del proyecto con el siguiente contenido:

    ```
    # DATABASE
    USER=user
    PASSWORD=anypasswd
    NAME=test
    HOST=database
    PORT=5432
    DATABASE_URL=postgresql://user:anypasswd@database:5432/test
    ```

2. **Levanta los servicios** con Docker Compose:

    ```bash
    docker-compose up -d --build
    ```

    Esto creará y levantará dos contenedores: `database` (PostgreSQL) y `flask` (la aplicación). La aplicación estará disponible en `http://localhost:5000`.

-----

## Cómo levantar la base de datos

La base de datos se levanta automáticamente al ejecutar `docker-compose up`. Si solo quieres levantar la base de datos, puedes ejecutar:

```bash
docker-compose up -d database
```

El servicio de la base de datos utiliza una imagen de `postgres:16-alpine` y expone el puerto `5432`. Los datos se almacenan en un volumen de Docker llamado `db_data` para persistencia.

-----

## Ejemplos de llamadas al API

A continuación se muestran ejemplos de cómo interactuar con la API utilizando `httpie`.

### Obtener todos los usuarios

```bash
http GET http://localhost:5000/users
```

### Crear un nuevo usuario

```bash
http POST http://localhost:5000/users name="John Doe" email="john.doe@example.com"
```

### Crear un usuario con un email que ya existe

Si intentas crear un usuario con un email que ya existe, recibirás un error 400.

```bash
http POST http://localhost:5000/users name="Jane Doe" email="john.doe@example.com"
```

**Respuesta esperada:**

```json
{
    "error": "Email already exists"
}
```
