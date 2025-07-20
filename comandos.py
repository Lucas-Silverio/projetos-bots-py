import sys
import time
import random
import webbrowser
import datetime
import os
def cmd_frase(animacao,frases):
        nmr = random.randint(0,len(frases)-1)
        resposta = frases[nmr]
        animacao.animacao_response(resposta,3)
        time.sleep(1)
def cmd_pesquisar():
        sys.stdout.write('\033[3;0H\033[K\033[?25h')
        sys.stdout.flush()
        pesquisa = input("O que você quer pesquisar ? ")
        url = f"https://www.google.com/search?q={pesquisa.replace(' ','+')}"
        webbrowser.open(url)
def cmd_ajuda(reservadas):
        sys.stdout.write('\033[4;0H\033[K\033[?25l')
        sys.stdout.write('Comandos: '+', '.join(reservadas)+' '* 10 +'\n')
        sys.stdout.flush()
        time.sleep(4)
        sys.stdout.write('\033[4;0H\033[J')
def cmd_data(animacao):
        data_formatada = datetime.datetime.now().strftime("dia %d do %m de %Y.")
        resposta = 'Hoje é '+data_formatada+''
        animacao.animacao_response(resposta)
        time.sleep(1)
def cmd_hora(animacao):
        hora_formatada = datetime.datetime.now().strftime("%H horas e %M minutos.")
        resposta = 'Agora são '+hora_formatada+''
        animacao.animacao_response(resposta)
        time.sleep(1)
def cmd_sair(animacao):
        animacao.parar()
def cmd_desenhar():
        os.system("mspaint")
def cmd_calculadora():
        os.system("calc.exe")