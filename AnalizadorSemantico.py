import ast
from distutils.command.config import config

import item as item
import re

class AnalizadorSemantico:
    def __init__(self):
        self.diccionario = {'key':{'int':{'nombre':[],'valor':[],'linea':[]}},'string':{'nombre':[],'valor':[],'linea':[]}
            ,'void':{'nombre':[],'inicio':[],'fin':[],'linea':[]},'float':{'nombre':[],'valor':[],'linea':[]},
                            'if':{'nombre':[],'inicio':[],'fin':[],'linea':[]},'while':{'nombre':[],'inicio':[],'fin':[],'linea':[]}}

    def _lectura(self):
        file='Lectura.txt'
        try:
            with open(file,'r',encoding="utf-8") as f_obj:
                for x in f_obj:
                    contenido = f_obj.readlines()
                    self.insertar(contenido)
        except FileNotFoundError:
            print("El archivo no existe")

    def insertar(self, datos):
        y=0
        for x in datos:
            secuencia=r'int'
            total=re.findall(secuencia, datos[y])
            if total:
                self.diccionario['key'][total.__getitem__(y)]
                print(total)  # busca en una linea la palabra que deseo
            else:
                secuencia=r'float'
                total=re.findall(secuencia, datos[y])
                if total:
                    self.diccionario['key'][total.__getitem__(y)]
                    print(total)  # busca en una linea la palabra que deseo
                else:
                    secuencia=r'string'
                    total=re.findall(secuencia, datos[y])
                    if total:
                        self.diccionario['key'][total.__getitem__(y)]
                        print(total)  # busca en una linea la palabra que deseo
                        exit()
            y+=1
        '''print(len(contenido))  # cuenta el total de lineas
        secuencia = r'int*'
        print(re.findall(secuencia,contenido[0]))#busca en una linea la palabra que deseo
        print(contenido[0])
        print(contenido)
        print(len(contenido))#cuenta el total de lineas
        print('x = x + 5' in contenido)#Busca si existe un elemento en el archivo
        print(contenido.index('x = x + 5'))#Trae el indice donde esta la palabra buscada
        print(contenido.count('x ='))#retorna el indice de coincidencias'''


if __name__ == '__main__':
    prueba = AnalizadorSemantico()
    prueba._lectura()