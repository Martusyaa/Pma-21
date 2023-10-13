class Money_Box:
    
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_amount = 0
        
    
    def add_coin(self, amount):
        if self.can_add(amount):
            self.current_amount += amount
        else:
            print("Amount is greated then goal")
            
    
    def can_add(self, amount):
        if self.capacity - (self.current_amount + amount) >= 0:
            return 1
        else:
            return 0
        
        
    def __str__(self):
        return f'Max amount:{self.capacity}, Current amount:{self.current_amount}'