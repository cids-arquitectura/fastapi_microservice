# Microservicio Python con FastAPI

## Dependencias
Python no tiene node_modules ni package.json, se maneja a traves de virtual enviroments. Para crear
el virtual enviroment del proyecto, estando dentro de la carpeta del mismo debemos ejecutar

```bash
  python -m venv venv
```
Esto va a generar una carpeta en donde se van a instalar todas las dependencias del proyecto. Para poder
usarlo en la consola donde vamos a trabajar hay que ejecutar:

```bash
//linux
source venv/bin/activate
//windows
venv\Scripts\activate
```
Podemos configurar nuestro IDE para que haga la activación automáticamente.
Sabremos si estamos dentro del venv ya que se agregara el contexto entre paréntesis.
```
(venv) franco@ryzen:~/cids/arquitectura/fastapi_microservice$
```

Una vez con el venv activado podemos proceder a instalar las dependencias definidas con:
```bash
pip install -r requirements.txt
```

Si agregásemos dependencias a nuestro proyecto, tenemos que actualizar el 
archivo de dependencias con:
```bash
pip freeze > requirements.txt
```

## Variables de entorno
Las siguentes variables de entorno son necesarias para correr el microservicio
 

- DB_HOST=DATABASE_HOST
- DB_PORT=DATABASE_PORT
- DB_SID=ORACLE_SERVICE_ID
- DB_USER=DATABASE_USER
- DB_PASS=DATABASE_PASS
- DB_CONN_MIN=DATABASE_MINIMUM_CONNECTION_INSTANCES
- DB_CONN_MAX=DATABASE_MAXIMUM_CONNECTION_INSTANCES
- REDIS_HOST=REDIS_HOSTNAME