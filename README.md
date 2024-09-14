# Analise do Algoritmo de Seleção por Raiz Quadratica

## Objetivo
Verificar eficiência do algoritmos de seleção por raiz quadratica usando
Shell Sort ou Heap

## Material e Metodologia
- **Definição do Problema:** O problema de ordenação consiste em organizar
    os itens guardados em um conjunto por um determinada especificação. Dessa forma
    será comparado o tempo de execução do algoritmo para ordenar o conjunto.
- **Implementação:** Os algoritmos implementados foram: ordenação por seleção por raiz quadrática usando \textit{shell sort} e ordenação por seleção por raiz quadrática usando \textit{heap},
    em Python, versão 3.12. No momento da implementação foi optado por tipar os 
    algoritmos além de seguir melhor prática de programação usando complexidade 
    ciclomática para os testes unitários.
- **Configuração do Ambiente:** O ambiente da execução dos experimentos
    foi configurando com as seguintes especificações: processador Core-i5 2520M
    8 GB Ram, SSD 1 TB, com o sistema operacional Windows 10. Os pacotes utilizados para medição de tempo foram \textit{timeit} e \textit{pandas}.
- **Seleção dos Dados:** Para elaboração dos vetores de tamanhos variados
    ($10^{4}$, $10^{5}$, $10^{6}$, $10^{7}$ e $10^{8}$), usando números randômicos.
    Para isso, foi utilizado o pacote \textit{numpy}, dessa forma após a geração deles,
    era coletado o tempo de execução do algoritmo.
- **Execução dos Experimentos:** Para as entradas de $10^{4}$, $10^{5}$, 
    $10^{6}$ foram executados 10 vezes, para $10^{7}$ foi executado 5 vezes e a outra
    entrada somente 1 vezes, além de 1 execução no
    pior caso de execução, sendo registrados em um dicionário. As comparações
    foi realizada no tempo médio dos algoritmos, considerando o desvio padrão
    dos dados coletados

### Conjuntos de dados

[Link dos dados para replicação]()