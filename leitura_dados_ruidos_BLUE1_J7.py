# EXPERIMENTO ATLAS - Reconstrução de sinal - Melhor Estimador Linear Não Enviesado - Best Linear Unbiased Estimator (BLUE1) - Estimação da amplitudw ou fase para o janelamento fixo 7.
# Autor: Guilherme Barroso Morett.
# Data: 04 de agosto de 2024.

# Objetivo do código: realização da leitura dos dados de ruídos no formato de janelamento fixo de 7.

""" 
Organização do código:

Leitura dos dados de entrada de acordo com o janelamento desejado.
Os dados de entrada dos ruídos no formato de arquivo texto (txt) contém informações sobre o ruído da eletrônica do sinal somado com o efeito de empilhamento para cada ocupação.
Obs.: na ocupação 0 só há o efeito do ruído da eletrônica do sinal, porque não há empilhamento.

Funções presentes:

1) Função para a leitura dos dados de ruídos de acordo com a ocupação.
Entrada: número de ocupação.
Saída: Matriz dos dados de ruídos.

2) Função para separação em dados de treino e teste.
Entrada: matriz com os dados de ruídos.
Saída: matriz com os dados de ruídos para a etapa de treino e teste.

3) Função para a construção da matriz de covariância.
Entrada: matriz com os dados de ruídos janelados.
Saída: matriz de covariância dos dados de ruídos.

4) Função para a construção da matriz de covariância como identidade.
Entrada: matriz com os dados de ruídos janelados.
Saída: matriz de covariância igual a identidade.
"""

# Importação das bibliotecas.
import numpy as np
import os

### ------------------------------------------ 1) FUNÇÃO PARA A LEITURA DOS DADOS DE RUÍDOS ---------------------------------------------------- ###

# Definição da função para a leitura dos dados de ruídos no formato free running.
def leitura_dados_ruidos(n_ocupacao):

    # Nome da pasta em que se encontra o arquivo de entrada dos ruídos.
    pasta_dados_ruidos = "Dados_Ruidos_OC_J7"

    # Nome do arquivo de entrada dos ruídos.
    arquivo_dados_ruidos = f"Ruido_OC_{n_ocupacao}.txt"

    # O caminho para esse arquivo de entrada dos ruídos.
    caminho_arquivo_dados_ruidos = os.path.join(pasta_dados_ruidos, arquivo_dados_ruidos)

    # Caso o caminho especificado exista.
    if os.path.exists(caminho_arquivo_dados_ruidos):
    
        # Abre o aquivo de entrada no modo leitura.
        with open(caminho_arquivo_dados_ruidos, "r") as arquivo_entrada_ruidos:
        
            # Armazena os dados na variável Matriz_Dados_Ruidos.
            Matriz_Dados_Ruidos = np.array(np.loadtxt(arquivo_entrada_ruidos, dtype = 'double', delimiter = ' '))
 
    # Caso contrário.       
    else:
    
        # Impressão de mensagem que o arquivo de entrada não existe.
        print(f"O arquivo {arquivo_dados_ruidos} não existe na pasta {pasta_dados_ruidos}.")

    # Obs.: da forma que o programa está escrito, os arquivos de entrada devem estar em uma pasta em que está o código do programa.
    # Caso deseja-se alterar isso basta mudar o endereço do arquivo.
    
    # A função retorna a matriz Matriz_Dados_Ruidos.
    return Matriz_Dados_Ruidos

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ----------------------------- 2) FUNÇÃO PARA SEPARAÇÃO EM DADOS DE RUÍDOS DE TREINO E DE TESTE --------------------------------------------- ###

# Definição da função para a separação dos dados em treino e teste.
def dados_ruidos_treino_teste_histograma(Matriz_Dados_Ruidos):
    
    # Definição do índice da metade da matriz. 
    # Obs.: nesse caso está configurado para metade dos dados serem de treino e teste.
    indice_metade = len(Matriz_Dados_Ruidos) // 2
        
    # A primeira metade corresponde a matriz Matriz_Dados_Ruidos_Treino.
    Matriz_Dados_Ruidos_Treino = Matriz_Dados_Ruidos[ : indice_metade]
        
    # A segunda metade corresponde a matriz Matriz_Dados_Ruidos_Teste.
    Matriz_Dados_Ruidos_Teste = Matriz_Dados_Ruidos[indice_metade : ]
          
    # A função retorna a matriz dos dados de ruídos dividida em treino e teste pela metade do dataset inicial.    
    return Matriz_Dados_Ruidos_Treino, Matriz_Dados_Ruidos_Teste
        
### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ------------------------------------- 3) FUNÇÃO PARA A CONSTRUÇÃO DA MATRIZ DE COVARIÂNCIA ------------------------------------------------- ###

# Definição da função para o cálculo da matriz de covariância a partir dos dados de ruídos.
def matriz_covariancia(Matriz_Dados_Ruidos):
    
    # Cálculo da matriz de covariância considerando que as variáveis estão dispostas nas colunas da matriz de dados de ruídos.
    Matriz_Covariancia_Ruidos = np.cov(Matriz_Dados_Ruidos, rowvar = False)
    
    # A função retorna a matriz de covariância de ruídos.
    return Matriz_Covariancia_Ruidos

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ----------------------------------- 4) FUNÇÃO PARA A CONSTRUÇÃO DA MATRIZ DE COVARIÂNCIA COMO IDENTIDADE ----------------------------------- ###

# Definição da função para a matriz de covariância ser igual a identidade.
def matriz_covariancia_identidade(n_janelamento):
    
    # A matriz de covariância é igual a identidade.
    Matriz_Covariancia_ID = np.eye(n_janelamento)
    
    # A função retorna a matriz de covariância igual a identidade.
    return Matriz_Covariancia_ID

### -------------------------------------------------------------------------------------------------------------------------------------------- ###