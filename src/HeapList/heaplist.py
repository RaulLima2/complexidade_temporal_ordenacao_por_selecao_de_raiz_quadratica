from Heap import Heap

class HeapList:
    def __init__(self):
        self.heap:list[Heap] = []

    def parent(self, i:int)->int:
        return (i - 1) // 2

    def left_child(self, i:int)->int:
        return 2 * i + 1

    def right_child(self, i:int)->int:
        return 2 * i + 2

    def insert(self, key:Heap)->None:
        if len(key.heap) != 0:
            self.heap.append(key)
            i = len(self.heap) - 1
            while i > 0 and self.heap[self.parent(i)].get_max() < self.heap[i].get_max():
                self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
                i = self.parent(i)

    def heapify(self, i:int)->None:
        largest = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < len(self.heap) and self.heap[left].get_max() > self.heap[largest].get_max():
            largest = left

        if right < len(self.heap) and self.heap[right].get_max() > self.heap[largest].get_max():
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(largest)

    def extract_max(self)->Heap|None:
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        return max_val
    

    def get_max(self)->Heap|None:
        return self.heap[0] if self.heap else None