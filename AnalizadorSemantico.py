import ast

import item as item


class AnalizadorSemantico:
    # def __init__(self):


    def _lectura(self):
        array=[]
        file= 'Lectura.txt'
        with open (file) as f_obj:
            for line in f_obj:
                array.append(line)
        return array

    def leer(self):
        archivo = open("C:\PROYECTO\Proyecto-2--Estructuras-de-datos", 'r')
        texto = archivo.read()
        archivo.close()
        # convertir a diccionarioimport ast
        d1 = ast.literal_eval(texto)

        # Los diccionarios tienen estos metodos: keys() para obtener las claves, y values():for item in d1.keys():

        temp = ','.join(d1[item].keys())
        print(item, ":", temp)


if __name__ == '__main__':
    analizador = AnalizadorSemantico()
    analizador.leer()