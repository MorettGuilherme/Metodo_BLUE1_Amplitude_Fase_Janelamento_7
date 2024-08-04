# EXPERIMENTO ATLAS - Reconstrução de sinal - Melhor Estimador Linear Não Enviesado - Best Linear Unbiased Estimator (BLUE1) - Estimação da amplitude ou fase para o janelamento fixo de 7.
# Autor: Guilherme Barroso Morett.
# Data: 04 de agosto de 2024.

# Objetivo do código: análise do erro de estimação do parâmetro da amplitude ou fase pelo método BLUE1 para o janelamento fixo de 7.

"""
Organização do Código:

Importação de arquivos.
Método BLUE1 para a estimação da amplitude ou fase para o janelamento fixo de 7: metodo_BLUE1_janelamento_7.py

Funções presentes:

1) Função para o cálculo da estatística do erro de estimação da amplitude ou fase pelo método BLUE1.
Entrada: lista com os erros de estimação da amplitude ou fase.
Saída: a média, a variância e o desvio padrão do erro de estimação da amplitude ou fase.

2) Instrução para o plote do histograma do erro de estimação da amplitude ou fase pelo método BLUE1.
Entrada: lista com os erros de estimação da amplitude ou fase e seus dados estatísticos.
Saída: nada.

4) Função principal.
Entrada: nada.
Saída: nada.
"""

# Importação das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt
import random as rd
import os
from termcolor import colored

# Importação dos arquivos.
from metodo_BLUE1_J7 import *

# Impressão de uma linha que representa o início do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")

# Título do programa.

# A variável titulo_programa armazena o título em negrito.
titulo_programa = colored("Análise do erro de estimação da amplitude, fase ou pedestal pelo método Best Linear Unbiased Estimator (BLUE 1) para o janelamento fixo de 7:\n", attrs=["bold"])

# Impressão do título do programa.
print(titulo_programa)

### -------------- 1) FUNÇÃO PARA O CÁLCULO DOS DADOS ESTATÍSTICOS DO ERRO DE ESTIMAÇÃO DA AMPLITUDE OU FASE PELO MÉTODO BLUE1 ----------------- ###

# Definição da função para o cálculo dos dados estatísticos do erro de estimação da amplitude ou fase pelo método BLUE1.
def dados_estatisticos_erro_estimacao_parametro_BLUE1_janelamento_7(lista_erro_estimacao_parametro):
    
    # A lista do erro de estimação da amplitude ou fase é convertida para o tipo numpy array.
    vetor_erro_estimacao_parametro = np.array(lista_erro_estimacao_parametro)

    # Cálculo da média do erro de estimação da amplitude ou fase.
    media_erro_estimacao_parametro = np.mean(vetor_erro_estimacao_parametro)

    # Cálculo da variância do erro de estimação da amplitude ou fase.
    var_erro_estimacao_parametro = np.var(vetor_erro_estimacao_parametro)

    # Cálculo do desvio padrão do erro de estimação da amplitude ou fase.
    desvio_padrao_erro_estimacao_parametro = np.std(vetor_erro_estimacao_parametro)
    
    # A função retorna a média, a variância e o desvio padrão dos dados do erro de estimação da amplitude ou fase.
    return media_erro_estimacao_parametro, var_erro_estimacao_parametro, desvio_padrao_erro_estimacao_parametro
    
### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ----------------- 2) INSTRUÇÃO PARA A CONSTRUÇÃO DO HISTOGRAMA DO ERRO DE ESTIMAÇÃO DA AMPLITUDE OU FASE PELO MÉTODO BLUE1 ----------------- ###

# Definição de instrução para o plot do histograma do tipo A do erro de estimação da amplitude ou fase pelo método BLUE1.
def histograma_erro_estimacao_parametro_BLUE1_Janelamento_7(n_ocupacao, parametro, lista_erro_estimacao_parametro, media_erro_estimacao_parametro, var_erro_estimacao_parametro, desvio_padrao_erro_estimacao_parametro):
    
    # A lista do erro de estimação do parâmetro é convertida para o tipo numpy array.
    vetor_erro_estimacao_parametro = np.array(lista_erro_estimacao_parametro)

    # Se a variável parametro for igual a string "amplitude".
    if parametro == "amplitude":
        
        # Nomeação do eixo x de acordo com a amplitude.
        plt.xlabel(f'Erro de estimação da {parametro} (ADC Count)', fontsize = 18)
        
        # A variável x_inf recebe o valor inferior do eixo das abscissas para a amplitude.
        x_inf = -300
    
        # A variável x_sup recebe o valor superior do eixo das abscissas para a amplitude.
        x_sup = 300

    # Se a variável parametro for igual a string "fase".
    if parametro == "fase":
        
        # Nomeação do eixo x de acordo com o parâmetro da fase.
        plt.xlabel(f'Erro de estimação da {parametro} (ns)', fontsize = 18)
        
        # A variável x_inf recebe o valor inferior do eixo das abscissas para a fase.
        x_inf = -300
    
        # A variável x_sup recebe o valor superior do eixo das abscissas para a fase.
        x_sup = 300
        
    # Definição do tamanho dos números do eixo x.    
    plt.xticks(fontsize = 16)

    # Nomeação do eixo y.
    plt.ylabel('Número de eventos', fontsize = 18)
    
    # Definição do tamanho dos números do eixo y.
    plt.yticks(fontsize = 16)
    
    # A variável n_bins recebe a quantidade de bins presente no histograma.
    n_bins = 100

    # A variável texto recebe uma string com as informações de interesse.
    texto = f"Média: {round(media_erro_estimacao_parametro, 6)} \n Variância: {round(var_erro_estimacao_parametro, 6)} \n Desvio padrão: {round(desvio_padrao_erro_estimacao_parametro, 6)}"

    # Impressão do título do gráfico (recomendável para a apresentação de slides).
    # plt.title(f"Ocupação {n_ocupacao}", fontsize = 18)

    # Definição do histograma a partir do vetor vetor_erro_parametro.
    plt.hist(vetor_erro_estimacao_parametro, bins = n_bins, range = [x_inf, x_sup], edgecolor = 'black', linewidth = 1.2)
    
    # Posicionamento do texto no gráfico.
    plt.text(0.99, 0.98, texto, horizontalalignment = 'right',
    verticalalignment = 'top',
    transform = plt.gca().transAxes,
    bbox = dict(facecolor = 'white', alpha = 0.5),
    fontsize = 14)

    # Criação de grid.
    plt.grid()

    # Exibição do gráfico.
    plt.show()

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### -------------------------------------- 3) INSTRUÇÃO PRINCIPAL DO CÓDIGO (MAIN) ------------------------------------------------------------- ###

