from datetime import datetime


class Order:
    """
    represents the ordering platform
    Attrs: order_history (list of orders (date,price,name)), catalog (dict of names and prices)
    Methods:
        Getters and Setters, including attr_str to get string version
        get_price: returns price from __catalog, None if not found
        make_order: if name is valid, appends order to __order_history.
                    must be accompanied by Wallet and Canister funcs
    """
    def __init__(self):
        self.__catalog = {'Ethiopia': 24, 'Kenya': 22, 'Brazil': 18, 'Costa Rica': 19, 'Mexico': 17}
        self.__order_history = []

    @property
    def catalog(self):
        return self.__catalog

    def catalog_str(self):
        output_str = 'Available items:\n'
        for product,price in self.__catalog.items():
            output_str += '\t{} -- ${:6,.2f}\n'.format(product, price)
        return output_str

    @property
    def order_history(self):
        return self.__order_history

    def order_history_str(self):
        output_str = 'Order History:\n'
        for entry in self.__order_history:
            output_str += '\t{} - ${:6,.2f} - {}\n'.format(entry[0].strftime('%Y-%m-%d'), entry[1], entry[2])
        return output_str

    def get_price(self,name):
        return self.__catalog.get(name)

    def make_order(self, name):
        price = self.get_price(name)
        if price:
            self.__order_history.append((datetime.today(), price, name))


