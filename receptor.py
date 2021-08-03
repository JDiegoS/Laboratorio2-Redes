"""
LABORATORIO 2
Ricardo Valenzuela
Diego Solorzano
Codigo fuente para uso de sockets:
https://www.geeksforgeeks.org/hamming-code-implementation-in-python/"""

import bitarray
import socket
from hamming import bitsRedun, detectError

wordstocheck = ["A","Hola", "Mundo", "Cubo", "PalabraLarga"]

def recibir_cadena(cadena):
    if cadena == False:
        print("Detecto un error en la cadena recibida")
    else:
        print("El mensaje recibido es:", cadena)
    return

def recibir_cadena_segura(cadena, opt):
    if opt == True:
        print("--------Usando el Codigo de Hamming para corregir errores--------")
        if len(cadena) == 16:
            cadena = cadena[:-4]
        elif len(cadena)<100:
            cadena = cadena[:-2]
        else:
            cadena = cadena[:-1]
        print("El codigo hamming recibido es:",cadena)

        words = wordstocheck
        words.reverse()
        error = False
        for i in words:
            a = bitarray.bitarray()
            a.frombytes(i.encode('utf-8'))
            m = bitsRedun(len(a))
            error = detectError(cadena, m)
            if error != False:
                break
        if error != False:
            print("Se encontro error en el bit", len(cadena)-error)
            resultado = False
        else:
            print("No hay error en el codigo Hamming")
            resultado = cadena


    else:
        print("--------Usando Fletcher CheckSum para detectar errores--------")
        isIncorrect = True
        cadenaCheck = fletcher32(cadena.tobytes())
        for i in wordstocheck:
            if  cadenaCheck== fletcher32(bytes(i, 'utf-8')):
                isIncorrect = False
        
        if isIncorrect:
            resultado = False
        else:
            resultado = cadena.tobytes().decode('utf-8')
    return resultado



#Checksum para deteccion de errores -- version de 32 bits
def fletcher32(data):
    sum1 = int()
    sum2 = int()
    for index in range(len(data)):
        sum1 = (sum1 + data[index]) % 65535
        sum2 = (sum2 + sum1) % 65535
    result = (sum2 << 16) | sum1
    return result


#------------------------------Main---------------------------------------
#Confirguracion paso de informacion
#socket
s = socket.socket()         
print ("Socket successfully created")

port = 12345

s.bind(('', port))         
print ("socket binded to %s" %(port)) 
  
# put the socket into listening mode 
s.listen(5)     
print ("socket is listening")            
  
print("""---------Seleccion de algoritmo---------
1. Correccion de errores - Codigo de Hamming
2. Deteccion de errores - Fletcher checksum""")
isHamming  = input("Seleccione su opcion:")

if isHamming == "1":
    isHamming = True

elif isHamming == "2":
    isHamming = False
else:
    print("dicha opcion no existe")
    quit()

print("Listo para recibir mensajes")

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
        a = bitarray.bitarray()
        a.frombytes(data)
        res = recibir_cadena_segura(a, isHamming)
        recibir_cadena(res)        
    # Close the connection with the client 
    c.close() 

