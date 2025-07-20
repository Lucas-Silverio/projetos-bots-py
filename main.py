import threading
import os
import sys
import time
import datetime
import webbrowser
import random

#VARIAVEIS
with open("./arquivos/frases.txt", "r",encoding= "utf-8") as f:
    frases = [frase.strip() for frase in f]
reservadas = ["sair","data","hora","pesquisar","frase","calculadora","desenhar"]

#EVENTOS 
animando_evento = threading.Event()
animando_evento.set()
funcionando_evento = threading.Event()
funcionando_evento.set()

#Animações
def animar():
    frames = ['(ô - ô)','(õ - õ)','(ㆆ - ㆆ)','(ó - ò)','(ò - ó)','(v - v)','(x - x)', '(e - e)','(T - T)','(º - º)','(° - °)','(õ ~ õ)','(︶︹︶)','(õ _ o)','(. _ .)','(・ _ ・)','(- _ -)','(ô ‿ ô)','(ó ‿ ò)','(õ ‿ õ)']
    while animando_evento.is_set():
        funcionando_evento.wait()
        rd = random.randint(0,len(frames)-1)
        sys.stdout.write('\033[s\033[?25l')
        sys.stdout.flush()
        animar_frame(frames[rd])
        sys.stdout.write('\033[u\033[?25h')
        sys.stdout.flush()
        time.sleep(1.8)
        
def animar_frame(texto):
    sys.stdout.write("\033[1;0H\033[?25l\033[K")
    sys.stdout.write(texto)
    sys.stdout.flush()
def animacao_sair():
    sys.stdout.write('\033[2J')
    sys.stdout.flush()
    animar_frame("(╥ ﹏ ╥) Até mais amigo.")
    sys.stdout.flush()
def animacao_resposta(resposta,tempo=1):
    funcionando_evento.clear()
    sys.stdout.write('\033[s\033[?25l')
    animar_frame('(ô o ô) '+resposta)
    sys.stdout.flush()
    time.sleep(1)
    animar_frame('(ô ‿ ô) '+resposta)
    sys.stdout.flush()
    time.sleep(tempo)
    animar_frame('(õ ‿ õ)')
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.write('\033[u\033[?25h')
    funcionando_evento.set()

#PRINCIPAL
def main():
    #Limpa a tela inicialmente e posciona o cursor
    sys.stdout.write('\033[2J')
    sys.stdout.write('\033[3;0H')
    sys.stdout.flush()

    #Cria a thread da animação
    thread = threading.Thread(target=animar)
    thread.start()
    
    #Loop no evento de animação
    while animando_evento.is_set():
        sys.stdout.write('\033[3;0H\033[J\033[?25h')
        sys.stdout.flush()
        entrada = input('Digite "ajuda" para saber os comandos disponiveis. ')

        #Comando de Frases
        if entrada.lower() == "frase":
            nmr = random.randint(0,len(frases)-1)
            resposta = frases[nmr]
            animacao_resposta(resposta,3)
            time.sleep(1)
        #Comando de Pesquisa
        if entrada.lower() == "pesquisar":
            sys.stdout.write('\033[3;0H\033[K\033[?25h')
            sys.stdout.flush()
            pesquisa = input("O que você quer pesquisar ? ")
            url = f"https://www.google.com/search?q={pesquisa.replace(' ','+')}"
            webbrowser.open(url)
        #Comando de Paint
        if entrada.lower() == "desenhar":
            os.system("mspaint")
        #Comando de Calculadora
        if entrada.lower() == "calculadora":
            os.system("calc.exe")
        #Comando de Data
        if entrada.lower() == "data":
            data_formatada = datetime.datetime.now().strftime("dia %d do %m de %Y.")
            resposta = 'Hoje é '+data_formatada+''
            animacao_resposta(resposta)
            time.sleep(1)
        #Comando de Hora
        if entrada.lower() == "hora":
            hora_formatada = datetime.datetime.now().strftime("%H horas e %M minutos.")
            resposta = 'Agora são '+hora_formatada+''
            animacao_resposta(resposta)
            time.sleep(1)
        #Comando de Ajuda
        if entrada.lower() == "ajuda":
            sys.stdout.write('\033[4;0H\033[K\033[?25l')
            sys.stdout.write('Comandos: '+', '.join(reservadas)+' '* 10 +'\n')
            sys.stdout.flush()
            time.sleep(4)
            sys.stdout.write('\033[4;0H\033[J')
        #Comando de Sair
        if entrada.lower() == "sair":
            #limpando eventos
            animando_evento.clear()
            funcionando_evento.clear()
            thread.join()
            animacao_sair()
            #tempo para mostrar o frame de saida e limpeza do terminal
            time.sleep(2)
            os.system('clear')
            break

if __name__ == "__main__":
    main()