# OrganizaDevs - Backend

Backend de **OrganizaDevs**, una API REST desarrollada con Django REST Framework para gestionar usuarios, proyectos académicos, integrantes y links importantes asociados a cada proyecto.

Este backend se conecta con el frontend desarrollado en Next.js y permite centralizar los recursos principales de un proyecto grupal, como repositorios, documentos, tableros de tareas, diseños y otros enlaces importantes.

---

## Tecnologías utilizadas

- Python
- Django
- Django REST Framework
- PostgreSQL
- Simple JWT
- django-cors-headers
- python-decouple
- psycopg2-binary

---

## Funcionalidades principales

- Registro de usuarios.
- Inicio de sesión mediante JWT.
- Autenticación con access token y refresh token.
- Gestión de proyectos académicos.
- Agregado de miembros a proyectos.
- Organización de links por categorías.
- CRUD de proyectos.
- CRUD de links.
- Control de acceso por usuario autenticado.
- Filtrado de proyectos según el usuario participante.
- Conexión con base de datos PostgreSQL.

---

## Modelo de datos

El backend está organizado principalmente en dos aplicaciones:

```txt
usuarios/
proyectos/
```

---

## Relaciones entre tablas

Resumen general:

```txt
UsuarioPersonalizado
│
├── crea muchos Proyectos
│
├── participa en muchos Proyectos mediante MiembroProyecto
│
└── agrega muchos LinksProyecto

Proyecto
│
├── tiene muchos MiembroProyecto
│
└── tiene muchos LinkProyecto

CategoriaLink
│
└── tiene muchos LinkProyecto
```

Diagrama simplificado:

```txt
UsuarioPersonalizado ───< Proyecto
        │
        │
        └──< MiembroProyecto >─── Proyecto
                                  │
                                  └──< LinkProyecto >─── CategoriaLink
```

---

## Autenticación

La autenticación se realiza mediante **JWT** usando Simple JWT.

Cuando el usuario inicia sesión, el backend devuelve dos tokens:

```txt
access token
refresh token
```

El `access token` se utiliza para acceder a rutas protegidas.

Ejemplo de header necesario:

```txt
Authorization: Bearer ACCESS_TOKEN
```

El `refresh token` permite obtener un nuevo access token cuando el anterior expira.

---

## Autor

Desarrollado por Sebastián Maldonado.

LinkedIn:  
https://www.linkedin.com/in/sebastian-maldonado-8a462b32a/

---

## Licencia

Este proyecto fue desarrollado con fines educativos y como parte de un portfolio personal.
