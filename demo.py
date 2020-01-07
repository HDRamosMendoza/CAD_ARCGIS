#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from os import listdir
import arcpy

pathWorkspace = os.getcwd()
arcpy.env.workspace = pathWorkspace
arcpy.env.overwriteOutput = True
path_mapDocumentos = os.path.join(pathWorkspace,'MXD\\DWG_TO_SHP.mxd')

try:
    print(path_mapDocumentos)
    # Document MXD
    mxd = arcpy.mapping.MapDocument(path_mapDocumentos)
    # Setting up MXD
    mxd.title           = "Automatización DWG to SHP"
    mxd.author          = "Ing. Heber Daniel Ramos Mendoza"
    mxd.summary         = "Automatización de proceso de referenciazción de DWG  a SHAPEFILE"
    mxd.description     = "Automatizar proceso de  referenciazción de DWG a SHAPEFILE. Este proceso se da en la Subgerencia de Planeamiento Urbano y Catastro"
    mxd.credits         = "HDRamosMendoza - Ing. Heber Daniel Ramos Mendoza"
    mxd.tags            = "HDRamosMendoza, MarkGIS"
    mxd.hyperlinkBase   = "https://hdramosmendoza.github.io/Perfil-Profesional/"
    mxd.save()

    # Obtener el marco de datos
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    df.elementPositionX, df.elementPositionY = 0.5,0.5
    df.elementWidth = 15
    df.elementHeight = 25

    # Creamos nueva capa
    lyrDWG = arcpy.mapping.Layer(os.path.join(pathWorkspace,'DWG\\3101009011.dwg'))

    # Agregue la capa al mapa en la parte inferior de la tabla de contenido en el marco de datos 0
    arcpy.mapping.AddLayer(df, lyrDWG,"BOTTOM")
    arcpy.RefreshActiveView()
    mxd.save()

    '''
    mxd = arcpy.mapping.MapDocument("CURRENT")
    df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
    addPoint = arcpy.mapping.Layer(r"C:\Temp\my.dwg\Point") # reference to point layer
    addPolyline = arcpy.mapping.Layer(r"C:\Temp\my.dwg\Polyline") # reference to Polyline layer
    arcpy.mapping.AddLayer(df, addPoint, "BOTTOM")
    arcpy.mapping.AddLayer(df, addPolyline, "BOTTOM")
    '''
    
except:
    print arcpy.GetMessages()