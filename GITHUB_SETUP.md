# 📤 Instrucciones para subir a GitHub

## Paso 1: Crear el repositorio en GitHub

1. Ve a [github.com](https://github.com) y accede a tu cuenta
2. Haz clic en el botón "+" arriba a la derecha
3. Selecciona "New repository"
4. **Nombre del repositorio:** `TuPrimeraPagina` (o con tu apellido: `TuPrimeraPagina+Apellido`)
5. Añade una descripción: "Blog en Django - Tercera Entrega CoderHouse"
6. Selecciona "Public" (para que se vea)
7. NO inicialices con README (lo tenemos)
8. Haz clic en "Create repository"

## Paso 2: Inicializar Git en tu máquina

```bash
cd TuPrimeraPagina
git init
```

## Paso 3: Configurar Git

```bash
git config user.name "Tu Nombre"
git config user.email "tu@email.com"
```

## Paso 4: Agregar archivos

```bash
git add .
```

## Paso 5: Hacer el primer commit

```bash
git commit -m "Initial commit: Tercera Entrega - Blog en Django con herencia de plantillas"
```

## Paso 6: Agregar el repositorio remoto

Reemplaza `tu-usuario` con tu usuario de GitHub:

```bash
git branch -M main
git remote add origin https://github.com/tu-usuario/TuPrimeraPagina.git
```

## Paso 7: Push al repositorio

```bash
git push -u origin main
```

## ✅ ¡Listo!

Tu proyecto está en GitHub. Verifica que todo esté bien:
- Visita `https://github.com/tu-usuario/TuPrimeraPagina`
- Deberías ver todos los archivos

---

### Commits importantes para hacer durante el desarrollo:

```bash
# Después de crear modelos
git add blog/models.py
git commit -m "Add: Modelos Category, Post y Comment"

# Después de crear formularios
git add blog/forms.py
git commit -m "Add: Formularios para Category, Post, Comment y búsqueda"

# Después de crear vistas
git add blog/views.py
git commit -m "Add: Vistas principales del blog"

# Después de crear templates
git add templates/
git commit -m "Add: Templates con herencia de base.html"

# Antes de terminar
git add .
git commit -m "Fix: Últimos ajustes y validaciones"
```

---

### Comandos útiles de Git:

```bash
# Ver estado
git status

# Ver historial de commits
git log --oneline

# Ver cambios no guardados
git diff

# Deshacer último commit (si no lo subiste)
git reset --soft HEAD~1

# Actualizar desde GitHub
git pull origin main
```

---

**¡Éxito con tu entrega! 🚀**
