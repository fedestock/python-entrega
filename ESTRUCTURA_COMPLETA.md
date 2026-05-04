# 📁 Estructura Completa del Proyecto

```
TuPrimeraPagina/
│
├── 📄 manage.py                    # Script principal de Django
├── 📄 requirements.txt             # Dependencias (Django, etc)
├── 📄 load_sample_data.py          # Script para cargar datos de ejemplo
├── 📄 db.sqlite3                   # Base de datos (generada al hacer migrate)
│
├── 📋 README.md                    # ⭐ DOCUMENTACIÓN PRINCIPAL
├── 📋 RESUMEN_RAPIDO.md            # Resumen de requisitos
├── 📋 GITHUB_SETUP.md              # Cómo subir a GitHub
├── 📋 COMANDOS_UTILES.md           # Comandos Django útiles
├── 📋 .gitignore                   # Archivos a ignorar en Git
│
├── 📁 blog_project/                # Configuración del proyecto
│   ├── __init__.py
│   ├── settings.py                 # Configuración Django
│   ├── urls.py                     # Rutas principales
│   └── wsgi.py
│
├── 📁 blog/                        # Aplicación principal (app)
│   ├── migrations/                 # Migraciones de BD
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py                    # Configuración del admin
│   ├── apps.py                     # Config de la app
│   ├── models.py                   # ⭐ 3 CLASES: Category, Post, Comment
│   ├── forms.py                    # ⭐ 4 FORMULARIOS
│   ├── views.py                    # Lógica de las vistas
│   └── urls.py                     # Rutas de la app
│
└── 📁 templates/                   # Plantillas HTML (HERENCIA)
    ├── base.html                   # ⭐ PLANTILLA BASE (plantilla padre)
    ├── index.html                  # Página principal
    ├── post_detail.html            # Detalle del post + comentarios
    ├── create_post.html            # Formulario crear post
    ├── create_category.html        # Formulario crear categoría
    ├── create_comment.html         # Formulario crear comentario
    ├── all_posts.html              # Todos posts + BÚSQUEDA
    ├── all_categories.html         # Todas las categorías
    └── category_posts.html         # Posts filtrados por categoría
```

---

## 📊 Desglose de Requisitos

### 🏗️ ARQUITECTURA MVT

| Componente | Archivo | Cumple |
|-----------|---------|--------|
| **Modelos** | `blog/models.py` | ✅ 3 clases |
| **Vistas** | `blog/views.py` | ✅ 7 vistas |
| **Templates** | `templates/*.html` | ✅ 9 templates |
| **URLs** | `blog/urls.py` + `blog_project/urls.py` | ✅ Rutas configuradas |

### 🗄️ MODELOS (3 CLASES)

```python
# blog/models.py

1. Category
   - name (CharField)
   - description (TextField)
   - created_at (DateTimeField)

2. Post
   - title (CharField)
   - content (TextField)
   - author (CharField)
   - category (ForeignKey → Category)
   - created_at (DateTimeField)
   - updated_at (DateTimeField)
   - published (BooleanField)

3. Comment
   - post (ForeignKey → Post)
   - author_name (CharField)
   - content (TextField)
   - email (EmailField)
   - created_at (DateTimeField)
   - approved (BooleanField)
```

### 📝 FORMULARIOS (4 TOTAL)

```python
# blog/forms.py

1. CategoryForm        → Para crear categorías
2. PostForm           → Para crear posts
3. CommentForm        → Para agregar comentarios
4. SearchPostForm     → ⭐ BÚSQUEDA en BD
```

### 🎨 HERENCIA DE PLANTILLAS

```html
<!-- base.html -->
<!-- Plantilla padre -->
<!-- - Navbar con links -->
<!-- - Footer -->
<!-- - Bloque {% block content %} -->

<!-- Todas las demás heredan: -->
{% extends 'base.html' %}
{% block content %}
  ... contenido específico ...
{% endblock %}
```

**Templates que heredan:**
- index.html
- post_detail.html
- create_post.html
- create_category.html
- create_comment.html
- all_posts.html
- all_categories.html
- category_posts.html

---

## 🔗 RELACIONES ENTRE MODELOS

```
Category (1) ──────────────── (N) Post
                    ForeignKey
                    
Post (1) ──────────────── (N) Comment
            ForeignKey
```

---

## 🌐 RUTAS Y VISTAS

| URL | Vista | Función |
|-----|-------|---------|
| `/` | `index()` | Página principal con posts |
| `/posts/` | `all_posts()` | Todos posts + **BÚSQUEDA** ⭐ |
| `/post/<id>/` | `post_detail()` | Detalle + comentarios |
| `/categorias/` | `all_categories()` | Todas categorías |
| `/category/<id>/` | `category_posts()` | Posts de una categoría |
| `/crear-post/` | `create_post()` | **FORMULARIO** crear post |
| `/crear-categoria/` | `create_category()` | **FORMULARIO** crear categoría |
| `/crear-comentario/` | `create_comment()` | **FORMULARIO** crear comentario |

---

## ✅ CHECKLIST DE REQUISITOS

### Tercera Entrega CoderHouse

- [x] Link de GitHub *(ver GITHUB_SETUP.md)*
- [x] Proyecto Web Django con patrón MVT
  - [x] Herencia de HTML (base.html)
  - [x] Por lo menos 3 clases en models (Category, Post, Comment)
  - [x] Un formulario para insertar datos a cada model
    - [x] CategoryForm
    - [x] PostForm
    - [x] CommentForm
  - [x] Un formulario para buscar algo en la BD
    - [x] SearchPostForm (busca posts)
- [x] README que indique:
  - [x] Orden en que se prueban las cosas
  - [x] Dónde están las funcionalidades

---

## 🚀 INICIO RÁPIDO

```bash
# 1. Instalar
pip install -r requirements.txt

# 2. Migrar
python manage.py migrate

# 3. Crear admin
python manage.py createsuperuser

# 4. Correr
python manage.py runserver

# 5. Visitar
http://localhost:8000
```

---

**Proyecto completo y listo para entregar ✅**
