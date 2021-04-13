# Sistema de Administracion de Persona (SAP)

Esta es un aplicación web estilo CRUD realidad con Django. Es muy básica y sencilla, pero contempla todas las funciones para agregar personas, eliminarlas o editarlas. Estos son los pasos para la instalación:

- $ git clone https://github.com/agusantarelli/sap.git
- $ cd sap/personas_django
- $ python -m venv myenv
- $ source myenv/bin/activate
- $ pip install Django
- $ pip install psycopg2-binary
- $ cd sap
 Una vez completado los pasos anteriores tienen que proceder a crear una base de datos en postgres. Una vez creada, deben proporcionar la indormación de la misma en sap/settings.py en el apartado DATABASES. Una vez completado los datos, procedemos en consola con lo siguiente:
- $ python manage.py migrate
- $ python3 manage.py runserver

Y ahora ingresan al a url que les va a proporcionar la consola, y pueden probar la aplicación web.
