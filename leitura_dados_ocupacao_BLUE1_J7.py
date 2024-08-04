# EXPERIMENTO ATLAS - Reconstrução de sinal - Melhor Estimador Linear Não Enviesado - Best Linear Unbiased Estimator (BLUE1) - Estimação da amplitude ou fase para o janelamento fixo de 7.
# Autor: Guilherme Barroso Morett.
# Data: 04 de agosto de 2024.

# Objetivo do código: realização da leitura dos dados de ocupação no formato de janelamento fixo de 7.

""" 
Organização do código:

Leitura dos dados de entrada de acordo com o janelamento fixo de 7.
Os dados de entrada das ocupações no formato de arquivo texto (txt) contém informações sobre os pulsos de sinais (ADC Count), a amplitude de referência (ADC Count) e a fase de referência (ns).

Funções presentes:

1) Função para a leitura dos dados de ocupação.
Entrada: número de ocupação.
Saída: matriz dos dados de ocupação.

2) Função para separação em dados de treino e teste.
Entrada: matriz com os dados de pulsos de sinais e o vetor com o parâmetro de referência.
Saída: matriz de treino e teste dos pulsos de sinais e o vetor de treino e teste do parâmetro de referência.
"""

# Importação das bibliotecas.
import numpy as np
import os

### ------------------------------------------ 1) FUNÇÃO PARA A LEITURA DOS DADOS DE OCUPAÇÃO -------------------------------------------------- ###

# Definição da função para a leitura dos dados de ocupação no formato free running.
def leitura_dados_ocupacao(numero_ocupacao):

    # Nome da pasta em que se encontra o arquivo de entrada das ocupações.
    pasta_dados_ocupacao = "Dados_OC_J7"

    # Nome do arquivo de entrada das ocupações.
    arquivo_dados_ocupacao = f"OC_{numero_ocupacao}.txt"

    # O caminho para esse arquivo de entrada das ocupações.
    caminho_arquivo_dados_ocupacao = os.path.join(pasta_dados_ocupacao, arquivo_dados_ocupacao)

    # Caso o caminho especificado exista.
    if os.path.exists(caminho_arquivo_dados_ocupacao):
    
        # Abre o aquivo de entrada no modo leitura.
        with open(caminho_arquivo_dados_ocupacao, "r") as arquivo_entrada_ocupacoes:
        
            # Armazena os dados na variável Matriz_Dados_OC.
            Matriz_Dados_OC = np.array(np.loadtxt(arquivo_entrada_ocupacoes, dtype = 'double', delimiter = ' '))
 
    # Caso contrário.       
    else:
    
        # Impressão de mensagem que o arquivo de entrada não existe.
        print(f"O arquivo {arquivo_dados_ocupacao} não existe na pasta {pasta_dados_ocupacao}.")

    # Obs.: da forma que o programa está escrito, os arquivos de entrada devem estar em uma pasta em que está o código do programa.
    # Caso deseja-se alterar isso basta mudar o endereço do arquivo.
    
    Matriz_Pulsos_Sinais_Janelado = Matriz_Dados_OC[:, :7]
    vetor_amplitude_referencia_janelado = Matriz_Dados_OC[:, 7]
    vetor_fase_referencia_janelado = Matriz_Dados_OC[:, 8]
     
    # A função retorna a Matriz_Pulsos_Sinais_Janelado, vetor_amplitude_referencia_janelado, vetor_fase_referencia_janelado.
    return Matriz_Pulsos_Sinais_Janelado, vetor_amplitude_referencia_janelado, vetor_fase_referencia_janelado

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ---------------------------------- 2) FUNÇÃO PARA SEPARAÇÃO EM DADOS DE TREINO E DE TESTE -------------------------------------------------- ###

# Definição da função para a separação dos dados em treino e teste.
def dados_treino_teste_histograma(Matriz_Pulsos_Sinais, vetor_parametro_referencia):
    
    # Obs.: certifique-se que a Matriz e o vetor tenham a mesma quantidade de linhas.
    
    # Caso a matriz dos dados dos pulsos de sinais e o vetor de parâmetros de referência tenham o mesmo tamanho.
    if len(Matriz_Pulsos_Sinais) == len(vetor_parametro_referencia):
        
        # Definição do índice da metade da matriz. 
        # Obs.: nesse caso está configurado para metade dos dados serem de treino e teste.
        indice_metade = len(Matriz_Pulsos_Sinais) // 2
        
        # A primeira metade corresponde a matriz Matriz_Pulsos_Sinais_Treino.
        Matriz_Pulsos_Sinais_Treino = Matriz_Pulsos_Sinais[ : indice_metade]
        
        # A segunda metade corresponde a matriz Matriz_Pulsos_Sinais_Teste.
        Matriz_Pulsos_Sinais_Teste = Matriz_Pulsos_Sinais[indice_metade : ]
        
        # A primeira metade do vetor corresponde ao vetor vetor_parametro_referencia_treino.
        vetor_parametro_referencia_treino = vetor_parametro_referencia[ : indice_metade]
        
        # A segunda metade do vetor corresponde ao vetor vetor_parametro_referencia_teste.
        vetor_parametro_referencia_teste = vetor_parametro_referencia[indice_metade : ]
        
    # Caso contrário.
    else:
    
        # Impressão de mensagem de alerta.
        print("A matriz de pulsos de sinais e o vetor do parâmetro de referência devem ter a mesma quantidade de linhas!\n")
        
        # A execução do programa é interrompida.
        exit(1)
    
    # A função retorna a matriz dos dados de pulsos de sinais dividida em treino e teste, assim como o vetor dos parâmetros de referência.    
    return Matriz_Pulsos_Sinais_Treino, Matriz_Pulsos_Sinais_Teste, vetor_parametro_referencia_treino, vetor_parametro_referencia_teste
        
### -------------------------------------------------------------------------------------------------------------------------------------------- ###