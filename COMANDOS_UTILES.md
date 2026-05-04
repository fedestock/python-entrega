# 🔧 Comandos Útiles de Django

## Instalación Inicial

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno (Windows)
venv\Scripts\activate

# Activar entorno (Mac/Linux)
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

## Migraciones

```bash
# Ver migraciones pendientes
python manage.py showmigrations

# Crear migraciones automáticas
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Ver estado de migraciones en detalle
python manage.py showmigrations --list
```

## Servidor de Desarrollo

```bash
# Iniciar servidor (por defecto en localhost:8000)
python manage.py runserver

# Iniciar en puerto específico
python manage.py runserver 8080

# Iniciar en IP específica
python manage.py runserver 0.0.0.0:8000
```

## Panel de Admin

```bash
# Crear superusuario (admin)
python manage.py createsuperuser

# Usuario sugerido:
# Username: admin
# Email: admin@example.com
# Password: admin123
```

**Acceder al admin:**
- URL: `http://localhost:8000/admin/`
- Usuario: admin
- Contraseña: admin123

## Shell de Django

```bash
# Abre una consola Python con Django cargado
python manage.py shell

# Ejemplos de uso en la shell:
# >>> from blog.models import Post, Category
# >>> Category.objects.all()
# >>> Post.objects.count()
# >>> Post.objects.filter(published=True)
```

## Datos de Ejemplo

```bash
# Cargar datos de ejemplo
python manage.py shell < load_sample_data.py

# O manualmente en la shell
python manage.py shell
# >>> from blog.models import Category, Post
# >>> Category.objects.create(name="Test", description="Test")
```

## Mantenimiento

```bash
# Limpiar archivos .pyc
find . -type d -name __pycache__ -exec rm -r {} +

# Eliminar la BD (para empezar de cero)
rm db.sqlite3
python manage.py migrate
```

## Recolectar archivos estáticos (producción)

```bash
python manage.py collectstatic
```

## Tests (si los tienes)

```bash
# Ejecutar todos los tests
python manage.py test

# Tests de la app blog
python manage.py test blog

# Tests verbosos
python manage.py test --verbosity=2
```

## Depuración

```bash
# Ver la query SQL que genera una consulta
python manage.py shell
# >>> from django.db import connection
# >>> from blog.models import Post
# >>> Post.objects.filter(published=True)
# >>> print(connection.queries[-1])
```

## Verificar problemas

```bash
# Verificar la configuración
python manage.py check

# Verificar archivos estáticos
python manage.py findstatic --list
```

## Reset Completo (cuidado!)

```bash
# Elimina la BD, borra migraciones y vuelve a empezar
rm db.sqlite3
rm blog/migrations/000*.py
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

## Flujo Típico de Desarrollo

```bash
# 1. Modificas un modelo
nano blog/models.py

# 2. Creas migración
python manage.py makemigrations

# 3. Aplicas migración
python manage.py migrate

# 4. Pruebas en el shell
python manage.py shell

# 5. Ejecutas el servidor
python manage.py runserver

# 6. Visitas en el navegador
# http://localhost:8000
```

---

**Nota:** Siempre que cambies los modelos, debes hacer:
1. `makemigrations`
2. `migrate`

**¡Listo para desarrollar! 🚀**
