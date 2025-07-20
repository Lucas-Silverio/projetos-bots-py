from animacao import Animacao
from comandos import *
import sys
def main():
    animacao = Animacao()
    animacao.iniciar()

    sys.stdout.write('\033[2J')
    sys.stdout.write('\033[3;0H')
    sys.stdout.flush()

    with open ('./arquivos/frases.txt', 'r', encoding='utf-8') as f:
        frases = [linha.strip() for linha in f]

    reservadas = ["sair","data","hora","pesquisar","frase","calculadora","desenhar"]

    while True:
        sys.stdout.write('\033[3;0H\033[J\033[?25h')
        sys.stdout.flush()
        entrada = input('Digite "ajuda" para mostrar todos os comandos. ').lower()

        if entrada == "sair":
            cmd_sair(animacao)
            break
        elif entrada == "frase":
            cmd_frase(animacao,frases)
        elif entrada == "data":
            cmd_data(animacao)
        elif entrada == "hora":
            cmd_hora(animacao)
        elif entrada == "pesquisar":
            cmd_pesquisar()
        elif entrada == "calculadora":
            cmd_calculadora()
        elif entrada == "desenhar":
            cmd_desenhar()
        elif entrada == "ajuda":
            cmd_ajuda(reservadas)
        else:
            print("Inválido")

if __name__ == "__main__":
    main()