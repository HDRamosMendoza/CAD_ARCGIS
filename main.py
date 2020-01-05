#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from os import listdir
import arcpy

pathDWG = r'D:\RepositorioGitHub\CAD_ARCGIS\DWG'
prj = r'D:\RepositorioGitHub\CAD_ARCGIS/PRJ\WGS84_18S.prj'

# Lista los archivos de la carpeta
def dataSource(ruta = '.'):
    return listdir(ruta)

'''
# Eliminar archivos de procesamiento.
def deleteFiles(folder):
	files_dump = [join(folder, c) for c in listdir(folder)]
	files_dump = filter(lambda c: isfile(c), files_dump)
	[os.remove(c) for c in files_dump]
'''

arcpy.env.workspace = "D:\RepositorioGitHub\CAD_ARCGIS"
arcpy.env.overwriteOutput = True

count = 0
#input_cad = r"D:\RepositorioGitHub\CAD_ARCGIS\DWG\3101009011.dwg"
out_geodatabase = "Demo.gdb"


scale = "1000"

# Execute CreateFeaturedataset
#arcpy.CadToGeodatabase_conversion(input_cad_dataset, out_gdb_path, out_dataset_name, reference_scale)
#arcpy.CreateFileGDB_management("C:/output", "HabitatAnalysis.gdb")
'''
arcpy.CADToGeodatabase_conversion(
    input_cad,
    out_geodatabase,
    out_dataSet,
    scale,
    prj
)
'''
# Antes de entrar a la ruta se tiene que verificar si existe
if (os.path.exists(pathDWG)):
    # deleteFiles(pathCSV)
    outDir = dataSource(pathDWG)
    for infile in outDir:
        count = count + 1
        # path DWG
        input_cad = os.path.join(pathDWG, infile)
        desc = arcpy.Describe(input_cad)
        #print("Name: {}".format(desc.name))
        #print("File {}".format(desc.file))
        #print("Extension {}".format(desc.extension))
        nameDataSet_CAD = "MSI_"+ desc.name.replace("."+ desc.extension, "").replace(" ", "").replace("-", "")
        #for child in desc.children:
        #print "\t%s = %s" % (child.name, child.dataType)
        print(nameDataSet_CAD)
        out_dataSet = nameDataSet_CAD
        arcpy.CADToGeodatabase_conversion(
            os.path.abspath(input_cad),
            out_geodatabase,
            out_dataSet,
            scale,
            prj
        )

        # Validamos la existencia si el archivo tiene alguna información
        #if os.stat(inPath).st_size == 0:
        #print("Archivo vacio: {0}".format(infile))

        # Porcentaje de archivos procesados
        percentage = (count*100)/len(outDir)
        print("{0}%".format(percentage))

    # fileTxt = ls(pathWord)
    # print pathWord+""+fileTxt
else:
    print("No existe RUTA")