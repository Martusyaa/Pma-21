class MoneyBox:

    def __init__(self, storage_limit):
        self.storage_limit = storage_limit
        self.coin_amount = 0
        self.NOT_ADDED_EXCEPTION = "Coins were not added. Storage is full or coin amount is < 0."


    def add(self, coins):
        if not self.can_add(coins):
            raise ValueError(self.NOT_ADDED_EXCEPTION)

        self.coin_amount += coins


    def can_add(self, coins):
        return 0 <= coins <= self.storage_limit - self.coin_amount


    def storage(self):
        return self.coin_amount


    def __str__(self):
        return f"Storage limit: {self.storage_limit}, coins in box: {self.storage()}"
