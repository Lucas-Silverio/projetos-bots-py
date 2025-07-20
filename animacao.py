import threading
import os
import time
import sys
import random
class Animacao():
    def __init__(self):
        self.animando_event = threading.Event()
        self.ativo_event = threading.Event()
        self.animando_event.set()
        self.ativo_event.set()
        self.thread = threading.Thread(target=self.animacao_start)
        self.frames = ['(ô - ô)','(õ - õ)','(ㆆ - ㆆ)','(ó - ò)','(ò - ó)','(v - v)','(x - x)', '(e - e)','(T - T)','(º - º)','(° - °)','(õ ~ õ)','(︶︹︶)','(õ _ o)','(. _ .)','(・ _ ・)','(- _ -)','(ô ‿ ô)','(ó ‿ ò)','(õ ‿ õ)']
    def iniciar(self):
        self.thread.start() 
    def parar(self):
        self.ativo_event.clear()
        self.animando_event.clear()
        self.thread.join()
        self.animacao_stop()
        time.sleep(2)
        os.system('clear')
    def animacao_response(self,resposta,tempo=1):
        self.ativo_event.clear()
        sys.stdout.write('\033[s\033[?25l')
        self.animar_frame('(ô o ô) '+resposta)
        sys.stdout.flush()
        time.sleep(1)
        self.animar_frame('(ô ‿ ô) '+resposta)
        sys.stdout.flush()
        time.sleep(tempo)
        self.animar_frame('(õ ‿ õ)')
        sys.stdout.flush()
        time.sleep(1)
        sys.stdout.write('\033[u\033[?25h')
        self.ativo_event.set()
    def animar_frame(self,texto):
        sys.stdout.write("\033[1;0H\033[?25l\033[K")
        sys.stdout.write(texto)
        sys.stdout.flush()
    def animacao_stop(self):
        sys.stdout.write('\033[2J')
        sys.stdout.flush()
        self.animar_frame("(╥ ﹏ ╥) Até mais amigo.")
        sys.stdout.flush()
    def animacao_start(self):
        while self.animando_event.is_set():
            self.ativo_event.wait()
            rd = random.randint(0,len(self.frames)-1)
            sys.stdout.write('\033[s\033[?25l')
            sys.stdout.flush()
            self.animar_frame(self.frames[rd])
            sys.stdout.write('\033[u\033[?25h')
            sys.stdout.flush()
            time.sleep(1.8)