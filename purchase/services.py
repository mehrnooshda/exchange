from threading import Lock


class PurchaseService:
    def __init__(self):
        self.aggregate_purchases = {}
        self.lock = Lock()

    def buy_from_exchange(self, total_quantity, coin_name):
        print(f"Buying {total_quantity} {coin_name}(s) from exchange")
        return True

    def handle_purchase(self, user, coin_name, quantity):
        COIN_PRICE = 4 # for simplicity every coin costs 4 dollars!
        total_price = quantity * COIN_PRICE

        if user.balance < total_price:
            raise Exception("Insufficient balance")

        user.balance -= total_price
        user.save()

        with self.lock:
            if coin_name not in self.aggregate_purchases:
                self.aggregate_purchases[coin_name] = 0
            self.aggregate_purchases[coin_name] += quantity

            if self.aggregate_purchases[coin_name] * COIN_PRICE >= 10:
                total_quantity = self.aggregate_purchases[coin_name]
                self.buy_from_exchange(total_quantity, coin_name)
                self.aggregate_purchases[coin_name] = 0  # reset the aggregate
