#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from os import listdir
import arcpy

pathWorkspace = os.getcwd()
arcpy.env.workspace = pathWorkspace
arcpy.env.overwriteOutput = True
pathDWG = os.path.join(pathWorkspace,'DWG')
psthSR = os.path.join(pathWorkspace,'PRJ\WGS84_18S.prj')

# Lista los archivos de la carpeta
def dataSource(ruta = '.'):
    return listdir(ruta)

# Eliminar archivos de procesamiento.
def deleteFiles(folder):
	files_dump = [join(folder, c) for c in listdir(folder)]
	files_dump = filter(lambda c: isfile(c), files_dump)
	[os.remove(c) for c in files_dump]

count = 0
#input_cad = r"D:\RepositorioGitHub\CAD_ARCGIS\DWG\3101009011.dwg"
out_geodatabase = "GDB\DWG_TO_SHP.gdb"
scale = "1000"

# Execute CreateFeaturedataset
#arcpy.CadToGeodatabase_conversion(input_cad_dataset, out_gdb_path, out_dataset_name, reference_scale)
#arcpy.CreateFileGDB_management("C:/output", "HabitatAnalysis.gdb")
try:
    # Consulta si existe el MXD
    if arcpy.Exists("MXD\\DWG_TO_SHP.mxd"):
        print("Existe el MXD")
        # Antes de entrar a la ruta se tiene que verificar si existe
        if (os.path.exists(pathDWG)):
            print("Entro")
            # deleteFiles(pathCSV)
            outDir = dataSource(pathDWG)
            for infile in outDir:
                count = count + 1
                # path DWG
                input_FileCAD = os.path.join(pathDWG, infile)
                desc_CAD = arcpy.Describe(input_FileCAD)
                
                #print("File {}".format(desc.file))
                print("Por crear el nombre")
                # New name - DWG
                out_dataSet_name_CAD = "MSI_"+ desc_CAD.name.replace("."+ desc_CAD.extension, "").replace(" ", "").replace("-", "")
                print(desc_CAD.spatialReference.name)
                # Spatial Reference == "unknown"
                if desc_CAD.spatialReference.name == "Unknown":
                    print("{0} no tiene referencial espacial o se desconoce".format(desc_CAD.name))

                    # Assign spatial reference
                    arcpy.DefineProjection_management(input_FileCAD, psthSR)

                # Spatial Reference
                else:

                    print("{0} : {1}".format(desc_CAD.name, desc_CAD.spatialReference.name))

                #for child in desc.children:
                #print "\t%s = %s" % (child.name, child.dataType)
                #arcpy.Describe(fc).spatialReference

                
                '''
                arcpy.CADToGeodatabase_conversion(
                    input_cad_datasets  = os.path.abspath(input_cad),
                    out_gdb_path        = out_geodatabase,
                    out_dataset_name    = out_dataSet_name_CAD,
                    reference_scale     = scale,
                    spatial_reference   = prj
                )
                '''

                # Validamos la existencia si el archivo tiene alguna información
                #if os.stat(inPath).st_size == 0:
                #print("Archivo vacio: {0}".format(infile))

                # Porcentaje de archivos procesados
                percentage = (count*100)/len(outDir)
                print("Procesando {0}%".format(percentage))

            # fileTxt = ls(pathWord)
            # print pathWord+""+fileTxt
        else:
            print("No existe RUTA")
    else:
        print("Se debe de crear el MXD")
except:
    print arcpy.GetMessages()