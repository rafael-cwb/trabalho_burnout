from dados_coletados import lista_respostas
from funcoes import *

print("=#="*10)
print("ANÁLISE COMPUTACIONAL DE RISCO DE BURNOUT")
print("PUCPR - Bacharelado em Ciência da Computação")
print("Disciplina: Raciocínio Algorítmico - Turma U")
print("Este programa analisa sintomas de burnout e sugere ações para minimizar seus efeitos.")
print("=#="*10)


while True:
    print() # Pula uma linha. Apenas estética
    oQueFazer = TelaAbertura() # Abertura do programa.
    
    # Se o input for incorreto, pede novamente ao usuário
    while oQueFazer not in "1234567" or len(oQueFazer) > 1 or len(oQueFazer) < 1:
        print("Ops! O que foi digitado não está entre as opções!")
        oQueFazer = input("O que deseja saber sobre o burnout? ")

    # Passando da etapa anterior a resposta com certeza é um número, então ele é passado para int para facilitar o código
    oQueFazer = int(oQueFazer)

    # PERGUNTAR SOBRE
    #MatrizFuncoes = [
    #    SugereMinimizacaoSintomas
    #]
    ClassificaNivelRisco(CalculaScoreIndividual(lista_respostas))
    print() # Pula uma linha. Apenas estética
    if oQueFazer == 1:
        SugereMinimizacaoSintomas()
    elif oQueFazer == 2:
        print("Bana")
    elif oQueFazer == 3:
        print("Bana")
    elif oQueFazer == 4:
        percentuais = CalculaPercentual(ClassificaNivelRisco(CalculaScoreIndividual(lista_respostas)))
        print(f"Percentual de pessoas com risco BAIXO: {percentuais['baixo']}%")
    elif oQueFazer == 5:
        percentuais = CalculaPercentual(ClassificaNivelRisco(CalculaScoreIndividual(lista_respostas)))
        print(f"Percentual de pessoas com risco MODERADO: {percentuais['moderado']}%")
    elif oQueFazer == 6:
        percentuais = CalculaPercentual(ClassificaNivelRisco(CalculaScoreIndividual(lista_respostas)))
        print(f"Percentual de pessoas com risco ALTO: {percentuais['alto']}%")  
    elif oQueFazer == 7:
        print("Encerrando o programa.")
        break