def classificar_numero(numero):
    if numero < 0:
        return "negativo!"
    elif numero > 0:
        return "positivo!"
    else:
        return
    
def main():
    positivos = 0
    negativos = 0
    
    while True:
        numero = int(input())
        
        if numero == 0:
            break 

        print(classificar_numero(numero))
        
        if classificar_numero(numero) == "positivo!":
            positivos += 1
        elif classificar_numero(numero) == "negativo!":
            negativos += 1
     
    print(f"{positivos} números positivos, {negativos} números negativos")

if __name__ == "__main__":
    main()