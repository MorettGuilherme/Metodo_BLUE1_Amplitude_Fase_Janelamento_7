# EXPERIMENTO ATLAS - Reconstrução de sinal - Melhor Estimador Linear Não Enviesado - Best Linear Unbiased Estimator (BLUE1) - Estimação da amplitude ou fase para o janelamento fixo 7.
# Autor: Guilherme Barroso Morett.
# Data: 04 de agosto de 2024.

# Objetivo do código: geração de arquivos de saída baseados nos dados estatísticos dos histogramas do erro de estimação da amplitude ou fase pelo método BLUE1 para o janelamento fixo 7.

""" 
Organização do Código:

Importação de arquivos.
Método BLUE1 para a estimação da amplitude ou fase para o janelamento fixo 7: metodo_BLUE1_J7.py

Funções presentes:

1) Função para o cálculo dos dados estatísticos do erro de estimação pelo método Best Linear Unbiased Estimator (BLUE1) para o janelamento fixo 7.
Entrada: lista com o erro de estimação para a amplitude ou fase.
Saída: a média, a variância e o desvio padrão do erro de estimação para a amplitude ou fase.

2) Instrução para salvar os dados estatísticos do erro de estimação da amplitude ou fase para determinada ocupação em um arquivo de saída pelo método Best Linear Unbiased Estimator (BLUE1) para o janelamento fixo 7.
Entrada: a média, a variância e o desvio padrão do erro de estimação para a amplitude ou fase.
Saída: nada.

3) Instrução principal do código.
Entrada: nada.
Saída: nada.
"""

# Importação das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt
import random as rd
import os
from tqdm import tqdm
import time
from termcolor import colored

# Importação dos arquivos.
from metodo_BLUE1_J7 import * 

# Impressão de uma linha que representa o início do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")

# Título do programa.

# A variável titulo_programa armazena o título em negrito.
titulo_programa = colored("Geração de arquivos de saída baseados nos dados estatísticos dos histogramas do erro de estimação da amplitude ou fase pelo método Best Linear Unbiased Estimator (BLUE1) para o janelamento fixo 7:\n", attrs=["bold"])

# Impressão do título do programa.
print(titulo_programa)

### ------------------- 1) FUNÇÃO PARA O CÁLCULO DOS DADOS ESTATÍSTICOS DO ERRO DE ESTIMAÇÃO DA AMPLITUDE OU FASEPELO MÉTODO BLUE1 ------------- ###

# Definição da função para o cálculo dos dados estatísticos do erro de estimação da amplitude ou fase pelo método BLUE1 para o janelamneto fixo 7.
def dados_estatisticos_erro_estimacao_parametro_BLUE1_janelamento_7(lista_erro_estimacao_parametro):
    
    # A lista do erro da amplitude ou fase é convertida para o tipo numpy array.
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

### --- 2) INSTRUÇÃO PARA A IMPRESSÃO DOS DADOS ESTATÍSTICOS DO ERRO DE ESTIMAÇÃO DA AMPLITUDEOU FASE EM UM ARQUIVO DE SAÍDA PELO MÈTODO BLUE1 --- ###

# Definição da instrução para a impressão em um arquivo de saída, os dados estatísticos do erro de estimação do parâmetro pelo método BLUE 1.
def arquivo_saida_dados_estatisticos_erro_estimacao_parametro_BLUE1_janelamento_7(parametro, n_ocupacao, media_erro_estimacao_parametro, var_erro_estimacao_parametro, desvio_padrao_erro_estimacao_parametro):

    # Definição do título presente no arquivo de saída.
    titulo_arquivo_saida = "Oc,media_erro,var_erro,desvio_padrao_erro\n"

    # Definição da pasta em que contém o arquivo de saída.
    pasta_saida = f"Dados_Estatisticos_BLUE1_{parametro.capitalize()}_Janelamento_7_OC"

    # Caso a pasta não exista.
    if not os.path.exists(pasta_saida):
        # Criação da pasta de saída.
        os.makedirs(pasta_saida)

    # Nome do arquivo de saida.
    arquivo_saida = f"dados_estatisticos_BLUE1_janelamento_7.txt"

    # Caminho completo para o arquivo de saída.
    caminho_arquivo_saida = os.path.join(pasta_saida, arquivo_saida)

    # Verifica se o arquivo existe e está vazio.
    try:
        with open(caminho_arquivo_saida, 'r') as arquivo_saida_dados_estatisticos:
            primeiro_caractere = arquivo_saida_dados_estatisticos.read(1)
            if not primeiro_caractere:
                # Arquivo está vazio, escreva o título
                with open(caminho_arquivo_saida, 'a') as file:
                    file.write(titulo_arquivo_saida)
    except FileNotFoundError:
        # Se o arquivo não existe, cria e escreve o título
        with open(caminho_arquivo_saida, 'w') as file:
            file.write(titulo_arquivo_saida)

    # Comando para tentar realizar uma operação.
    try:
        # Abre o arquivo de saída no modo de acrescentar (append).
        with open(caminho_arquivo_saida, "a") as arquivo_saida_dados_estatisticos:
            # Escrita dos dados de interesse.
            arquivo_saida_dados_estatisticos.write(f"{n_ocupacao},{media_erro_estimacao_parametro},{var_erro_estimacao_parametro},{desvio_padrao_erro_estimacao_parametro}\n")
        
    # Excessão.
    except Exception as e:
        # Impressão de mensagem de alerta.
        print("Ocorreu um erro ao atualizar o arquivo de saída dos dados estatísticos:", str(e))

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### -------------------------------------- 3) INSTRUÇÃO PRINCIPAL DO CÓDIGO (MAIN) ------------------------------------------------------------- ###

