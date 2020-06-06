class MaxHeap:
    def __init__(self, init_capacity):
        self.heap = []
        self.size = 0
        self.init_capacity = init_capacity

    def get_parent(self, i):
        return int((i - 1) / 2)

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def has_parent(self, i):
        return self.get_parent(i) >= 0

    def has_left_child(self, i):
        return self.left_child(i) < self.size

    def has_right_child(self, i):
        return self.right_child(i) < self.size

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, key):
        self.heap.append(key)
        self.size += 1
        self.heapify_up(self.size - 1)

    def heapify_up(self, i):
        while self.has_parent(i) and self.heap[i] < self.heap[self.get_parent(i)]:
            self.swap(i, self.get_parent(i))
            i = self.get_parent(i)

    def get_heap(self):
        print(self.heap)

    def delete_min(self):
        if self.size is 0:
            return None
        else:
            last_index = self.size - 1
            self.swap(0, last_index)
            root = self.heap.pop()
            self.heapify_down(0)
            self.size -= 1
            return root

    def heapify_down(self, i):
        while self.has_left_child(i):
            max_child_ind = self.get_max_child_ind(i)
            if max_child_ind is None:
                break
            if self.heap[i] > self.heap[max_child_ind]:                     #AND HERE
                self.swap(i, max_child_ind)
                i = max_child_ind
            else:
                break

    def get_max_child_ind(self, i):
        if self.has_left_child(i):
            left_c = self.left_child(i)
            if self.has_right_child(i):
                right_c = self.right_child(i)
                if self.heap[left_c] > self.heap[right_c]:
                    return left_c
                else:
                    return right_c
        else:
            return 1


mp = MaxHeap()

for i in [1, 2, 3, 4, 0]:
    mp.insert(i)

mp.get_heap()