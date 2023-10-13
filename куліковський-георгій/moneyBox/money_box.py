class Money_Box:


    def __init__(self, max_amount, goal, current_amount=0):
        self.max_amount = max_amount
        self.goal = goal
        self.current_amount = current_amount


    def add_coin(self):
        if self.goal - 1 == self.current_amount:
            self.current_amount += 1
            print("Goal is achieved")
        elif self.goal == self.current_amount:
            print("Goal is already achieved")
        else:
            self.current_amount += 1


    def add_amount(self, amount):
        if self.can_add(amount):
            self.current_amount += amount
        else:
            print("Amount is greated then goal")


    def can_add(self, amount):
        if self.goal - (self.current_amount + amount) >= 0:
            return 1
        else:
            return 0


    def __str__(self):
        return f'Goal:{self.goal}, Max amount:{self.max_amount}, Current amount:{self.current_amount}'