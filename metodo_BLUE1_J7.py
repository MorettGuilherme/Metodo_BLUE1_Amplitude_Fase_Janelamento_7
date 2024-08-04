# EXPERIMENTO ATLAS - Reconstrução de sinal - Melhor Estimador Linear Não Enviesado - Best Linear Unbiased Estimator (BLUE1) - Estimação da amplitude ou fase para o janelamento fixo de 7.
# Autor: Guilherme Barroso Morett.
# Data: 04 de agosto de 2024.

# Objetivo do código: Aplicação do método BLUE1 para a estimação da amplitude ou fase para o janelamento fixo de 7.

"""
Organização do código:

Leitura dos dados de entrada de acordo com o janelamento fixo de 7.
Os dados de entrada das ocupações no formato de arquivo texto (txt) contém informações sobre os pulsos de sinais (ADC Count), a amplitude de referência (ADC Count) e a fase de referência (ns).

Funções presentes:

1) Função para a definição do vetor pulso de referência.
Entrada: nada.
Saída: vetor pulso de referência para cada instante de tempo de acordo com o janelamento 7.

2) Função para a definição do vetor da derivada temporal do pulso de referência.
Entrada: nada.
Saída: vetor da derivada temporal do pulso de referência para cada instante de tempo de acordo com o janelamento 7.

3) Função para o método BLUE1.
Entrada: parâmetro, matriz com os pulsos de sinais da etapa de treino, matriz com os pulsos de sinais da etapa de teste, vetor do parâmetro de referência.
Saída: lista com o erro de estimação pelo método BLUE1

"""

# Importação das bibliotecas.
import numpy as np

# Importação dos arquivos.
from leitura_dados_ocupacao_BLUE1_J7 import *
from leitura_dados_ruidos_BLUE1_J7 import *

### ------------------------------------------------- 1) FUNÇÃO PARA O PULSO DE REFERÊNCIA ----------------------------------------------------- ###

# Definição da função para o vetor pulso de referência de acordo com o janelamento fixo de 7.
def pulso_referencia():
    
    # Criação das variáveis que armazenam os valores dos pulsos de referência para cada cada instante de tempo.
    h_tm75 = 2.304e-05 # t = -75,0 ns
    h_tm50 = 0.0172264 # t = -50,0 ns
    h_tm25 = 0.452445 # t = -25,0 ns
    h_t0 = 1.0 # t = 0,0 ns
    h_tM25 = 0.563307 # t = 25,0 ns
    h_tM50 = 0.149335 # t = 50,0 ns
    h_tM75 = 0.0423598 # t = 75,0 ns
       
    # Definição do vetor pulso de referência de acordo com o janelamento 7 no intervalo de tempo de -75,0 a 75,0 ns.
    vetor_pulso_referencia = np.array([h_tm75, h_tm50, h_tm25, h_t0, h_tM25, h_tM50, h_tM75])

    # A função retorna o vetor pulso de referência.
    return vetor_pulso_referencia

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ------------------------------------------- 2) FUNÇÃO PARA A DERIVADA DO PULSO DE REFERÊNCIA ----------------------------------------------- ###

# Definição da função para o vetor da derivada do pulso de referência de acordo com o janelamento fixo de 7.
def derivada_pulso_referencia():
    
    # Criação das variáveis que armazenam os valores das derivadas dos pulsos de referência para cada cada instante de tempo.
    dh_tm75 = 5.472e-05 # t = -75,0 ns
    dh_tm50 = 0.0036703166666666675 # t = -50,0 ns
    dh_tm25 = 0.031080499999999955 # t = -25,0 ns
    dh_t0 = 1.666666668009853e-07 # t = 0,0 ns
    dh_tM25 = -0.024345499999999964 # t = 25,0 ns
    dh_tM50 = -0.008006833333333371 # t = 50,0 ns
    dh_tM75 = -0.0024333666666666635 # t = 75,0 ns
        
    # Definição do vetor da derivada do pulso de referência de acordo com o janelamento 7 no intervalo de tempo de -75,0 a 75,0 ns.
    vetor_derivada_pulso_referencia = np.array([dh_tm75, dh_tm50, dh_tm25, dh_t0, dh_tM25, dh_tM50, dh_tM75])
        
    # A função retorna o vetor pulso de referência.
    return vetor_derivada_pulso_referencia
    
### -------------------------------------------------------------------------------------------------------------------------------------------- ###   

### ----------------------------------------------- 3) FUNÇÃO PARA O MÉTODO BLUE1 ------------------------------------------------------------- ###

