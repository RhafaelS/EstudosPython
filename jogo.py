import random 
import os
import time

class Carro(object):
    def __init__(self, modelo, mim, max):
        self.__modelo = modelo
        self.__max = max
        self.__mim = mim
        self.__velo_atual = 0
    
    @property
    def modelo(self):
        return self.__modelo
    
    @property
    def modelo(self):
        return self.__velo_atual

    @property
    def modelo(self):
        return self.__max
    
    @property
    def modelo(self):
        return self.__mim
    
    def andar(self):
        return random.randint(self.__mim, self.__max)

def corrida(p1, p2):
    print('0----------1000')
    if p1 > p2:
        print('1 em primeiro {}'.format(p1))
        print('2 em segundo {}'.format(p2))
    else:
        print('2 em primeiro  {}'.format(p2))
        print('1 em segundo {}'.format(p1))
    print('---------------')

c1 = Carro('Fusca',0, 100)
c2 = Carro('Gol', 15, 85)
p1 = 0
p2 = 0
para = True
while(para):
    os.system('clear')
    time.sleep(1)
    p1 += c1.andar()
    p2 += c2.andar()
    corrida(p1,p2)
    if p1 >= 1000 or p2 >= 1000:
        para = False

if p1 > p2:
    print("p1 ganhou")
else:
    print("p2 ganhou")