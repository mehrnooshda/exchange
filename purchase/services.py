from threading import Lock


class PurchaseService:
    SUPPORTED_COINS = {
        'BTC': 10,  # Bitcoin
        'ETH': 4,  # Ethereum
        'XRP': 1,  # Ripple
        'ADA': 2,  # Cardano
        'LTC': 3  # Litecoin
    }

    def __init__(self):
        self.aggregate_purchases = {coin: 0 for coin in self.SUPPORTED_COINS}
        self.lock = Lock()

    def buy_from_exchange(self, total_quantity, coin_name):
        print(f"Buying {total_quantity} {coin_name}(s) from exchange")
        return True

    def handle_purchase(self, user, coin_name, quantity):
        if coin_name not in self.SUPPORTED_COINS:
            raise ValueError(
                f"Coin '{coin_name}' is not available. Please choose from: {', '.join(self.SUPPORTED_COINS.keys())}")

        coin_price = self.SUPPORTED_COINS[coin_name]
        total_price = quantity * coin_price

        if user.balance < total_price:
            raise ValueError("Insufficient balance to complete this transaction.")

        user.balance -= total_price
        user.save()

        with self.lock:
            self.aggregate_purchases[coin_name] += quantity

            if self.aggregate_purchases[coin_name] * coin_price >= 10:
                total_quantity = self.aggregate_purchases[coin_name]
                self.buy_from_exchange(total_quantity, coin_name)
                self.aggregate_purchases[coin_name] = 0  # Reset the aggregate
