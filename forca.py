
def jogar():
    print ("////////////////////////////////////////")
    print ("***Bem vindo no jogo de forca!***")
    print ("////////////////////////////////////////")

    import random

    palavras = ["python", "desenvolvimento", "computador", "algoritmo", "programacao"]

    def escolher_palavra():
        return random.choice(palavras)

    def jogar_forca():
        print("Bem-vindo ao Jogo da Forca!")
    
    palavra = escolher_palavra()
    letras_adivinhadas = []  
    chances = 6 
    letras_corretas = ['_' for _ in palavra]  

    while chances > 0:
        print("\nPalavra:", ' '.join(letras_corretas))
        print(f"Chances restantes: {chances}")
        print(f"Letras adivinhadas: {' '.join(letras_adivinhadas)}")

        tentativa = input("Adivinhe uma letra: ").lower()

        if tentativa in letras_adivinhadas:
            print("Você já adivinhou essa letra.")
            continue

        letras_adivinhadas.append(tentativa)

        if tentativa in palavra:
            for index, letra in enumerate(palavra):
                if letra == tentativa:
                    letras_corretas[index] = tentativa
        else:
            print(f"A letra '{tentativa}' não está na palavra.")
            chances -= 1

        if '_' not in letras_corretas:
            print(f"\nParabéns, você ganhou! A palavra era '{palavra}'.")
            break
    else:
        print(f"\nFim de jogo! Você perdeu. A palavra era '{palavra}'.")

    jogar_forca()


    print ("Fim do jogo!")
    

if(__name__=="__main__"):
    jogar()




