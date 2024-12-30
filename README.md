# prueba-tecnica-IMEXHS

pre requisitos:

- Contar con un entorno virtual, en este caso se realizó con un venv python 3.12
- Ejecutar el siguiente comando para ejecutar las dependencias:
    - pip install -r requirements.txt

# Ejercicio 1

Ejecutar desde el directorio 1_recursion_and_colors el siguiente comando:

* python .\main.py

# Ejercicio 2

Ejecutar desde el directorio 2_file_handling_and_arrays_operations el siguiente comando:

* python .\main.py

# Ejercicio 3

Se debe de realizar la migracion mediante Alembic:
* en el directorio raiz 3_restful_api ejecutamos el comando inicial Alembic:
  * alembic init alembic
* generamos la revision de la migracion
  *  alembic revision --autogenerate -m "Descripción del cambio"
* y procedemos a hacer la actualizacion en base de dados
  * alembic upgrade head

Una vez realizada la migración procedemos a ejecutar el siguiente comando desde el directorio raiz 3_restful_api
* python .\main.py

Con esto ya se encontrará arriba la aplicacion y podemos probar con la documentación swagger donde se puede acceder a continuación:
* http://localhost:8000/docs