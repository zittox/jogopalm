import time
import json
from operator import itemgetter





def json_add(filename='jogadores.json'):
    with open(filename, 'r+') as jg:
        jogo = json.load(jg)
        idx = len(jogo) + 1
        perg1 = input("Qual o seu nome?")
        perg2 = input("Qual a sua idade?")
        perg3 = 0
        perg4 = 0
        nova_entrada = {'id': idx, 'nome': perg1, 'idade': perg2, 'placar': perg3, 'tempo': perg4}
        jogo.append(nova_entrada)
        jg.seek(0)
        json.dump(jogo, jg)



def maior_placar():
    with open('jogadores.json', 'r') as jg:
        jogo = json.load(jg)
        jogo.sort(key=itemgetter('placar'), reverse=True)

        for x, i in enumerate(jogo):
            t = time.gmtime(i['tempo'])
            temp = time.strftime('%H:%M:%S', t)
            print(f'{x+1}º lugar: {i["nome"]}\nPontos: {i["placar"]}\nTempo: {temp}\n')



    



