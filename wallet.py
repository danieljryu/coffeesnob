from datetime import datetime


class Wallet:
    """
    Represents all financial record keeping
    Attrs: transaction_history, balance (sum of all transactions)
    Methods:
        Getters and Setters, including attr_str to get string version
        add_money: adds transaction to transaction_history, adds to balance
        pay_money: adds transaction to transaction_history, subtracts from balance
        get_spend: returns sum of all payments (negative values) from transaction_history
        get_savings: diff of all coffee spend and equivalent starbucks spend ($3 americano)
    """

    def __init__(self):
        self.__transaction_history = []
        self.__balance = 0

    @property
    def transaction_history(self):
        return self.__transaction_history

    def transaction_history_str(self):
        output_str = 'Transaction History:\n'
        for entry in self.__transaction_history:
            if entry[1] >= 0:
                output_str += '\t{} - ${:6,.2f} - {}\n'.format(entry[0].strftime('%Y-%m-%d'), entry[1], entry[2])
            else:
                output_str += '\t{} - (${:6,.2f}) - {}\n'.format(entry[0].strftime('%Y-%m-%d'), -entry[1], entry[2])
        return output_str

    def add_money(self, note, value):
        if value < 0:
            raise ValueError(0)
        else:
            self.__transaction_history.append((datetime.today(), value, note))
            self.__balance += value
        return self.__balance

    def pay_money(self, note, value):
        if value > self.__balance:
            raise ValueError(self.__balance)
        else:
            self.__transaction_history.append((datetime.today(), -value, note))
            self.__balance -= value
        return self.__balance

    @property
    def balance(self):
        return self.__balance

    def get_spend(self):
        payment_list = [-val for dt, val, note in self.__transaction_history if val < 0 and note.startswith('Bought')]
        return sum(payment_list)

    def get_savings(self):
        """relies on each payment being for 1 lb of beans"""

        payment_list = [-val for dt, val, note in self.__transaction_history if val < 0 and note.startswith('Bought')]
        lbs_coffee = len(payment_list)

        # Starbucks Grande Americano: 470g water -> 24g coffee/$3 -> $0.125/g coffee
        starbucks_spend = lbs_coffee*.125*454
        savings = starbucks_spend - sum(payment_list)

        return savings

    