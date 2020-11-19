import re
import queue
import hashlib
diccionarioVariables=dict(nameVoid='void', nameString='string', nameFloat='float', nameInt='int')
diccionarioPalabraRe=dict(nameIf='if', nameWhile='while')
diccionarioCaracter=dict(mas='+', menos='-', punComa=';', asterisco='*', coma=',',
                         diago='/', igual='=', igualacion='==', diferente='!=', mener='<', menIgual='<=', mayIgual='>=',
                         mayor='>', parentesis=['(',')'], corchetes=['{','}'])

class Analizador:
    def __init__(self):
        self.nombre=""
        self.tipo=""
        self.identificador=""
        self.funcion=""

    def setNombre(self, nombre):
        self.nombre=nombre

    def setIdentificador(self, identificador):
        self.identificador=identificador

    def setTipo(self, tipo):
        self.tipo=tipo

    def setFuncion(self, funcion):
        self.funcion=funcion

    def getNombre(self):
        return self.nombre

    def getIdentificador(self):
        return self.identificador

    def getTipo(self):
        return self.tipo

    def getFuncion(self):
        return self.funcion

    def mostrar(self):
        var="Tipo: " + self.tipo + "\n" + "Nombre Variable: " + self.nombre + "\n" + "identificador: " + self.identificador + "Funcion: " + self.funcion
        return var

    def es_Variable(self, dato):
        for aux in diccionarioVariables:
            if diccionarioVariables[aux] == dato:
                return True
        return False
    def es_Palabra(self, dato):
        for aux in diccionarioPalabraRe:
            if diccionarioPalabraRe[aux] == dato:
                return True
        return False
    def es_Caracter(self,dato):
        for aux in diccionarioCaracter:
            if aux == "corchetes" or aux=="parentesis":
                if diccionarioCaracter[aux][0]==dato or diccionarioCaracter[aux][1]==dato:
                    return True
            if diccionarioCaracter[aux] == dato:
                return True
        return False
    def es_String(self, dato):
        return dato[0] == -30 and dato[dato.size() - 1] == -99 or dato[0] == 34 and dato[dato.size() - 1] == 34 or dato[0] == 39 and dato[dato.size() - 1] == 39;
    def es_Numero(self, dato):
        x=dato.isdigit()
        return x
    def funcion_hash(self,dato):
        pos = hashlib.sha1()
        pos.update(dato.encode('utf-8'))
        i = int(pos.hexdigest(),16)
        return pos.hexdigest()

    def recuperar_archivo(self):
        archivo = open("incorrecto.txt",'r', encoding="UTF8")
        for linea in archivo.readlines():
            lineas.append(linea)
        archivo.close()
        pilaClase = queue.LifoQueue()
        pilaString = queue.LifoQueue()
        diccionario = dict()
        num_linea = 1
       # for(pal1, )


if __name__ == '__main__':
    prueba1=Analizador()
    print(prueba1.es_Variable("string"))
    print(prueba1.es_Caracter("("))
    print(prueba1.es_Palabra("while"))
    print(prueba1.es_String('Hola'))
    print(prueba1.es_Numero("2"))
    print(prueba1.funcion_hash("Hola"))
    '''print(diccionarioPalabra['nameIf'])
    print(diccionarioVariables['nameInt'])
    print(diccionarioCaracter['mayor'])'''
