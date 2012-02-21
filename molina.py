import sys
import math
import glob

def encuentra():
	listArchivos = []
	for nombreArchivo in glob.glob('/afs/ictp.it/home/m/mmolina/shellexample/thehackerwithin-PyTrieste-4f54727/shellExample/cleardata/*.txt'):
		listArchivos.append(nombreArchivo)
		
	return listArchivos
	
#print encuentra()


def buscaN(s):
	f = open(s, 'r')
	lineas= f.readlines()
	#print lineas[4]
	f.close()	
	return lineas[4].find('N')


def reemplazoArchivo():
	listArchivos=encuentra()
	for nombreArchivo in listArchivos:
		posi=buscaN(nombreArchivo)
		if posi!= -1:
			f = open(nombreArchivo, 'r')
			lineas= f.readlines()
			f.close()			
			lineas[4].replace('N','M')
			f=open(nombreArchivo,'w')
			for i in lineas:
				f.write(i)
			f.close()




		 

reemplazoArchivo()

#print buscaN('/afs/ictp.it/home/m/mmolina/shellexample/thehackerwithin-PyTrieste-4f54727/shellExample/cleardata/Data0559.txt')
