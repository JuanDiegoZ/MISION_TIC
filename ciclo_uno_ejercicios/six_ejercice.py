list_abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def encriptar_caracter(caracter, b):
    for i in range(len(list_abc)): #Ciclo para encontrar el numero de letra a encriptar
        if caracter == list_abc[i]:
            numero_letra = i 

    numero_encriptado =(numero_letra + b )%27#Formula para encriptar el numero.   
    
    for i in range(len(list_abc)):#Ciclo el cual retorna la letra segun su indice dado por la formula de encriptacion
        if numero_encriptado == i:
            caracter_encriptado = list_abc[i]            
    
    
    return caracter_encriptado
    
def encriptar(mensaje, b):
    mensaje_encriptado = ""
    lista_mensaje = []
    for letter in mensaje:
        lista_mensaje.append(letter)

    for i in range(len(lista_mensaje)):
        if lista_mensaje[i] != " ":
            lista_mensaje[i] = encriptar_caracter(lista_mensaje[i],b)
        mensaje_encriptado += lista_mensaje[i]

    return mensaje_encriptado   
  
def desencriptar_caracter(caracter_encriptado, b):
    caracter_desencriptado = ""
    for i in range(len(list_abc)): #Ciclo para encontrar el numero de letra a encriptar
        if caracter_encriptado == list_abc[i]:
            numero_letra = i 

    numero_encriptado =(numero_letra - b )%27#Formula para encriptar el numero.   
    
    for i in range(len(list_abc)):#Ciclo el cual retorna la letra segun su indice dado por la formula de encriptacion
        if numero_encriptado == i:
            caracter_desencriptado = list_abc[i] 
    
    return caracter_desencriptado
    
def desencriptar(mensaje_encriptado, b):
    mensaje_desencriptado = ""
    lista_mensaje = []
    for letter in mensaje_encriptado:
        lista_mensaje.append(letter)

    for i in range(len(lista_mensaje)):
        if lista_mensaje[i] != " ":
            lista_mensaje[i] = desencriptar_caracter(lista_mensaje[i],b)
        mensaje_desencriptado += lista_mensaje[i]    
    
    return mensaje_desencriptado
    
  