# Definição da instrução principal (main) do código.
def principal_histograma_erro_estimacao_parametro_BLUE1_janelamento_7():
    
    # Impressão de mensagem no terminal.
    print("Opções de parâmetros:\nAmplitude: 1\nFase: 2\n")
    
    # A variável parametro armazena o número do tipo inteiro digitado pelo usuário via terminal.
    parametro = int(input("Digite o número do parâmetro desejado: "))
    
    # A variável valores_parametro é uma lista com os valores aceitáveis para o parametro.
    valores_parametro = list(range(1,4,1))

    # Caso o valor digitado armazenado na variável parametro não estiver presente na lista valores_parametro.
    if parametro not in valores_parametro:
    
        # Exibição de uma mensagem de alerta de que a opção solicitada é inválida.
        print("Essa opção é inválida!")
        print("---------------------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1)
    
    # A variável n_ocupacao armazena o valor digitado da ocupação desejada no terminal pelo usuário.
    n_ocupacao = float(input("Digite o valor da ocupação desejada: "))

    # A variável valores_ocupacao é uma lista com os valores aceitáveis de ocupação de 0 até 100.
    valores_ocupacao = list(range(0,101,10))

    # Caso o valor digitado armazenado na variável n_ocupacao não estiver presente na lista valores_ocupacao.
    if n_ocupacao not in valores_ocupacao:
    
        # Exibição de uma mensagem de alerta de que a ocupação solicitada é inválida.
        print("\nNúmero de ocupação inválida!\n")
        # A execução do programa é interrompida.
        exit(1) 

    # O tipo da variável n_ocupacao é convertida para inteiro.
    # Obs.: essa conversão possibilita que a leitura do arquivo possa ser feita corretamente.
    n_ocupacao = int(n_ocupacao)
      
    # Chamada ordenada das funções.
    
    Matriz_Pulsos_Sinais_janelado, vetor_amplitude_referencia_janelado, vetor_fase_referencia_janelado = leitura_dados_ocupacao(n_ocupacao)
    
    Matriz_Ruidos_Janelado = leitura_dados_ruidos(n_ocupacao)
    
    Matriz_Ruidos_Janelado_Treino, Matriz_Ruidos_Janelado_Teste = dados_ruidos_treino_teste_histograma(Matriz_Ruidos_Janelado) 

    # Caso a variável parametro seja igual a 1.
    if parametro == 1:
        
        # A variável parametro recebe a string "amplitude".
        parametro = "amplitude"
        
        vetor_parametro_referencia_janelado = vetor_amplitude_referencia_janelado
        
    # Caso a variável parametro seja igual a 2.
    elif parametro == 2:
    
        # A variável parametro recebe a string "fase".
        parametro = "fase"
        
        vetor_parametro_referencia_janelado = vetor_fase_referencia_janelado
        
    # Chamada ordenada das funções.
        
    Matriz_Pulsos_Sinais_Treino_Janelado, Matriz_Pulsos_Sinais_Teste_Janelado, vetor_parametro_referencia_treino_janelado, vetor_parametro_referencia_teste_janelado = dados_treino_teste_histograma(Matriz_Pulsos_Sinais_janelado, vetor_parametro_referencia_janelado)
    
    lista_erro_estimacao_parametro = metodo_BLUE1(parametro, Matriz_Ruidos_Janelado_Treino, Matriz_Pulsos_Sinais_Teste_Janelado, vetor_parametro_referencia_teste_janelado)

    media_erro_estimacao_parametro, var_erro_estimacao_parametro, desvio_padrao_erro_estimacao_parametro = dados_estatisticos_erro_estimacao_parametro_BLUE1_janelamento_7(lista_erro_estimacao_parametro)
    
    histograma_erro_estimacao_parametro_BLUE1_Janelamento_7(n_ocupacao, parametro, lista_erro_estimacao_parametro, media_erro_estimacao_parametro, var_erro_estimacao_parametro, desvio_padrao_erro_estimacao_parametro)
    
# Chamada da instrução principal (main) do código.
principal_histograma_erro_estimacao_parametro_BLUE1_janelamento_7()

### -------------------------------------------------------------------------------------------------------------------------------------------- ###
# Impressão de uma linha que representa o fim do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")