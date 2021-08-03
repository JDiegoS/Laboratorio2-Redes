
"""
LABORATORIO 2
Ricardo Valenzuela
Diego Solorzano
Codigo fuente de:
https://www.geeksforgeeks.org/hamming-code-implementation-in-python/"""


#Algoritmo de hamming para correcion de errores
def bitsRedun(size): 
    for i in range(size):
        if(2**i >= size + i + 1):
            return i

def posBitsRedun(bitArr, r): 
    j = 0
    k = 1
    m = len(bitArr)
    res = ''
 
    for i in range(1, m + r+1):
        if(i == 2**j):
            res = res + '0'
            j += 1
        else:
            res = res + str(bitArr[-1 * k])
            k += 1
    res = res[::-1]  
    return res

def pariBit(bitArr, r):
    n = len(bitArr)
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if(j & (2**i) == (2**i)):
                val = val ^ int(bitArr[-1 * j])
        bitArr = bitArr[:n-(2**i)] + str(val) + bitArr[n-(2**i)+1:]
    return bitArr


def detectError(bitr, nr): 
    n = len(bitr) 
    res = 0
    for i in range(nr): 
        val = 0
        for j in range(1, n + 1): 
            if(j &(2**i) == (2**i)): 
                val = val ^ int(bitr[-1 * j]) 
        res = res + val*(10**i)
    res = int(str(res), 2)
    if res == 0:
        return False
    else:
        return res