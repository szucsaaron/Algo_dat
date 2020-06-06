class MyListNode:
    def __init__(self, element):
        self.element = element
        self.next = None

    def get_element(self):
        return self.element

    def set_element(self, element):
        self.element = element

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next
