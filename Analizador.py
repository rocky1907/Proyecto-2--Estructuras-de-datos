from collections import deque
from queue import LifoQueue
import re
import queue
import hashlib

vector_tipos = ['void', 'string', 'float', 'int']
vector_sentencias_bucles = ['if', 'while']
vector_caracteres = ['+', '-', ';', '*', ',', '/', '=', '==', '!=', '<', '<=', '>=',
                          '>', '(', ')', '{', '}']


class Analizador:
    def __init__(self, tipo, nombre):
        self.nombre = nombre
        self.tipo = tipo
        self.identificador = ""
        self.funcion = ""

    def setNombre(self, nombre):
        self.nombre = nombre

    def setIdentificador(self, identificador):
        self.identificador = identificador

    def setTipo(self, tipo):
        self.tipo = tipo

    def setFuncion(self, funcion):
        self.funcion = funcion

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
        for aux in vector_tipos:
            if vector_tipos[aux] == dato:
                return True
        return False
    def es_Palabra(self, dato):
        for aux in vector_sentencias_bucles:
            if vector_sentencias_bucles[aux] == dato:
                return True
        return False
    def es_Caracter(self,dato):
        for aux in vector_caracteres:
            if aux == "corchetes" or aux=="parentesis":
                if vector_caracteres[aux][0]==dato or vector_caracteres[aux][1]==dato:
                    return True
            if vector_caracteres[aux] == dato:
                return True
        return False
    def es_String(self, dato):
        return dato[0] == -30 and dato[dato.size() - 1] == -99 or dato[0] == 34 and dato[dato.size() - 1] == 34 or dato[0] == 39 and dato[dato.size() - 1] == 39
    def es_Numero(self, dato):
        x=dato.isdigit()
        return x
    def funcion_hash(self,dato):
        pos = hashlib.sha1()
        pos.update(dato.encode('utf-8'))
        i = int(pos.hexdigest(),16)
        return pos.hexdigest()

    def recuperar_archivo(self):
        file='incorrecto.txt'
        try:
            with open(file, 'r', encoding="utf-8") as f_obj:
                for line in f_obj:
                    contenido=f_obj.readlines()
        except FileNotFoundError:
            print("El archivo no existe")
        f_obj.close()
        pilaClase=LifoQueue()
        pilaString=LifoQueue()
        diccionario=dict(int=Analizador)
        num_linea=1
        with open(file, 'r', encoding="utf-8") as f_obj:
            for line in f_obj:
                buffer = line
                for pal1 in buffer:
                    if pal1=="}":
                        pilaString.pop()
                    if pal1 == "if" or pal1 == "while":
                        v = Analizador(pal1,"indefinida")
                        v.setIdentificador("declaracion")
                        if pilaString:
                            v.setFuncion(pilaString.peek())
                        pilaClase.push(v)
                        pilaString.push(pal1)
                    if esVariable(pal1) or pal1 == "(":
                        if pal1 == "(":
                            if not pilaClase.isEmpty():
                                if pilaClase.peek().getIdentificador() != "declaracion":
                                    pilaClase.peek().setIdentificador("funcion")
                                    pilaString.push(pilaClase.peek().getNombre)
                                    diccionario.pop(funcion_hash(pilaClase.peek().getNombre))
                        else:
                            for pal2 in buffer:
                                a = Analizador(pal1,pal2)
                                if pilaString:
                                    a.setFuncion(pilaString.peek())
                                    if pal1 == "}":
                                        pilaString.pop()
                                a.setIdentificador("variable")
                                pilaClase.push(a)
                                diccionario.update({funcion_hash(a.getNombre())})
                    # elif:








if __name__ == '__main__':
    prueba1=Analizador("indefinido","statement")
    # print(prueba1.recuperar_archivo())
    '''print(prueba1.es_Variable("string"))
    print(prueba1.es_Caracter("("))
    print(prueba1.es_Palabra("while"))
    print(prueba1.es_String('Hola'))
    print(prueba1.es_Numero("2"))
    print(prueba1.funcion_hash("Hola"))
    print(diccionarioPalabra['nameIf'])
    print(vector_tipos['nameInt'])
    print(vector_caracteres['mayor'])'''
