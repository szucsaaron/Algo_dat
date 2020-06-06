class My_ListNode:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.next_val = next
        self.prev_val = prev
        
    def _get_data(self):
        return self.data

    def _set_data(self, new_data):
        self.data = new_data

    def _get_next_val(self):
        return self.next_val

    def _get_prev_val(self):
        return self.prev_val

    def _set_next_val(self, _node):
        self.next_val = _node

    def _set_prev_val(self, _node):
        self.prev_val = _node
