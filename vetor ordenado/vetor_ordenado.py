import numpy as np

class VetorOrdenado:

  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    self.valores = np.empty(self.capacidade, dtype=int)

  def imprime(self):
    if self.ultima_posicao == -1:
      print('Vetor vazio')
    else:
      for i in range(self.ultima_posicao + 1):
        print(f'{i} : {self.valores[i]}')

  def insere(self, valor):

    #Passo 1: verificar se vetor está cheio
    if self.ultima_posicao == self.capacidade - 1:
      print('Capacidade máxima atingida')
      return #encerra o método

    #Passo 2: encontrar a posição correta
    posicao = 0 #var. para guardar a posição correta
    for i in range(self.ultima_posicao + 1):#pesquisa linear
      posicao = i
      if self.valores[i] > valor:
        break
      if i == self.ultima_posicao:
        posicao = i + 1

    #Passo 3: remanejando os elementos
    x = self.ultima_posicao
    while (x >= posicao):
      self.valores[x + 1] = self.valores[x]
      x = x - 1

    #passo 4: inserir o elemento na pos. correta
    self.valores[posicao] = valor

    #Passo 5: atualizar ultima posicao
    self.ultima_posicao += 1

  def pesquisar(self, valor):

    for i in range(self.ultima_posicao + 1):

      #situaçao 1
      if self.valores[i] > valor: #nao encontra logo de cara
        return -1

      #situação 2
      if self.valores[i] == valor: #encontra o elemento
        return i

      #situacao 3
      if i == self.ultima_posicao: #passou o vetor todo e não encontrou
        return -1

  def pesquisa_binaria(self, valor):

    #Passo 1: pegando a posição inicial e posição final
    limite_inferior = 0
    limite_superior = self.ultima_posicao

    #Passo 2: pegar indice do meio, verificar se encontrou e dividir limites
    while True:
      #Passo 2.1: guardar indice do meio
      posicao_atual = int((limite_inferior + limite_superior)/2)

      #Passo 2.2: se achou na primeira tentativa ou não
      if self.valores[posicao_atual] == valor: #se achou
        return posicao_atual
      elif limite_inferior > limite_superior: #se não achou
        return -1
      else: #dividir os limites
        if self.valores[posicao_atual] < valor: #limite inferior
          limite_inferior = posicao_atual + 1
        else:
          limite_superior = posicao_atual - 1

  def excluir(self, valor):

    posicao = self.pesquisar(valor) #pesquisa o elemento

    if posicao == -1: #não encontrou
      return -1
    else: #percorre o vetor, reordenando os elementos

      for i in range(posicao, self.ultima_posicao):
        self.valores[i] = self.valores[i+1]

      self.ultima_posicao -= 1