# Definição da função para o método BLUE1.
def metodo_BLUE1(parametro, Matriz_Pulsos_Sinais_Treino_Janelado, Matriz_Pulsos_Sinais_Teste_Janelado, vetor_parametro_referencia_teste_janelado):

    # Criação da lista vazia para armazenar os erros calculados para o parâmetro. 
    lista_erro_estimacao_parametro = []
    
    # A variável vetor_h recebe o retorno da função pulso_referencia para o janelamento fixo de 7.
    vetor_h = pulso_referencia()
    
    # A variável vetor_dh recebe o retorno da função derivada_pulso_referencia para o janelamento fixo de 7.
    vetor_dh = derivada_pulso_referencia()
    
    # A variável vetor_unitario é um vetor formato por uns com dimensão igual a quantidade de janelamento para o janelamento 7.
    vetor_unitario = np.ones(7)
    
    # Definição da matriz cujas colunas são respectivamente formadas pelo vetor_h, vetor_dh e o vetor_unitario.
    U = np.column_stack((vetor_h, vetor_dh, vetor_unitario))
    
    # A variável Matriz_Covariancia recebe o valor de retorno da função matriz_covariancia.
    Matriz_Covariancia = matriz_covariancia(Matriz_Pulsos_Sinais_Treino_Janelado)
        
    # Tenta calcular a inversa da matriz Matriz_Covariancia.
    try:
    # Calcula a inversa da matriz Matriz_Covariancia usando numpy.linalg.inv.
        Inversa_Matriz_Covariancia = np.linalg.inv(Matriz_Covariancia)
          
    # Caso a matriz Matriz_Covariancia seja singular ou não invertível.  
    except np.linalg.LinAlgError:
    # Impressão de mensagem de erro
        print("A matriz matriz de covariancia não é invertível.")
        
    # Cálculo da transposta da matriz U.
    Transposta_U = np.transpose(U)
    
    # Cálculo de uma parte do vetor de pesos pelo método BLUE 1.
    parte_vetor_blue1 = np.dot(np.dot(Transposta_U, Inversa_Matriz_Covariancia), U)
    
    # Tenta calcular a inversa da parte_vetor_blue1.
    try:
    # Calcula a inversa da matriz parte_vetor_blue1 usando numpy.linalg.inv.
        Inversa_parte_vetor_blue1 = np.linalg.inv(parte_vetor_blue1)
          
    # Caso a matriz parte_vetor_blue1 seja singular ou não invertível.  
    except np.linalg.LinAlgError:
    # Impressão de mensagem de erro
        print("A matriz da parte do vetor de pesos do método BLUE 1 não é invertível.")
    
    # Para o índice de zero até o número de linhas da matriz Matriz_Pulsos_Sinais_Treino_Janelado.
    for indice_linha in range(len(Matriz_Pulsos_Sinais_Teste_Janelado)):
        
        # O vetor vetor_pulsos_sinais corresponde a linha de índice indice_linha da matriz Matriz_Pulsos_Sinais_Treino_Janelado.    
        vetor_pulsos_sinais_teste = Matriz_Pulsos_Sinais_Teste_Janelado[indice_linha]
    
        # O parâmetro de referência é o elemento de índice indice_linha do vetor vetor_parametro_referencia_teste_janelado.
        valor_parametro_referencia_teste = vetor_parametro_referencia_teste_janelado[indice_linha]
        
        # Cálculo do vetor de pesos pelo método BLUE 1.
        vetor_pesos_blue1 = np.dot(np.dot(Inversa_parte_vetor_blue1, Transposta_U), Inversa_Matriz_Covariancia)
        
        # Cálculo do parâmetro estimado pelo método BLUE 1.
        vetor_parametro_estimado = np.dot(vetor_pesos_blue1, vetor_pulsos_sinais_teste)
        
        # Caso a variável parametro seja igual a string "amplitude".
        if parametro == "amplitude":
            
            # A varável valor_parametro_estimado recebe o primeiro elemento do vetor vetor_parametro_estimado.
            valor_parametro_estimado = vetor_parametro_estimado[0]
        
        # Caso a variável parametro seja igual a string "fase".
        elif parametro == "fase":
            
            # A variável valor_amplitude_estimada recebe o primeiro elemento do vetor vetor_parametro_estimado.
            valor_amplitude_estimada = vetor_parametro_estimado[0]
            
            # A variável valor_amplitude_versus_fase_estimada recebe o segundo elemento do vetor vetor_parametro_estimado.
            valor_amplitude_versus_fase_estimada = vetor_parametro_estimado[1]
            
            # A variável valor_parametro_estimado é calculada pela divisão entre os valores da amplitude_fase_estimada pela amplitude_estimada.
            valor_parametro_estimado = valor_amplitude_versus_fase_estimada / valor_amplitude_estimada
        
        # Cálculo do erro de estimação do parâmetro.
        erro_estimacao_parametro = valor_parametro_referencia_teste-valor_parametro_estimado
    
        # O elemento erro_estimacao_parametro é adicionado na lista correspondente.    
        lista_erro_estimacao_parametro.append(erro_estimacao_parametro)

    # A função retorna a lista lista_erro_estimacao_parametro.
    return lista_erro_estimacao_parametro
 
### -------------------------------------------------------------------------------------------------------------------------------------------- ###