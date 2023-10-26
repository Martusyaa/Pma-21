from Validator import Validator

class MoneyBox():
    def __init__(self, assets_limit):
        self.assets_limit = assets_limit
        self.assets = 0

    @Validator
    def add_asset(self, amount):
        self.assets += amount

    def box_status(self):
         print(self.assets)
