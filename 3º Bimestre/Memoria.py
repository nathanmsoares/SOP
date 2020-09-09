import random

class Memoria:

    def __init__(self, lista):
        self.__espaco_memoria = lista
        self.__memoria = []


    def gerarMemoria(self):
        self.__memoria = ['X' if random.randint(1, 10) > 7 else '' for i in range(self.__espaco_memoria)]
        print("\nMemoria Inicial\n", self.__memoria)


    @property
    def tamanho_memoria(self):
        return self.__memoria


    def bestFit(self, tamanho_programa):
        print("\nVocê escolheu o método Best Fit\n")
        final = 0
        inicio = 0
        posicao = 0
        menor = 10000000000000000
        achou = False
        while(inicio < len(self.__memoria)):
            if self.__memoria[inicio] == '':
                final = inicio + 1
                while(final < len(self.__memoria)):
                    if self.__memoria[final] != '':
                        break
                    final += 1
                espaco = final - inicio
                if espaco >= tamanho_programa:
                    if menor > espaco:
                        menor = espaco
                        posicao = inicio
                        achou = True
                inicio = final
            inicio += 1
        if achou == False:
            print("Não foi possivel alocar seu programa")
        else:
            for i in range(tamanho_programa):
                self.__memoria[posicao] = '1'
                posicao += 1
            print("Memoria com alocacao", self.__memoria)

    def worstFit(self, tamanho_programa):
        print("\nVocê escolheu o método Worst Fit\n")
        worst = 0
        final = 0
        inicio = 0
        posicao = 0
        while(inicio < len(self.__memoria)):
            if self.__memoria[inicio] == '':
                final = inicio + 1
                while(final < len(self.__memoria)):
                    if self.__memoria[final] != '':
                        break
                    final += 1
                espaco = final - inicio
                if espaco > worst:
                    worst = espaco
                    posicao = inicio
                inicio = final    
            inicio += 1
        if worst >= tamanho_programa:
            for i in range(tamanho_programa):
                self.__memoria[posicao] = '2'
                posicao += 1
            print('Memoria atual', self.__memoria)

        else:
            print("Não foi possivel alocar o programa")


    def firstFit(self, tamanho_programa):
        print("\nVocê escolheu o método First Fit\n")
        inicio = 0
        final = 0
        achou = False
        posicao_inicial = 0
        while(inicio < len(self.__memoria)):
            if self.__memoria[inicio] == '':
                final = inicio + 1
                if achou == True:
                    break                 
                while(final < len(self.__memoria)):
                    if self.__memoria[final] != '':
                        break
                    final += + 1
                first = final - inicio
                if first >= tamanho_programa:
                    for i in range(tamanho_programa):
                        self.__memoria[inicio] = '3'
                        inicio += 1
                    achou = True
                    break   
                inicio = final
            inicio += 1
        if achou == True:
            print("Memoria com programa alocado", self.__memoria)
        else:
            print("Não foi possivel alocar a memoria")

    def desalocar_programa(self, programa):
        for i in range(len(self.__memoria)):
            if self.__memoria[i] == programa:
                self.__memoria[i] = ''    
        print("Memoria desalocada", self.__memoria)

if __name__ == '__main__':

    array = int(input("Qual o tamanho da memória que você deseja usar?\n"))
    memoria_atual = Memoria(array)
    memoria_atual.gerarMemoria()
    while(True):
        tamanho = int(input("\nQual o tamanho do seu programa?\n"))
        escolha = int(input("\nQual algoritmo você deseja executar?\
        \n\t1 - Best Fit\n\t2 - Worst Fit\n\t3 - First fit\n\
        4 - Desalocar programa alocado através do Best Fit\n\
        5 - Desalocar programa alocado através do Worst Fit\n\
        6 - Desalocar programa alocado através do First Fit\n\
        7 - Sair\n\t"))
        if escolha == 1:
            memoria_atual.bestFit(tamanho)
        elif escolha == 2:
            memoria_atual.worstFit(tamanho)
        elif escolha == 3:
            memoria_atual.firstFit(tamanho)
        elif escolha == 4:
            memoria_atual.desalocar_programa('1')
        elif escolha == 5:
            memoria_atual.desalocar_programa('2')
        elif escolha == 6:
            memoria_atual.desalocar_programa('3')
        elif escolha == 7:
            break
        else:
            print("você digitou um número invalido")
        

    
    # memoria_atual.gerarMemoria()
    # memoria_atual.firstFit(5)


    