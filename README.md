# CAD_ARCGIS
Pruebas de conversión de DWG a SHAPEFILE.

Python 2.7

Si te refieres al directorio del script que se está ejecutando:
import os os.path.dirname(os.path.abspath(__file__)) 

Si te refieres al directorio de trabajo actual:
import os os.getcwd() 
Tenga en cuenta que antes y después del file hay dos guiones bajos, no solo uno.

Nota: También tenga en cuenta que si está ejecutando de forma interactiva o si ha cargado un código de algo que no sea un archivo (por ejemplo, una base de datos o un recurso en línea), no se puede configurar __file__ ya que no hay una noción de “archivo actual”. La respuesta anterior asume el escenario más común de ejecutar una secuencia de comandos de Python que está en un archivo.
