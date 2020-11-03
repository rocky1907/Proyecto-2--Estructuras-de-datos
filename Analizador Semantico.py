import hashlib
class Analizador_Semantico:
    def generator_Hash(self, h):
        digest = h.hexdigest()
        return digest

    def algorithm_funtion(self, algorithm_number, data):
        algorithm =""
        if algorithm_number !=3:
            if algorithm_number == 1:
                '''El sha256 es la longitud de bytes que tendra el hash'''
                algorithm = "sha256"
            if algorithm_number == 2:
                '''El sha512 es la longitud de bytes que tendra el hash'''
                algorithm = "sha512"
            bdata = bytes(data,'utf-8')
            h = hashlib.new(algorithm,bdata)
            _hash = self.generator_Hash(h)
            print(_hash)

if __name__ == '__main__':
    x=0
    prueba = Analizador_Semantico()
    prueba.algorithm_funtion(2,"while")

