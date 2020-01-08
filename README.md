# CAD_ARCGIS
Pruebas de conversión de DWG a SHAPEFILE.

Python 2.7

Si te refieres al directorio del script que se está ejecutando:
import os os.path.dirname(os.path.abspath(__file__)) 

Si te refieres al directorio de trabajo actual:
import os os.getcwd() 
Tenga en cuenta que antes y después del file hay dos guiones bajos, no solo uno.

Nota: También tenga en cuenta que si está ejecutando de forma interactiva o si ha cargado un código de algo que no sea un archivo (por ejemplo, una base de datos o un recurso en línea), no se puede configurar __file__ ya que no hay una noción de “archivo actual”. La respuesta anterior asume el escenario más común de ejecutar una secuencia de comandos de Python que está en un archivo.

Apoyo:
- https://www.youtube.com/watch?v=i4lAEYQ_49w
- https://gis.stackexchange.com/questions/124987/add-cad-feature-class-to-arcgis-using-arcpy
- https://desktop.arcgis.com/es/arcmap/10.3/manage-data/cad/using-python-to-load-cad-data.htm
- https://pro.arcgis.com/es/pro-app/tool-reference/data-management/make-feature-layer.htm