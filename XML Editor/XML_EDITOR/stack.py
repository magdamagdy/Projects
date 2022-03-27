class node:
    def __init__(self):
        self.item = None
        self.next = None
class stack_imp:
    def __init__(self):
        self.top = None
        self.size=0
    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False
    def push(self,item):
        if self.top is None:
            new_node = node()
            new_node.item = item
            new_node.next = None
            self.top = new_node
            self.size+=1
        else:
            new_node = node()
            new_node.item = item
            new_node.next = self.top
            self.top = new_node
            self.size+=1
    def pop(self):
        if self.top is not None:
            self.pop_element = self.top
            self.top = self.top.next
            self.size-=1
    def get_top(self):
        if self.top != None:
            return self.top.item

    def get_size(self):
        return self.size



