# Backend Chat Bot

Backend desarrollado con Django REST Framework para el sistema de Chat Bot.

## 🚀 Requisitos Previos

- Docker
- Docker Compose
- Make (opcional, para comandos simplificados)

## 📦 Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd backend-chat-bot
```

### 2. Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

```env
POSTGRES_HOST=db
POSTGRES_DB=chatbot_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=tu_contraseña_segura
```

### 3. Crear la red externa de Docker

Si no existe, crea la red `reverse-proxy`:

```bash
docker network create reverse-proxy
```

## 🐳 Uso con Docker

### Construir y levantar los contenedores

```bash
docker-compose up --build
```

O para ejecutar en segundo plano:

```bash
docker-compose up -d --build
```

### Ver los logs

```bash
docker-compose logs -f django
```

### Detener los contenedores

```bash
docker-compose down
```

Para detener y eliminar los volúmenes (incluyendo la base de datos):

```bash
docker-compose down -v
```

## 📊 Gestión de Base de Datos

### Ejecutar migraciones

Con Make:
```bash
make django@migrate
```

Sin Make:
```bash
docker exec django-app-chat-bot python manage.py migrate
```

### Crear migraciones

Con Make:
```bash
make django@makemigrations
```

Sin Make:
```bash
docker exec django-app-chat-bot python manage.py makemigrations
```

### Crear superusuario

Con Make:
```bash
make django@createsuperuser
```

Sin Make:
```bash
docker exec -it django-app-chat-bot python manage.py createsuperuser
```

## 🔧 Comandos Útiles

### Ejecutar comandos de Django dentro del contenedor

```bash
docker exec django-app-chat-bot python manage.py <comando>
```

### Acceder al shell de Django

```bash
docker exec -it django-app-chat-bot python manage.py shell
```

### Acceder a la base de datos PostgreSQL

```bash
docker exec -it db-capital-one-ia psql -U postgres -d chatbot_db
```

### Ver logs en tiempo real

```bash
docker-compose logs -f
```

### Reconstruir el contenedor después de cambios

```bash
docker-compose up --build --force-recreate
```

## 🌐 Acceso a la Aplicación

Una vez levantados los contenedores, la aplicación estará disponible en:

- **API**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin

## 📁 Estructura del Proyecto

```
backend-chat-bot/
├── apps/              # Aplicaciones Django
│   └── cores/         # App principal
├── config/            # Configuración del proyecto
├── docker-compose.yml # Configuración de servicios Docker
├── Dockerfile         # Imagen Docker multi-stage
├── Makefile          # Comandos simplificados
├── manage.py         # Script de gestión de Django
└── requirements.txt  # Dependencias de Python
```

## 🏗️ Arquitectura Docker

### Servicios

- **django**: Servicio principal de Django
  - Puerto: 8000
  - Imagen: Multi-stage (development/production)
  - Volúmenes: Montaje del código fuente para desarrollo

- **db**: Base de datos PostgreSQL
  - Imagen: postgres:alpine
  - Volúmenes: Persistencia de datos
  - Network: reverse-proxy

### Stages del Dockerfile

1. **development**: Para desarrollo local
   - Incluye todas las dependencias
   - Servidor de desarrollo integrado
   - Montaje de volúmenes para hot-reload

2. **production**: Para producción
   - Optimizado con multi-stage build
   - Servidor Gunicorn
   - Health check incluido

### Cambiar entre development y production

En `docker-compose.yml`, modifica el target:

```yaml
build:
  target: development  # o production
```

## 🛠️ Desarrollo

### Realizar cambios en el código

Los cambios en el código se reflejan automáticamente gracias al montaje de volúmenes. Solo necesitas:

1. Editar el código
2. Reiniciar el contenedor si es necesario:
   ```bash
   docker-compose restart django
   ```

### Depuración

Para ver logs detallados:

```bash
docker-compose logs -f django
```

## 🔒 Seguridad

- No olvides cambiar las credenciales por defecto en producción
- Modifica `SECRET_KEY` en `config/settings.py` para producción
- Configura `ALLOWED_HOSTS` apropiadamente para producción
- No commitees el archivo `.env` con información sensible

## 📝 Notas Adicionales

- El contenedor de PostgreSQL persistirá los datos entre reinicios
- Para limpiar completamente la base de datos, usa `docker-compose down -v`
- El proyecto está configurado para usar la red `reverse-proxy` externa
- Todos los contenedores se reinician automáticamente a menos que se detengan manualmente

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

