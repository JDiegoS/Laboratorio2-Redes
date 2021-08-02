#Laboratorio 2
#Receptor

import bitarray
import socket

wordstocheck = ["A","Hola", "Mundo", "Cubo", "1234", "PalabraLarga", "Ricardo", "Diego", "Valenzuela", "Solorzano", "Redes"]

def recibir_cadena(cadena):
    print("\nEl mensaje recibido es: \n" + cadena)
    return

def recibir_cadena_segura(cadena, opt):
    if opt == True:
        print("--------Usando el Codigo de Hamming para corregir errores--------")
        size = len(cadena)
        check = BitsRedun(size)
        print("Se recibio:", cadena)
        correction = detectError(cadena, check)
        if correction == False:
            print("La cadena mandada no tiene errores")
            resultado = cadena.tobytes().decode('utf-8')
        else:
            correction = len(cadena)-correction
            print("Se encontro un error en la posicion:", str(correction))

            datoCorregir = cadena[correction]
            if datoCorregir == 1:
                cadena[correction] = 0
            else:
                cadena[correction] = 1
            
            print(cadena)
            resultado = cadena.tobytes().decode('utf-8')
    else:
        print("--------Usando Fletcher CheckSum para detectar errores--------")
        isIncorrect = True
        print(cadena)
        cadenaCheck = fletcher32(cadena.tobytes())
        for i in wordstocheck:
            if  cadenaCheck== fletcher32(bytes(i, 'utf-8')):
                isIncorrect = False
        
        if isIncorrect:
            resultado = "Se detecto error mediante Checksum: "+str(cadenaCheck)
        else:
            resultado = cadena.tobytes().decode('utf-8')
    return resultado

#Algoritmo de hamming para correcion de errores
def BitsRedun(size): 
    for i in range(size): 
        if(2**i >= size + i + 1): 
            return i

def detectError(bitr, nr): 
    n = len(bitr) 
    res = 0
    for i in range(nr): 
        val = 0
        for j in range(1, n + 1): 
            if(j &(2**i) == (2**i)): 
                val = val ^ int(bitr[-1 * j]) 
        res = res + val*(10**i)
        print(res)
    res = int(str(res), 2)
    print(res)
    if res == 0:
        return False
    else:
        return res

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
        print(data)
        a.frombytes(data)
        print(a)
        res = recibir_cadena_segura(a, isHamming)
        recibir_cadena(res)        
    # Close the connection with the client 
    c.close() 

