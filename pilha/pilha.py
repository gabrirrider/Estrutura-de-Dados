import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.__capacidade = capacidade #tamanho da pilha
        self.__topo = -1 #pilha vazia
        self.__valores = np.empty(self.__capacidade, dtype=int)

    #métodos auxiliares, usuario não terá acesso
    def __pilha_cheia(self): #usada somente ao empilhar
        return self.__topo == self.__capacidade - 1 #verifica se a pilha está cheia
        
    def __pilha_vazia(self):
        return self.__topo == -1 #verifica se a pilha está vazia
        
    def empilhar(self, valor): #coloca um valor no topo da pilha
        if self.__pilha_cheia():
            print('A pilha está cheia')
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor

    def desempilhar(self):
        if self.__pilha_vazia(): #retira o valor do topo da pilha
            print('A pilha está vazia')
        else:
            self.__topo -= 1

    def ver_topo(self): #retorna o valor do topo da pilha
        if self.__pilha_vazia():
            return None
        else:
            return self.__valores[self.__topo]