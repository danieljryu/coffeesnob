from datetime import datetime


class Canister:
    """
    Represents a coffee canister, which holds 1lb of coffee beans.
    Attrs: name (of bean), weight (in g), purchase_date
    Methods:
        Getters and Setters, including attr_str to get string version
        add_beans: adds new beans to the canister and sets the purchase date to today
        remaining_cups: takes grams of beans per cup, returns how many cups left
        use_beans: takes grams of beans to use, depletes the __weight that amount, zeroes it out if all beans used
    """

    def __init__(self):
        self.__name = ''
        self.__weight = 0
        self.__purchase_date = ''

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self,value):
        self.__weight = value

    @property
    def purchase_date(self):
        return self.__purchase_date

    def purchase_date_str(self):
        return self.__purchase_date.strftime('%Y-%m-%d')

    @purchase_date.setter
    def purchase_date(self,dt):
        self.__purchase_date = dt

    def add_beans(self, name, weight):
        self.__name = name
        self.__weight = weight
        self.__purchase_date = datetime.today()

    def remaining_cups(self, one_cup_weight):
        return round(self.__weight/one_cup_weight, 2)

    def use_beans(self, weight):
        if weight > self.__weight:
            raise ValueError(self.__weight)
        if weight == self.__weight:
            self.__name = ''
            self.__purchase_date = ''
        self.__weight -= weight
