#Laboratorio 2
#Receptor

import bitarray
import socket

def recibir_cadena(cadena):
    print("\nEl mensaje recibido es: \n" + cadena)
    return

def recibir_cadena_segura(cadena):
    resultado = cadena.decode('utf-8')
    return resultado


#socket
s = socket.socket()         
print ("Socket successfully created")

port = 12345

s.bind(('', port))         
print ("socket binded to %s" %(port)) 
  
# put the socket into listening mode 
s.listen(5)     
print ("socket is listening")            
  
# a forever loop until we interrupt it or 
# an error occurs 
while True: 
  
    # Establish connection with client. 
    c, addr = s.accept()     
    print ('Got connection from', addr )
    
    # send a thank you message to the client. 
    c.send('Thank you for connecting'.encode('utf-8')) 
    
    while True:
        data = c.recv(1024)
        if not data: break
        res = recibir_cadena_segura(data)
        recibir_cadena(res)        
    # Close the connection with the client 
    c.close() 

