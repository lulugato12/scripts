## Actualizaciones
### Las actualizaciones son de la más reciente a la más antigua.

### **9 de diciembre, 2020**

1. Creación de ambiente virtual con Virtualenv. Como el sever tiene Python 2.7 y netZooPy requiere 3.5+.
2. Ejecución del ambiente con source.
3. Se instaló netZooPy directamente en el ambiente virtual.
4. Se enviaron los archivos para el algoritmo a través de ftp.
5. Se ejecutó el programa de Python dentro del ambiente virtual y se dejó ejecutando a través de screen.

Código para ejecutar el ambiente virutal

`$ virtualenv -p python 3 test`

`$ source test/bin/activate`

`(env) $ git clone https://github.com/netZoo/netZooPy.git`

`(env) $ cd netZooPy`

`(env) $ pip install -e .`

`(env) $ screen`

`(env) $ python main.py`
