import pilha as p

pilha = p.Pilha(5)
pilha.empilhar(4)
print(pilha.ver_topo())
pilha.empilhar(3)
pilha.empilhar(8)
pilha.empilhar(9)
pilha.empilhar(2)
pilha.empilhar(15)
print(pilha.ver_topo())
pilha.desempilhar()
print(pilha.ver_topo())