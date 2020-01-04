#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import csv
from openpyxl import Workbook
from os import listdir
from os.path import isfile, join

count = 0
pathWord = r'D:\RepositorioGitLab\Frontend\Electron\data_source\ASCII'
pathCSV = r'D:\RepositorioGitLab\Frontend\Electron\xlsx'

# Lista los archivos de la carpeta
def dataSource(ruta = '.'):
    return listdir(ruta)

# Valida si es número o no
def isNumber(param_in):
    try:
        float(param_in)
        return True
    except ValueError:
        return False

# Eliminar archivos de procesamiento.
def deleteFiles(folder):
	files_dump = [join(folder, c) for c in listdir(folder)]
	files_dump = filter(lambda c: isfile(c), files_dump)
	[os.remove(c) for c in files_dump]

# Configurando EXCEL
wb = Workbook()
ws = wb.active
ws.sheet_properties.tabColor = "1072BA"

# Antes de entrar a la ruta se tiene que verificar si existe
if (os.path.exists(pathWord)):
	deleteFiles(pathCSV)
	outDir = dataSource(pathWord)
	for infile in outDir:
		inPath = os.path.join(pathWord, infile)
		print inPath

		# Validamos la existencia si el archivo tiene alguna información
		if os.stat(inPath).st_size == 0 :
			print "Archivo vacio: {0}".format(infile)
		else:
			count = count + 1			
			with open(inPath,'r') as file:
				for line in file:
					lineArr = line.split()
					ws.title = infile
					if isNumber(lineArr[0]) and isNumber(lineArr[1]):
						ws.append([lineArr[0], lineArr[1]])
					else:
						ws.append(['X', 'Y'])
			file.close()
			wb.save(os.path.join(pathCSV, "{0}.xlsx".format(infile)))
			
		# Porcentaje de archivos procesados
		percentage = (count*100)/len(outDir)
		print "{0}%".format(percentage)
	# fileTxt = ls(pathWord)
	# print pathWord+""+fileTxt
else:
	print "No existe RUTA"