class CashRegister:

    def __init__(self):

        self.total_items = {} # {'item': 'price'}
        self.total_price = 0
        self.discount = 0

    def add_item(self,item):
        self.total_items.update(item)

    def remove_item(self, item):
        self.total_items.pop(item)

    def apply_discount(self, discount_pct):
        self.discount = float(discount_pct)/100

    def get_total(self):
        self.total_price = sum(self.total_items.values())
        return self.total_price * (1-self.discount)

    def show_items(self):
        for key, value in self.total_items.items():
            print(f"{key} | £{value:.2f}")

    def reset_register(self):
        self.total_items = {}
        self.total_price = 0

#Suppose there is one cash register
a = CashRegister()

#Suppose the customer is registering three items: Biscuits, Bananas, Beer
# a.add_item({'Biscuits':1.5},{'Bananas':0.5},{'Beer',12})
a.add_item({'Biscuits':1.5})
a.add_item({'Bananas':0.5})
a.add_item({'Beer':12})

#Suppose the customer is removing one of the items: Beer
a.remove_item('Beer')
#Suppose the customer is part of a loyalty program that is eligible for 5% off of total price
a.apply_discount(5)
#Suppose the customer needs to see the total price at check out
a.get_total()
#Suppose the customer needs to see the total list of items at check out
a.show_items()
#Suppose another customer is at the counter for a new register
a.reset_register()