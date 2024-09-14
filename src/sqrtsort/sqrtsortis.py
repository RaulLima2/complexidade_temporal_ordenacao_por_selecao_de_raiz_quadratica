import math
import numpy as np
from collections import deque

def divide_partes(vetor:list[int], n_partes:int)->list[deque[int]]:
  partes:list[deque[int]] = []
  sqrt_n:int = int(math.sqrt(n_partes))
  for i in range(0, n_partes, sqrt_n):
      swap_d:list[int] = list(np.array(vetor[i:i + sqrt_n]) * -1)
      swap:deque[int] = deque(swap_d)
      partes.append(swap)
  return partes


def shell_sort(vetor:deque[int])->deque[int]:
    tamanho:int = len(vetor)
    bloco:int = tamanho // 2
    while bloco > 0:
        for i in range(bloco, tamanho):
            temp = vetor[i]
            j = i
            while j >= bloco and vetor[j - bloco] > temp:
                vetor[j] = vetor[j - bloco]
                j -= bloco
            vetor[j] = temp
        bloco //= 2
    return vetor


def ordenar_partes_s(partes:list[deque[int]], tamanho:int)->list[deque[int]]:
  for i in range(0, tamanho):
      partes[i] = shell_sort(partes[i])
  return partes


def encontrar_maiores(partes:list[deque[int]], indices:dict, maiores:list[int])->int:
    swap_m:np.ndarray[int] = np.array(maiores)
    indice_maximo = swap_m.argmax()
    maximo =  maiores[indice_maximo]
    indice = indices[maximo]
    partes[indice].pop()
    swap:deque[int] = partes[indice]
    if (swap) and (not swap[-1] in maiores):
        maiores.append(1*swap[-1])
    maiores.pop(indice_maximo)
    return -maximo

def sqrt_sort_is(vetor:list[int])->list[int]:
    n:int = len(vetor)
    vetor_swap:list[int] = []
    partes:list[deque[int]] = divide_partes(vetor, n)
    tamanho:int = len(partes)
    partes = ordenar_partes_s(partes, tamanho)
    maiores:list[int] = [partes[i][-1] for i in range(0, tamanho)]
    indices:dict = {p:i for i in range(0, tamanho) for p in partes[i]}
    print(indices)
    i = 0
    while i < n:
        elemento = encontrar_maiores(partes, indices, maiores)
        vetor_swap.append(elemento)
        i += 1
    return vetor_swap