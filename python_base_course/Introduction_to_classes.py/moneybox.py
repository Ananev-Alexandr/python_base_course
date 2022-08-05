class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
    def can_add(self, value):
        if value <= self.capacity:
            return True
        else:
            return False
    def add(self, value):
        if  self.can_add(value) == True:
            self.capacity = self.capacity - value
        return False
            
