#Benjamin Retamales - Valentina Valdivia

import socket
#maximo comun divisor ==1


#Leer archivo
def Leer(documento):
    archivo = open(documento,'r')
    lectura = archivo.read()
    archivo.close()
    return lectura
#escribir archivo  
def Escribir(nombre,cifrado):
    documento = open(nombre,'w')
    documento.write(cifrado)
    documento.close()
    return True


def client_program():
    
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    p = int(input('Ingrese un numero primo grande:\n --> '))
    q = int(input('Ingrese un numero alearotio\n -->  '))
    n = p*q
    nn = (p-1)*(q-1)
    print('nn = ')
    e = 0
    d = 0
    message = str(nn)
    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        e=int(data)
        print(e)
        d = pow(e,nn-2,nn)
        print(d)
        m = int(Leer('mensajeentrada.txt'))
        print(m)
        cifra = (m**e)//n
        print(cifra)
        desci = cifra**d//n
        print(desci)
        Escribir('mensajerecibido.txt', str(desci))
        print("Realizado")
        message='bye'

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
