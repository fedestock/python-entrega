"""
Script para cargar datos de ejemplo en la base de datos.
Ejecutar con: python manage.py shell < load_sample_data.py
"""

from blog.models import Category, Post, Comment

# Crear categorías
categories = [
    Category.objects.create(
        name="Programación",
        description="Artículos sobre lenguajes de programación y desarrollo"
    ),
    Category.objects.create(
        name="Web Development",
        description="Tutoriales y guías sobre desarrollo web"
    ),
    Category.objects.create(
        name="Bases de Datos",
        description="Contenido sobre SQL, NoSQL y administración de datos"
    ),
]

# Crear posts
posts = [
    Post.objects.create(
        title="Introducción a Django",
        content="Django es un framework web de alto nivel que fomenta el desarrollo rápido y el diseño limpio y pragmático.\n\nFue desarrollado en gran parte porque los usuarios de Django News de Lawrence Journal-World necesitaban herramientas de desarrollo rápido.",
        author="Juan García",
        category=categories[0],
        published=True
    ),
    Post.objects.create(
        title="HTML5: Las mejores prácticas",
        content="HTML5 es la quinta revisión del estándar HTML. Este artículo te mostrará las mejores prácticas para escribir código HTML5 semántico.\n\n1. Usar elementos semánticos\n2. Validar tu código\n3. Usar atributos data\n4. Accesibilidad primero",
        author="María López",
        category=categories[1],
        published=True
    ),
    Post.objects.create(
        title="PostgreSQL vs MySQL",
        content="Comparación entre dos de los sistemas de gestión de bases de datos relacionales más populares.\n\nPostgreSQL ofrece características avanzadas como JSON, full-text search y extensibilidad.\n\nMySQL es más simple de instalar y utilizar, perfecto para aplicaciones pequeñas y medianas.",
        author="Carlos Rodríguez",
        category=categories[2],
        published=True
    ),
]

# Crear comentarios
comments = [
    Comment.objects.create(
        post=posts[0],
        author_name="Pedro Martín",
        content="Excelente artículo, muy útil para principiantes!",
        email="pedro@example.com"
    ),
    Comment.objects.create(
        post=posts[0],
        author_name="Ana Gómez",
        content="Gracias por compartir esto. Estoy aprendiendo Django y esto me ayudó mucho.",
        email="ana@example.com"
    ),
    Comment.objects.create(
        post=posts[1],
        author_name="Luis Fernández",
        content="Las mejores prácticas son muy importantes. Buen resumen!",
        email="luis@example.com"
    ),
]

print("✅ Datos de ejemplo cargados exitosamente!")
print(f"✅ {len(categories)} categorías creadas")
print(f"✅ {len(posts)} posts creados")
print(f"✅ {len(comments)} comentarios agregados")
