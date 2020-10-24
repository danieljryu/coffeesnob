from time import sleep

class Brewer:
    """
    Represents the Brewer - user runs brew walkthrough according to customizable Recipe
    Attrs: grind_size, bean_weight, bloom_time, first(second)_pour_qty, first(second)_pour_time
    Methods:
        Getters and Setters, including attr_str to get string version
        get_brew_recipe: returns all recipe attrs in formatted string
        brew: runs through timed brew recipe according to attrs
    """
    def __init__(self
                 , grind_size=40
                 , bean_weight=20
                 , bloom_time=30
                 , first_pour_qty=200
                 , first_pour_time=60
                 , second_pour_qty=140
                 , second_pour_time=45):
        self.__grind_size = grind_size
        self.__bean_weight = bean_weight
        self.__bloom_time = bloom_time
        self.__first_pour_qty = first_pour_qty
        self.__first_pour_time = first_pour_time
        self.__second_pour_qty = second_pour_qty
        self.__second_pour_time = second_pour_time

    @property
    def grind_size(self):
        return self.__grind_size

    @grind_size.setter
    def grind_size(self,new_grind):
        self.__grind_size = int(new_grind)

    @property
    def bean_weight(self):
        return self.__bean_weight

    @bean_weight.setter
    def bean_weight(self,new_weight):
        self.__bean_weight = int(new_weight)

    @property
    def bloom_time(self):
        return self.__bloom_time

    @bloom_time.setter
    def bloom_time(self,new_weight):
        self.__bloom_time = int(new_weight)

    @property
    def first_pour_qty(self):
        return self.__first_pour_qty

    @first_pour_qty.setter
    def first_pour_qty(self,new_weight):
        self.__first_pour_qty = int(new_weight)

    @property
    def first_pour_time(self):
        return self.__first_pour_time

    @first_pour_time.setter
    def first_pour_time(self,new_weight):
        self.__first_pour_time = int(new_weight)

    @property
    def second_pour_qty(self):
        return self.__second_pour_qty

    @second_pour_qty.setter
    def second_pour_qty(self,new_weight):
        self.__second_pour_qty = int(new_weight)

    @property
    def second_pour_time(self):
        return self.__second_pour_time

    @second_pour_time.setter
    def second_pour_time(self,new_weight):
        self.__second_pour_time = int(new_weight)

    def get_brew_recipe(self):
        recipe_list = [
            ('Grams of beans per cup (bean_weight): ', self.__bean_weight),
            ('Setting on grinder (grind_size): ', self.__grind_size),
            ('Seconds to let bloom (bloom_time): ', self.__bloom_time),
            ('Grams of water per cup in first pour (first_pour_qty): ', self.__first_pour_qty),
            ('Seconds during/after first pour (first_pour_time): ', self.__first_pour_time),
            ('Grams of water per cup in second pour (second_pour_qty): ', self.__second_pour_qty),
            ('Seconds during/after second pour (second_pour_time): ', self.__second_pour_time),
        ]
        output_str = ''
        for pair in recipe_list:
            output_str += pair[0]
            output_str += str(pair[1])
            output_str += '\n'
        return output_str

    def brew(self,cups):
        elapsed_pour_weight = 0
        print('\n~~ Welcome to your Brew Walkthrough! ~~')
        print(f'Grind {self.__bean_weight*cups:.0f}g of coffee to a setting of {self.__grind_size}')
        input('Press Enter to continue...')
        print(f'\nPour initial bloom of {self.__bean_weight*cups*2:.0f}g.')
        sleep(1)
        print('~~~Wait~~~')
        elapsed_pour_weight += self.__bean_weight*cups*2
        sleep(self.__bloom_time)
        elapsed_pour_weight += self.__first_pour_qty*cups
        print(f'\nStart first pour of {self.__first_pour_qty*cups:.0f}g '
              f'(to total of {elapsed_pour_weight:.0f}g) quickly.')
        sleep(1)
        print('~~~Wait~~~')
        sleep(self.__first_pour_time)
        elapsed_pour_weight += self.__second_pour_qty*cups
        print(f'\nStart second pour of {self.__second_pour_qty*cups:.0f}g '
              f'(to total of {elapsed_pour_weight:.0f}g) slowly.')
        sleep(1)
        print('~~~Wait~~~')
        sleep(self.__second_pour_time)
        print(f'Your {cups:.1f} cups of coffee should be done! Pour & enjoy!')
