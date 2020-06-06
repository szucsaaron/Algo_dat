class MaxHeap:
    def __init__(self, init_capacity):
        self.heap = init_capacity * [None]
        self.size = 0
        self.init_capacity = init_capacity

    def parent(self, index):
        return int((index - 1) / 2)

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def has_parent(self, index):
        return self.parent(index) >= 0

    def has_left_child(self, index):
        return self.left_child(index) < self.size

    def has_right_child(self, index):
        return self.right_child(index) < self.size

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, element):
        if element is None:
            raise ValueError
        else:
            if self.size >= self.init_capacity:
                self.heap += self.init_capacity * [None]
                self.init_capacity *= 2

            self.heap[self.size] = element
            # self.heap.append(key)
            self.size += 1
            self.heapify_up(self.size - 1)

    def heapify_up(self, index):
        while self.has_parent(index) and self.heap[index] < self.heap[self.parent(index)]:
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def print_heap(self):
        print(self.heap)

    def get_heap(self):
        return self.heap

    def delete_min(self):
        if self.size is 0:
            return None
        else:
            last_index = self.size - 1
            root = self.heap[0]
            self.swap(0, last_index)
            self.heap[last_index] = None
            self.heapify_down(0)
            self.size -= 1
            return root

    def heapify_down(self, index):
        while self.has_left_child(index):
            min_child_ind = self.get_min_child_ind(index)
            if min_child_ind is None:
                break
            if self.heap[index] > self.heap[min_child_ind]:
                self.swap(index, min_child_ind)
                index = min_child_ind
            else:
                break

    def get_min_child_ind(self, index):
        if self.has_left_child(index):
            left_c = self.left_child(index)
            if self.has_right_child(index):
                right_c = self.right_child(index)
                if self.heap[left_c] < self.heap[right_c]:
                    return left_c
                else:
                    return right_c


mp = MaxHeap(4)

for i in [1, 2, 3, 4, 10, -1]:
    mp.insert(i)

mp.get_heap()
print(mp.delete_min())
mp.get_heap()