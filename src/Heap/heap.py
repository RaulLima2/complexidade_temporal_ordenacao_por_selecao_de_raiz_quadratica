class Heap:
    def __init__(self):
        self.heap:list[int] = []

    def parent(self, i)->int:
        return (i - 1) // 2

    def left_child(self, i)->int:
        return 2 * i + 1

    def right_child(self, i)->int:
        return 2 * i + 2

    def insert(self, key)->None:
        self.heap.append(key)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def heapify(self, i)->None:
        largest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(largest)

    def extract_max(self)->int|None:
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        return max_val

    def get_max(self)->int|None:
        return self.heap[0] if self.heap else None