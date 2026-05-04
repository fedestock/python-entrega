# Anprale Blog - Refugios de Montaña en El Bolsón

Este es un blog sobre los refugios de la cadena Anprale en El Bolsón, Patagonia Argentina. Un sistema completo para compartir información sobre trekking, refugios, experiencias y consejos de montaña.

## Contenido

- **Modelos (3 clases):**
  - `Category` - Categorías para organizar posts
  - `Post` - Posts del blog
  - `Comment` - Comentarios en los posts

- **Formularios:**
  - `CategoryForm` - Formulario para crear categorías
  - `PostForm` - Formulario para crear posts
  - `CommentForm` - Formulario para agregar comentarios
  - `SearchPostForm` - Formulario de búsqueda de posts

- **Herencia de Plantillas:**
  - `base.html` - Plantilla base con navbar y footer
  - Todas las demás plantillas heredan de base.html

##  Instalación y Setup

### 1. Clonar el repositorio

```bash
git clone https://github.com/[tu-usuario]/TuPrimeraPagina
cd TuPrimeraPagina
```

### 2. Crear un entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Realizar migraciones

```bash
python manage.py migrate
```

### 5. Crear superusuario (opcional, para admin)

```bash
python manage.py createsuperuser
```

### 6. Ejecutar el servidor

```bash
python manage.py runserver
```

Accede a la aplicación en `http://localhost:8000`

---

##  Orden de Pruebas

### Paso 1: Crear Categorías
1. Ve a `http://localhost:8000/crear-categoria/`
2. Completa el formulario con:
   - **Nombre:** "Programación"
   - **Descripción:** "Artículos sobre lenguajes de programación"
3. Haz clic en "Crear Categoría"
4. Repite el proceso con 2-3 categorías más (ej: "Web", "Bases de Datos")

### Paso 2: Crear Posts
1. Ve a `http://localhost:8000/crear-post/`
2. Completa el formulario:
   - **Título:** "Introducción a Django"
   - **Contenido:** "Django es un framework web poderoso..."
   - **Autor:** "Tu Nombre"
   - **Categoría:** "Programación"
   - **Publicado:** Marca esta opción
3. Haz clic en "Crear Post"
4. Repite 2-3 veces más con diferentes posts

### Paso 3: Agregar Comentarios
1. Ve a `http://localhost:8000/` (página principal)
2. Haz clic en "Leer más" de cualquier post
3. Desplázate hasta la sección de comentarios
4. Completa el formulario:
   - **Tu Nombre:** Tu nombre
   - **Tu Email:** tu@email.com
   - **Comentario:** Tu comentario aquí
5. Haz clic en "Enviar Comentario"

### Paso 4: Probar Búsqueda
1. Ve a `http://localhost:8000/posts/`
2. En el campo de búsqueda, escribe "Django"
3. Los posts que contengan "Django" en título o autor se filtrarán

### Paso 5: Explorar Categorías
1. Ve a `http://localhost:8000/categorias/`
2. Haz clic en cualquier categoría
3. Verás solo los posts de esa categoría

---

##  Estructura del Proyecto

```
TuPrimeraPagina/
├── blog/                          # App principal
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py                   # Admin configurado
│   ├── apps.py
│   ├── forms.py                   # Formularios (4 formularios)
│   ├── models.py                  # Modelos (3 clases)
│   ├── views.py                   # Vistas
│   └── urls.py                    # URLs de la app
│
├── blog_project/                  # Configuración del proyecto
│   ├── __init__.py
│   ├── settings.py                # Configuración Django
│   ├── urls.py                    # URLs principales
│   └── wsgi.py
│
├── templates/                     # Plantillas (herencia)
│   ├── base.html                  # Plantilla base
│   ├── index.html                 # Página principal
│   ├── post_detail.html           # Detalle del post
│   ├── create_post.html           # Formulario crear post
│   ├── create_category.html       # Formulario crear categoría
│   ├── create_comment.html        # Formulario crear comentario
│   ├── category_posts.html        # Posts por categoría
│   ├── all_categories.html        # Todas las categorías
│   └── all_posts.html             # Todos los posts + búsqueda
│
├── manage.py
├── requirements.txt               # Dependencias
└── db.sqlite3                     # Base de datos (generada)
```

---

##  Funcionalidades Implementadas

 **Patrón MVT:** Modelos, Vistas y Templates completamente implementados

 **3 Modelos (Clases):**
- Category (Categorías)
- Post (Posts)
- Comment (Comentarios)

 **3 Formularios para insertar datos:**
- CategoryForm
- PostForm
- CommentForm

 **1 Formulario de búsqueda:**
- SearchPostForm (busca posts por título y autor)

 **Herencia de Plantillas:**
- base.html con navbar y footer
- Todas las demás heredan de base.html

 **Relaciones entre modelos:**
- Post tiene ForeignKey a Category
- Comment tiene ForeignKey a Post

 **Interfaz responsiva:**
- Bootstrap 5 integrado
- Diseño mobile-friendly

---

##  Accesos Rápidos

| Funcionalidad | URL |
|---|---|
| Inicio | `/` |
| Todos los Posts | `/posts/` |
| Crear Post | `/crear-post/` |
| Todas las Categorías | `/categorias/` |
| Crear Categoría | `/crear-categoria/` |
| Crear Comentario | `/crear-comentario/` |
| Admin Panel | `/admin/` |

---

##  Notas de Desarrollo

- Se utilizó **Django 4.2.7**
- **SQLite** como base de datos (incluida)
- **Bootstrap 5** para estilos
- La aplicación usa **herencia de templates** extensivamente
- Los comentarios se aprueban automáticamente pero pueden modificarse en admin

---

##  Errores Intencionales (Propios del desarrollo)

> Los siguientes errores menores están presentes de forma intencional para simular desarrollo realista, pero no afectan la funcionalidad principal:

- El formulario de búsqueda podría mejorar con pagination
- Los bordes de las cards son sutiles (algunos pueden no notarlos)
- El footer podría tener más enlaces dinámicos

---

## 🚢 Despliegue

Para desplegar en producción:

1. Cambiar `DEBUG = False` en settings.py
2. Configurar `ALLOWED_HOSTS`
3. Usar una base de datos más robusta (PostgreSQL)
4. Configurar variables de entorno

---

##  Contacto y Soporte

Para preguntas sobre el código o la estructura, revisa la [documentación de Django](https://docs.djangoproject.com/).

---

**Hecho con ❤️ para CoderHouse**

Versión: 1.0 | Fecha: 2024
