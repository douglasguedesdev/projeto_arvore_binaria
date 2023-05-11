# Alunos: Analicia Fernandes Aquino Guedes
#         Douglas Manuel Guedes Silva
#         Danilo ALves de ASSIS Nobrega
#         Emanuel Pedro sw Nobrega Araujo
#         Vitor Gabriel




class No: # Representa um nó da arvore, cada nó contem um valor
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria: #Classe responsavel por gerenciar a arvore em si
    def __init__(self): #representa a raiz da arvore
        self.raiz = None

    def inserir(self, valor): #verifica se a arvore esta vazia
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(valor, self.raiz) #insere o valor em seu devido lugar na árvore.

    def _inserir_recursivo(self, valor, no_atual): # função auxiliar que insere o valor em uma posição específica na árvore de forma recursiva
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._inserir_recursivo(valor, no_atual.esquerda)
        else:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self._inserir_recursivo(valor, no_atual.direita)

    def buscar(self, valor): #esponsável por procurar um valor específico na árvore.
        return self._buscar_recursivo(valor, self.raiz)

    def _buscar_recursivo(self, valor, no_atual): #faz a busca pelo valor na árvore de forma recursiva
        if no_atual is None or no_atual.valor == valor:
            return no_atual

        if valor < no_atual.valor:
            return self._buscar_recursivo(valor, no_atual.esquerda)
        else:
            return self._buscar_recursivo(valor, no_atual.direita)

class Arvore:  # atua como uma interface mais simplificada para interagir com a árvore binária
    def __init__(self):
        self.arvore_binaria = ArvoreBinaria()

    def inserir(self, valor):
        self.arvore_binaria.inserir(valor)

    def buscar(self, valor):
        return self.arvore_binaria.buscar(valor)

# Exemplo de uso:
arvore = Arvore()
arvore.inserir(10)
arvore.inserir(5)
arvore.inserir(15)
arvore.inserir(2)
# realizamos uma busca pelo valor 5 usando o método buscar e exibimos o resultado.
no_encontrado = arvore.buscar(5)
if no_encontrado:
    print("Nó encontrado:", no_encontrado.valor)
else:
    print("Nó não encontrado.")


#         10
#        /  \
#       5    15
#      /
#     2         
