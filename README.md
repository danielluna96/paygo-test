# Proyecto Paygo Test

PayGo Test es una aplicación que permite la lectura de datos de empleados. La aplicación de prueba se encuentra alojada en [http://3.135.82.80](http://3.135.82.80)

## Para probarla localmente

Para probarla clonar el repositorio. 

Se debe tener instalado python, desarrollado usando Python 3.10.0.

Ejecutar el comando:

### `pip install -r requirements.txt`
  

Después de instalar las dependencias correr el comando:  

### `python manage.py runserver`  

Abrir [http://localhost:800](http://localhost:8000) para ver en el navegador. 
  
## Sobre el proyecto

El proyecto utiliza principalmente librerías propias de Django, tales como el login, ORM, y demás.

Información sobre los principales folders.

`app/` contiene las configuraciones principales y tiene las urls principales<br />
`static/` tiene el contenido estático tales como estilos e imágenes.<br />
`templates/` Plantillas que son utilizadas por las vistas.<br />
`users/` app que contiene la logica de negocio de los empleados.<br />
 
 
 ## Librerias importantes

- SQLite 3: Motor de bases de datos
- Bootstrap: Para el diseño en las templates