# Definição da instrução principal (main) para esse código.
def principal_arquivo_saida_dados_estatisticos_BLUE1_janelamento_7():
    
    # A variável ocupacao_inicial armazena o valor inicial da ocupação que é 0.
    ocupacao_inicial = 0
    
    # A variável ocupacao_final armazena o valor final da ocupação que é 100.
    ocupacao_final = 100
    
    # A variável incremento_ocupacao armazena o valor de incremento entre as ocupações.
    incremento_ocupacao = 10
    
    # A variável parametro_amplitude recebe a string "amplitude".
    parametro_amplitude = "amplitude"
    
    # A variável parametro_fase recebe a string "fase".
    parametro_fase = "fase"
    
    # Para o número de ocupação inicial de 0 até 100 com incremento de 10.
    for n_ocupacao in tqdm(range(ocupacao_inicial, ocupacao_final+1, incremento_ocupacao)):
    
        # Chamada ordenada das funções.
    
        Matriz_Pulsos_Sinais_janelado, vetor_amplitude_referencia_janelado, vetor_fase_referencia_janelado = leitura_dados_ocupacao(n_ocupacao)
        Matriz_Pulsos_Sinais_Treino_Janelado, Matriz_Pulsos_Sinais_Teste_Janelado, vetor_amplitude_referencia_treino_janelado, vetor_amplitude_referencia_teste_janelado = dados_treino_teste_histograma(Matriz_Pulsos_Sinais_janelado, vetor_amplitude_referencia_janelado)
        Matriz_Pulsos_Sinais_Treino_Janelado, Matriz_Pulsos_Sinais_Teste_Janelado, vetor_fase_referencia_treino_janelado, vetor_fase_referencia_teste_janelado = dados_treino_teste_histograma(Matriz_Pulsos_Sinais_janelado, vetor_fase_referencia_janelado)
    
        Matriz_Ruidos_Janelado = leitura_dados_ruidos(n_ocupacao)
        Matriz_Ruidos_Janelado_Treino, Matriz_Ruidos_Janelado_Teste = dados_ruidos_treino_teste_histograma(Matriz_Ruidos_Janelado)
    
        lista_erro_estimacao_amplitude = metodo_BLUE1(parametro_amplitude, Matriz_Ruidos_Janelado_Treino, Matriz_Pulsos_Sinais_Teste_Janelado, vetor_amplitude_referencia_teste_janelado)
        lista_erro_estimacao_fase = metodo_BLUE1(parametro_fase, Matriz_Ruidos_Janelado_Treino, Matriz_Pulsos_Sinais_Teste_Janelado, vetor_fase_referencia_teste_janelado)
            
        media_erro_estimacao_amplitude, var_erro_estimacao_amplitude, desvio_padrao_erro_estimacao_amplitude = dados_estatisticos_erro_estimacao_parametro_BLUE1_janelamento_7(lista_erro_estimacao_amplitude)
        media_erro_estimacao_fase, var_erro_estimacao_fase, desvio_padrao_erro_estimacao_fase = dados_estatisticos_erro_estimacao_parametro_BLUE1_janelamento_7(lista_erro_estimacao_fase)
    
        arquivo_saida_dados_estatisticos_erro_estimacao_parametro_BLUE1_janelamento_7(parametro_amplitude, n_ocupacao, media_erro_estimacao_amplitude, var_erro_estimacao_amplitude, desvio_padrao_erro_estimacao_amplitude)
        arquivo_saida_dados_estatisticos_erro_estimacao_parametro_BLUE1_janelamento_7(parametro_fase, n_ocupacao, media_erro_estimacao_fase, var_erro_estimacao_fase, desvio_padrao_erro_estimacao_fase)

# Chamada da instrução principal do código.
principal_arquivo_saida_dados_estatisticos_BLUE1_janelamento_7()

# Impressão de uma linha que representa o fim do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")   


            
            