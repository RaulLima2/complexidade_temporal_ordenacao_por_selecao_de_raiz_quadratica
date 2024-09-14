import math
from Heap import Heap
from HeapList import HeapList

def make_heap(vetor:list[int])->Heap:
  heap:Heap = Heap()
  for i in vetor:
    heap.insert(i)
  return heap

def insert_heap(heap:Heap, elem:int)->None:
   heap.insert(-1*elem)

def remover_maximo(heap:HeapList)->Heap:
  return heap.extract_max()

def pegar_maior_elemento_heap(heap_maiores:HeapList)->Heap:
  max_value = remover_maximo(heap_maiores)
  return max_value

def particionar(vetor:list[int], n_partes:int)->list[list[int]]:
  partes:list[list[int]] = []
  sqrt_n:int = int(math.sqrt(n_partes))
  for i in range(0, n_partes, sqrt_n):
      partes.append(vetor[i:i + sqrt_n])
  return partes

def ordenar_partes(partes:list[list])->HeapList:
  partes_heap:HeapList = HeapList()
  for i in range(0, len(partes)):
      item:Heap = Heap()
      item = make_heap(partes[i])
      partes_heap.insert(item)
  return partes_heap


def sqrt_sort_h(vetor:list[int])->list[int]:
  tamanho:int = len(vetor)
  vetor_swap:list[int] = []
  partes:list[list[int]] = particionar(vetor, tamanho)
  partes_heap:HeapList = ordenar_partes(partes)
  while partes_heap.heap:
      item_heap = pegar_maior_elemento_heap(partes_heap)
      if item_heap.heap:
        elemento = item_heap.extract_max()
        vetor_swap.append(elemento)
        partes_heap.insert(item_heap)
  return vetor_swap