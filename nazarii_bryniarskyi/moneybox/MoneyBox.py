


class MoneyBox:

    def __init__(self, storage_limit):
        self.storage_limit = storage_limit
        self.coin_amount = 0

    def add(self, coins):
        if self.can_add(coins):
            self.coin_amount += coins
        else:
            print("Coins were not added. Storage is full or coin amount is < 0.")

    def can_add(self, coins):
        if self.coin_amount + coins <= self.storage_limit and self.check_coins(coins):
            return True
        return False

    def storage(self):
        return self.coin_amount

    @staticmethod
    def check_coins(coins):
        return True if coins >= 0 else False

    def __str__(self):
        return f"Storage limit: {self.storage_limit}, coins in box: {self.storage()}"
