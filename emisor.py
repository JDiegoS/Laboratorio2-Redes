import bitarray
import random
import socket


def enviar_cadena():
    inp = input("Mensaje a enviar:\n")
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
            if i == 1:
                i = 0
            else:
                i = 1
            b.append(i)
        else:
            b.append(i)
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
messages = enviar_cadena()
toSend = ruido(verificacion(messages))
# Send message
s.sendall(toSend)

# close the connection 
s.close()     
	
