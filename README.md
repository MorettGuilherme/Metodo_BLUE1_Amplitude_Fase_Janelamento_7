O método Melhor Estimador Linear Não Enviesado (Best Unbiased Linear Estimador - BLUE1) em sua primeria versão permite obter um vetor de parâmetros estimandos, contendo respectivamente, a amplitude, o termo da amplitude versus a fase e o pedestal. Esse reposítorio os resultados referentes a estimação da amplitude e fase para o conjunto de dados já formatados para o janelamento 7.

Organização dos arquivos e pastas.

1) BLUE1_Amplitude_J7
   * Essa pasta contém os os histogramas e os gráficos dos dados estatísticos para a estimação da amplitude pelo método BLUE1.

2) BLUE1_Fase_J7
   * Essa pasta contém os os histogramas e os gráficos dos dados estatísticos para a estimação da fase pelo método BLUE1.
  
3) Dados_Estatisticos_BLUE1_Amplitude_Janelamento_7_OC
   * Essa pasta armazena os dados estatísticos gerados referentes a amplitude.
  
4) Dados_Estatisticos_BLUE1_Fase_Janelamento_7_OC
   * Essa pasta armazena os dados estatísticos gerados referentes a fase.
  
5) Dados_OC_J7
   * Essa pasta contém os arquivos no fornato de texto para os dados referentes a cada uma das ocupações.

6) Dados_Ruidos_OC_J7
   * Essa pasta contém os arquivos no fornato de texto para os dados referentes os ruídos de cada uma das ocupações.
  
7) arquivo_saida_dados_estatisticos_BLUE1_J7.py
   * Esse arquivo gera os dados estatísticos para a estimação da amplitude e fase pelo método BLUE1.
  
8) grafico_dado_estatistico_janelamento_BLUE1_J7.py
   * Esse arquivo plota os gráficos dos dados estátisticos (média, variância ou desvio padrão) da amplitude ou fase.
  
9) histograma_erro_parametro_BLUE1_J7.py
   * Esse arquivo plota o histograma para a amplitude ou fase para uma dada ocupação ao considerar o janelamento fixo 7.

10) leitura_dados_ocupacao_BLUE1_J7.py
   * Esse arquivo realiza a leitura dos dados de ocupações já formatados para o janealemento 7.

11) leitura_dados_ruidos_BLUE1_J7.py
   * Esse arquivo realiza a leitura dos dados de ruídos já formatados para o janelamento 7.

12) metodo_BLUE1_J7.py
   * Aplicação do método BLUE1 para a estimaçãop dos parâmetro da amplitude e fase.

Obs.: esses dados de ocupações e ruídos foram fornecidos pelo orientador. Não foram gerados pelo Pulse Generator.

