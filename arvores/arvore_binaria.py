# Árvore Binária - DSA
# Eduardo Moreira Silva - RM 569923
#
# Cada nó aponta para no máximo dois filhos: esquerda e direita.
# Não existe regra de ordem aqui, os nós são ligados manualmente.


class No:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def pre_ordem(self, no, saida):
        if no is not None:
            saida.append(no.dado)
            self.pre_ordem(no.esquerda, saida)
            self.pre_ordem(no.direita, saida)
        return saida

    def em_ordem(self, no, saida):
        if no is not None:
            self.em_ordem(no.esquerda, saida)
            saida.append(no.dado)
            self.em_ordem(no.direita, saida)
        return saida

    def pos_ordem(self, no, saida):
        if no is not None:
            self.pos_ordem(no.esquerda, saida)
            self.pos_ordem(no.direita, saida)
            saida.append(no.dado)
        return saida

    def buscar(self, no, valor):
        if no is None or no.dado == valor:
            return no
        achou = self.buscar(no.esquerda, valor)
        if achou:
            return achou
        return self.buscar(no.direita, valor)

    def contar_nos(self, no):
        if no is None:
            return 0
        esquerda = self.contar_nos(no.esquerda)
        direita = self.contar_nos(no.direita)
        return esquerda + direita + 1

    def altura(self, no):
        # árvore vazia tem altura 0 e uma folha tem altura 1
        if no is None:
            return 0
        return 1 + max(self.altura(no.esquerda), self.altura(no.direita))

    def folhas(self, no, saida):
        if no is None:
            return saida
        if no.esquerda is None and no.direita is None:
            saida.append(no.dado)
        else:
            self.folhas(no.esquerda, saida)
            self.folhas(no.direita, saida)
        return saida


def main():
    #           8
    #         /   \
    #        3     10
    #       / \      \
    #      1   6      14
    #         /
    #        4
    raiz = No(8)
    raiz.esquerda = No(3)
    raiz.direita = No(10)
    raiz.esquerda.esquerda = No(1)
    raiz.esquerda.direita = No(6)
    raiz.esquerda.direita.esquerda = No(4)
    raiz.direita.direita = No(14)

    arvore = ArvoreBinaria(raiz)
    print("Pré-ordem:", arvore.pre_ordem(arvore.raiz, []))
    print("Em ordem:", arvore.em_ordem(arvore.raiz, []))
    print("Pós-ordem:", arvore.pos_ordem(arvore.raiz, []))
    print("Quantidade de nós:", arvore.contar_nos(arvore.raiz))
    print("Altura:", arvore.altura(arvore.raiz))
    print("Folhas:", arvore.folhas(arvore.raiz, []))

    for procurado in [6, 99]:
        resultado = arvore.buscar(arvore.raiz, procurado)
        print(f"Buscar {procurado}:", "encontrado" if resultado else "não encontrado")


main()
