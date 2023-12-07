import numpy as np

class VetorNaoOrdenado():
    def __init__(self, tamanho):
     self.tamanho = tamanho
     self.ultima_posicao = -1 #sempre está vazio no inicio
     self.valores = np.empty(self.tamanho, dtype=int)

    def imprime(self):
    #testar se vetor está vazio
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(f'{i} : {self.valores[i]}')

    def insere(self, valor):
    #verificar se o vetor não está cheio
        if self.ultima_posicao == self.tamanho - 1:
            print('Capacidade máxima atingida')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i #qdo encontrar retorna a posição
        return -1 #qdo não encontrar retorna -1
    
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else: # realocar os elementos posteriores
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i+1]
            #ajustar o valor da ultima_posicao
            self.ultima_posicao -= 1