from collections import deque
from enum import auto
from queue import LifoQueue
import re
import queue
import hashlib
import gothon as gothon
vector_tipos = ['void', 'string', 'float', 'int']
vector_sentencias_bucles = ['if', 'while']
vector_caracteres = ['+', '-', ';', '*', ',', '/', '=', '==', '!=', '<', '<=', '>=',
                          '>', '(', ')', '{', '}']

class Node:
    def __init__(self, value):
        self.value=value
        self.next=None


class Stack:

    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self):
        self.head=Node("head")
        self.size=0

    # String representation of the stack
    def __str__(self):
        cur=self.head.next
        out=""
        while cur:
            out+=str(cur.value) + "->"
            cur=cur.next
        return out[:-3]


    def getSize(self):
        return self.size

    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0

    def peek(self):

        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value

    def push(self, value):
        node=Node(value)
        node.next=self.head.next
        self.head.next=node
        self.size+=1

    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove=self.head.next
        self.head.next=self.head.next.next
        self.size-=1
        return remove.value


# Driver Code
if __name__ == "__main__":
    stack=Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")

    for _ in range(1, 6):
        remove=stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")


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
        i=0
        for aux in vector_tipos:
            if aux == dato:
                return True
        i+=1
        return False
    def es_Palabra(self, dato):
        i=0
        for aux in vector_sentencias_bucles:
            if vector_sentencias_bucles.__getitem__(i) == dato:
                return True
        i=i+1
        return False
    def es_Caracter(self,dato):
        i=0
        for aux in vector_caracteres:
            if aux == "corchetes" or aux=="parentesis":
                if vector_caracteres.__getitem__(i) is dato or vector_caracteres.__getitem__(i) is dato:
                    return True
            if vector_caracteres.__getitem__(i) is dato:
                return True
            i=i+1
        return False
    def es_String(self, s):
        x=(s[0] == -30 and s[s.__sizeof__() - 1] == -99 or s[0] == 34 and s[s.__sizeof__() - 1] == 34 or s[0] == 39and s[s.__sizeof__() - 1] == 39)
        return s
    def es_Numero(self, dato):
        x=dato.isdigit()
        return x
    def funcion_hash(self,dato):
        pos = hashlib.sha1()
        pos.update(dato[1].encode('utf-8'))
        #i = int(pos.hexdigest(),16)
        return pos.hexdigest()

    def recuperar_archivo(self):
        file='incorrecto.txt'
        try:
            with open(file, 'r', encoding="utf-8") as f_obj:
                for line in f_obj:
                    contenido=f_obj.readlines()
        except FileNotFoundError:
            print("El archivo no existe")
        lista =[]
        f_obj.close()
        pilaClase=Stack()
        pilaString=Stack()
        diccionario=dict()
        num_linea=1
        pal2 = "vacio"
        with open(file, 'r', encoding="utf-8") as f_obj:
            for line in f_obj:
                buffer = line
                for pal1 in buffer.split(" "):
                    if pal1 == "\n":
                        num_linea=num_linea + 1
                        break
                    if pal2 != pal1 and pal1 !="":
                        if pal1 == "}":
                            pilaString.pop()
                        if pal1 == "if" or pal1 == "while":
                            v = Analizador(pal1,"indefinida")
                            v.setIdentificador("declaracion")
                            if not pilaString.isEmpty():
                                v.setFuncion(pilaString.peek())
                            pilaClase.push(v)
                            pilaString.push(pal1)
                        if self.es_Variable(pal1) or pal1 is "(":
                            if pal1 == "(":
                                if not pilaClase.isEmpty():
                                    if pilaClase.peek() != "funcion":
                                        pilaString.push(pilaClase.peek().getNombre)
                                        diccionario.pop(self.funcion_hash(pilaClase.peek().getNombre))
                            else:
                                for aux2 in buffer.split(" "):
                                    if pal1==aux2 or aux2 =="":
                                        aux2=aux2
                                    else:
                                        pal2=aux2
                                        break
                                a = Analizador(pal1,pal2)
                                if not pilaString.isEmpty():
                                    a.setFuncion(pilaString.peek())
                                    if pal1 == "}":
                                        pilaString.pop()
                                a.setIdentificador("variable")
                                pilaClase.push(a)
                                x=self.funcion_hash(a.getNombre())
                                diccionario[self.funcion_hash(a.getNombre())] = [a.getNombre(),a.getTipo(),a.getIdentificador(),a.getFuncion()]
                        elif self.es_Caracter(pal1) != True and  self.es_Numero(pal1)  != True and  self.es_Palabra(pal1) != True and  self.es_String(pal1) != True:
                            '''diccionario_iterador = dict(int = Analizador)
                            diccionario_iterador = diccionario.get(self.funcion_hash(pal1))
                            if diccionario_iterador == len(diccionario)-1 :'''
                            try:
                                bandera = False
                                lista=list(diccionario.keys())
                                for elemento in lista:
                                    if elemento == self.funcion_hash(pal1):
                                        bandera = True
                                if bandera == False:

                                    print("Error en linea" + str(num_linea) + ":" + pal1 + "---no esta declarado(a)---")
                            except FileNotFoundError:
                                print("Error en linea" + num_linea + ":" + pal1 + "---no esta declarado(a)---")




if __name__ == '__main__':
    prueba1=Analizador("indefinido","statement")
    #prueba1.es_String("(n")
    print(prueba1.recuperar_archivo())
    '''print(prueba1.es_Variable("string"))
    print(prueba1.es_Caracter("("))
    print(prueba1.es_Palabra("while"))
    print(prueba1.es_String('Hola'))
    print(prueba1.es_Numero("2"))
    print(prueba1.funcion_hash("Hola"))
    print(diccionarioPalabra['nameIf'])
    print(vector_tipos['nameInt'])
    print(vector_caracteres['mayor'])'''
