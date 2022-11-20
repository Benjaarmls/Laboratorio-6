
import socket
def mcdU(a):
    mcd=0
    i = 0
    for e in range(a):
        if i !=1:
            while e!=0:
                i = e
                e=a%e
                a = i
        else:
            mcd=e
            e=a
    return mcd

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode() #mensaje recibido
        data = int(data)
        data = mcdU(data)
        data=str(data)
        print(data)
        if not data:
            # if data is not received break
            break

        conn.send(data.encode())  # envia mensaje al cliente

    conn.close()  # cierra coneción


if __name__ == '__main__':
    server_program()