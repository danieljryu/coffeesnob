from canister import Canister
from brewer import Brewer
from journal import Journal
from order import Order
from wallet import Wallet
from exception import get_user_choice, get_user_qty
from time import sleep


class Snob:
    """
    Main controller class. Holds instance of all other classes, runs the show
    Attrs: name, Canister, Brewer, Journal, Order, Wallet
    Methods:
        main_menu: displays options, calls submenu func from below, with option to return to main menu or quit:
        canister_menu:
            1) View Contents: Show Canister attrs 
            2) Remaining Cups: get grams per cup from Brewer, returns remaining cups in Canister
            3) Dump Beans: zero out all attrs
        brewer_menu:
            1) Brew Walkthrough: run through timed brew recipe
            2) View Brew Recipe
            3) Edit Brew Recipe
        order_menu:
            1) Show Catalog: show available beans to buy and prices
            2) Order Beans: deduct money from Wallet, add beans to Canister, record transaction
            3) Show Order History
        wallet_menu:
            1) Get Balance
            2) Add Money
            3) Withdraw Money
            4) See Total Spent: Add up money spent ordering beans
            5) See Savings: compare total spend to comparable cost of ordering the same amount of coffee
            6) View History: Show transaction history (add, withdraw, and buy beans)
        journal_menu:
            1) Write Entry
            2) View Entry Titles
            3) View Entry
            4) Edit Entry
            5) Delete Entry
    """

    def __init__(self, name='Taylor Anybody'):
        self.__name = name.title()
        self.__canister = Canister()
        self.__brewer= Brewer()
        self.__journal = Journal()
        self.__order = Order()
        self.__wallet = Wallet()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def display_menu_options(self, option_list):
        """Goes through option_list, prints options with numbers. returns user choice as a string"""
        print('What would you like to do?')
        for i in range(len(option_list)):
            print(f'\t[{i+1}] {option_list[i]}')
        print('\t[0] Return to Main Menu\n\t[q] Quit')

        valid_choices = [str(i) for i in range(len(option_list)+1)]
        menu_choice = get_user_choice(f'Your choice (0-{len(option_list)} or \'q\' to quit): ', valid_choices)
        return menu_choice

    def main_menu(self):
        menu_choices = {
            '1': self.canister_menu,
            '2': self.brewer_menu,
            '3': self.order_menu,
            '4': self.wallet_menu,
            '5': self.journal_menu
        }
        menu_choice = '1'
        while menu_choice in menu_choices.keys():
            sleep(1.5)
            print(f'\n---- Main Menu ----\nHello, {self.__name.title()}! What would you like to check out?')
            print('\t[1] Canister')
            print('\t[2] Brewer')
            print('\t[3] Bean Ordering')
            print('\t[4] Wallet')
            print('\t[5] Journal')
            print('\t[q] Quit')

            menu_choice = get_user_choice('Your choice (1-5 or \'q\' to quit): ', list(menu_choices.keys()))

            # get_user_choice returns None if user enters 'q'
            if not menu_choice:
                break

            # Execute the func from the menu_choices dict
            sub_choice = menu_choices.get(menu_choice)()

            # all sub menus return None if user quits ('q') from sub-menu
            if not sub_choice:
                break

        print('Program closed, have a great day!')

    def canister_menu(self):
        while True:
            sleep(1.5)
            print('\n---- Canister ----')
            menu_options = ['View Contents', 'Remaining Cups', 'Dump Beans']
            menu_choice = self.display_menu_options(menu_options)

            # View Contents
            if menu_choice == '1':
                if self.__canister.weight == 0:
                    print('You currently have no beans, disaster!')
                else:
                    print(f'You have {self.__canister.weight}g of {self.__canister.name} beans from '
                          f'{self.__canister.purchase_date_str()}')

            # Remaining Cups
            elif menu_choice == '2':
                remaining_cups = self.__canister.remaining_cups(self.__brewer.bean_weight)
                if remaining_cups == 0:
                    print('You have no coffee beans. No beans, no coffee!')
                else:
                    print('You can make',remaining_cups,'more cups of coffee with the beans you have')

            # Dump Beans
            elif menu_choice == '3':
                if self.__canister.weight == 0:
                    print('Your canister is already empty!')
                else:
                    print('Throwing out', self.__canister.weight, 'g of coffee beans. What a waste...')
                    self.__canister.use_beans(self.__canister.weight)
            elif menu_choice == '0':
                return True
            elif not menu_choice:
                return None

    def brewer_menu(self):
        while True:
            sleep(1.5)
            print('\n---- Brewer ----')
            menu_options = ['Brew Walkthrough','View Brew Recipe','Edit Brew Recipe']
            menu_choice = self.display_menu_options(menu_options)

            # Brew Walkthrough
            if menu_choice == '1':
                max_cups = self.__canister.weight/self.__brewer.bean_weight
                if max_cups < 0.1:
                    print('Not enough coffee! Go buy more beans before you try to brew.')
                    continue
                input_prompt = f'How many cups would you like to brew? {max_cups} cups remaining, or \'q\' to quit: '
                cups = get_user_qty(input_prompt, max_cups, 1)

                # if user wants to quit 'q'
                if not cups:
                    continue
                qty_used = self.__brewer.bean_weight*cups
                self.__canister.use_beans(qty_used)
                self.__brewer.brew(cups)

            # View Brew Recipe
            elif menu_choice == '2':
                print(self.__brewer.get_brew_recipe())

            # Edit Brew Recipe
            elif menu_choice == '3':
                print('Current Brew Recipe:\n', self.__brewer.get_brew_recipe())

                weight_prompt = f'Bean Weight, or \'q\' to keep existing value ({self.__brewer.bean_weight}): '
                weight = get_user_qty(weight_prompt, 100, 1)
                if weight:
                    self.__brewer.bean_weight = weight

                grind_prompt = f'Grind Size, or \'q\' to keep existing value ({self.__brewer.grind_size}): '
                grind = get_user_qty(grind_prompt, 40, 1)
                if grind:
                    self.__brewer.grind_size = grind

                bloom_time_prompt = f'Bloom Time, or \'q\' to keep existing value ({self.__brewer.bloom_time}): '
                bloom_time = get_user_qty(bloom_time_prompt, 60, 1)
                if bloom_time:
                    self.__brewer.bloom_time = bloom_time

                first_pour_qty_prompt = f'First Pour Qty, or \'q\' to keep existing value ({self.__brewer.grind_size}): '
                first_pour_qty = get_user_qty(first_pour_qty_prompt, 100, 1)
                if first_pour_qty:
                    self.__brewer.first_pour_qty = first_pour_qty

                first_pour_time_prompt = f'First Pour Time, or \'q\' to keep existing value ({self.__brewer.grind_size}): '
                first_pour_time = get_user_qty(first_pour_time_prompt,120,1)
                if first_pour_time:
                    self.__brewer.first_pour_time = first_pour_time

                second_pour_qty_prompt = f'Second Pour Qty, or \'q\' to keep existing value ({self.__brewer.grind_size}): '
                second_pour_qty = get_user_qty(second_pour_qty_prompt, 100, 1)
                if second_pour_qty:
                    self.__brewer.second_pour_qty = second_pour_qty

                second_pour_time_prompt = f'Second Pour Time, or \'q\' to keep existing value ({self.__brewer.grind_size}): '
                second_pour_time = get_user_qty(second_pour_time_prompt,120,1)
                if second_pour_time:
                    self.__brewer.second_pour_time = second_pour_time

                print('\nNew Brew Recipe:\n', self.__brewer.get_brew_recipe())
            elif menu_choice == '0':
                return True
            elif not menu_choice:
                return None

    def order_menu(self):
        while True:
            sleep(1.5)
            print('\n---- Order ----')
            menu_options = ['Show Catalog', 'Order Beans', 'Show Order History']
            menu_choice = self.display_menu_options(menu_options)

            # Show Catalog
            if menu_choice == '1':
                print(self.__order.catalog_str())

            # Order Beans
            elif menu_choice == '2':
                if self.__canister.weight > 0:
                    print('You still have beans! Use them or throw them away to buy more.')
                    continue

                # include lower, upper, and camel case versions in possibilities
                bean_names_lower = [key.lower() for key in self.__order.catalog.keys()]
                bean_names_upper = [key.upper() for key in self.__order.catalog.keys()]
                bean_names_title = [key.title() for key in self.__order.catalog.keys()]
                bean_names = bean_names_lower + bean_names_upper + bean_names_title

                input_prompt = self.__order.catalog_str()+'Which beans would you like, or \'q\' to quit: '
                bean_choice = get_user_choice(input_prompt, bean_names)

                # if user wants to quit 'q'
                if not bean_choice:
                    continue
                bean_choice = bean_choice.title()
                bean_price = self.__order.get_price(bean_choice)
                if bean_price > self.__wallet.balance:
                    print('Insufficient balance in Wallet: (${:6,.2f})'.format(self.__wallet.balance))
                    print('Please add more funds or choose another bean!')
                    continue
                self.__order.make_order(bean_choice)
                self.__wallet.pay_money(f'Bought beans ({bean_choice})', bean_price)
                self.__canister.add_beans(bean_choice, 454)
                print('Purchased {} beans for ${:6,.2f}'.format(bean_choice, bean_price))

            # Show Order History
            elif menu_choice == '3':
                print(self.__order.order_history_str())
            elif menu_choice == '0':
                return True
            elif not menu_choice:
                return None

    def wallet_menu(self):
        while True:
            sleep(1.5)
            print('\n---- Wallet ----')
            menu_options = ['Get Balance', 'Add Money', 'Withdraw Money',
                            'See Total Spent', 'See Savings', 'View History']
            menu_choice = self.display_menu_options(menu_options)

            # Get Balance
            if menu_choice == '1':
                print('Remaining Balance: ${:6,.2f}'.format(self.__wallet.balance))

            # Add Money
            elif menu_choice == '2':
                add_value = get_user_qty('How much would you like to add, or \'q\' to quit: ', 1000)
                # if user wants to quit 'q'
                if not add_value:
                    continue
                self.__wallet.add_money('Funds added',add_value)
                print('${:6,.2f} added to wallet!'.format(add_value))

            # Withdraw Money
            elif menu_choice == '3':
                if self.__wallet.balance <= 0:
                    print('No available balance to withdraw! Please add funds to withdraw.')
                    continue
                pull_value = get_user_qty('How much would you like to withdraw, or \'q\' to quit: ', self.__wallet.balance)
                self.__wallet.pay_money('Funds withdrawn', pull_value)
                print('${:6,.2f} withdrawn from wallet!'.format(pull_value))

            # See Total Spent
            elif menu_choice == '4':
                print('Total spend: ${:6,.2f}'.format(self.__wallet.get_spend()))

            # See Total Savings
            elif menu_choice == '5':
                print('Total savings (based off a $3 St*rbucks grande Americano: '
                      '${:6,.2f}'.format(self.__wallet.get_savings()))

            # View Transaction History
            elif menu_choice == '6':
                print(self.__wallet.transaction_history_str())
            elif menu_choice == '0':
                return True
            elif not menu_choice:
                return None

    def journal_menu(self):
        while True:
            sleep(1.5)
            print('\n---- Journal ----')
            menu_options = ['Write Entry', 'View Entry Titles', 'View Entry', 'Edit Entry', 'Delete Entry']
            menu_choice = self.display_menu_options(menu_options)

            # Write Entry
            if menu_choice == '1':
                title = str(input('What is the title of your entry: '))
                body = str(input('What is the body of your entry (press Enter to finish):\n'))
                self.__journal.write_entry(title, body)

            # View Entry Titles
            elif menu_choice == '2':
                print('Entry_Titles: ')
                print(self.__journal.get_title_str())

            # View Entry
            elif menu_choice == '3':
                titles = self.__journal.get_title_str()
                input_prompt = f'Which entry would you like to view?\n{titles}Your choice, or \'q\' to quit: '
                title = get_user_choice(input_prompt, self.__journal.get_titles())
                # if user wants to quit 'q'
                if not title:
                    continue
                print(self.__journal.get_entry_str(title))

            # Edit Entry
            elif menu_choice == '4':
                titles = self.__journal.get_title_str()
                input_prompt = f'Which entry would you like to edit?\n{titles}Your choice, or \'q\' to quit: '
                title = get_user_choice(input_prompt, self.__journal.get_titles())
                # if user wants to quit 'q'
                if not title:
                    continue
                print(self.__journal.get_entry_str(title))
                body = str(input('\nWhat is the new body of your entry (press Enter to finish):\n'))
                self.__journal.write_entry(title, body)
                print(f'Entry \'{title}\' edited!')

            # Delete Entry
            elif menu_choice == '5':
                titles = self.__journal.get_title_str()
                input_prompt = f'Which entry would you like to delete?\n{titles}Your choice, or \'q\' to quit: '
                title = get_user_choice(input_prompt, self.__journal.get_titles())
                if self.__journal.delete_entry(title):
                    print(f'Entry \'{title}\' deleted!')
            elif menu_choice == '0':
                return True
            elif not menu_choice:
                return None


if __name__ == "__main__":
    name = input('Enter your name: ')
    snob1 = Snob(name)
    snob1.main_menu()
