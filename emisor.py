"""
LABORATORIO 2
Ricardo Valenzuela
Diego Solorzano
Codigo fuente para uso de sockets:
https://www.geeksforgeeks.org/socket-programming-python/"""

import bitarray
import random
import socket
from hamming import bitsRedun, posBitsRedun, pariBit

words = ["A","Hola", "Mundo", "Cubo", "PalabraLarga"]

def enviar_cadena():
    print("Los mensajes que puede mandar son:", words)

    inp = input("Del 1 al 5 que mensaje desea mandar:\n")
    if int(inp) > 0 & int(inp) < 5:
        inp = words[int(inp)-1]
    else:
        print("La opcion no existe")
    return inp

def verificacion(cadena):
    a = bitarray.bitarray()
    a.frombytes(cadena.encode('utf-8'))
    print(a)
    return a
    #Decode: print(a.tobytes().decode('utf-8'))

def ruido(bitar):
    b = bitarray.bitarray()
    for i in bitar:
        if random.random() < 0.05:
            if int(i) == 1:
                i = 0
            else:
                i = 1
            b.append(int(i))
        else:
            b.append(int(i))
    return b


# Create a socket object 
s = socket.socket()         
  
# Define the port on which you want to connect 
port = 12345                
  
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 

# receive data from the server 
print (s.recv(1024) )

#Get messages
print("""---------Seleccion de algoritmo---------
1. Correccion de errores - Codigo de Hamming
2. Deteccion de errores - Fletcher checksum""")
isHamming  = input("Seleccione su opcion:")

if isHamming == "1":
    messages = enviar_cadena()
    bitMess = verificacion(messages)
    m = len(bitMess)
    r = bitsRedun(m)
    arr = posBitsRedun(bitMess, r)
    arr = pariBit(arr, r)
    print("Hamming code:",arr)
    toSend = ruido(arr)
    print("Con ruido:", toSend)

elif isHamming == "2":
    messages = enviar_cadena()
    toSend = ruido(verificacion(messages))
else:
    print("dicha opcion no existe")
    quit()

# Send message
s.sendall(toSend)

# close the connection 
s.close()     
	
