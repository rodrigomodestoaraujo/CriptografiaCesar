alfabeto = 'abcdefghijklmnopqrstuvwxyz'

def chave():
    z = int(input("chave: "))
    return z

def cipher(message, dir):
    m = ''
    chav = chave()
    for c in message:
        if c in alfabeto:
            c_index = alfabeto.index(c)
            m += alfabeto[(c_index + (dir * chav)) % len(alfabeto)]
        else:
            m += c
    return m

def esconde(message):
    message = message.lower()
    return cipher(message, 1)

def revela(message):
    message = message.lower()
    return cipher(message, -1)


r=1
while (r != 0):
    print("_____________________________________________________________________________")
    r = int(input("\n1 <- Criptografar\n2 <- Descriptografar\n0 <- Sair:\n\n--->  "))
    if (r ==1):
        m = input("\nFrase: ")
        f = (esconde(m))
        print("Criptografia: ", f)
    elif(r==2):
        m = input("\nFrase: ")
        f = (revela(m))
        print("Descriptografia: ", f)
    

    
